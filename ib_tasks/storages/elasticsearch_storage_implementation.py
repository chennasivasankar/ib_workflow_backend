"""
Created on: 07/08/20
Author: Pavankumar Pamuru

"""
from typing import Tuple, Dict

from elasticsearch_dsl import Q, Search

from ib_tasks.constants.enum import Operators, FieldTypes
from ib_tasks.documents.elastic_task import *
from ib_tasks.documents.elastic_task import ElasticFieldDTO, \
    Field
from ib_tasks.documents.elastic_task import ElasticTaskDTO, Task, QueryTasksDTO
from ib_tasks.interactors.storage_interfaces.elastic_storage_interface import \
    ApplyFilterDTO
from ib_tasks.interactors.storage_interfaces.elastic_storage_interface import \
    ElasticSearchStorageInterface
from ib_tasks.interactors.storage_interfaces.fields_storage_interface import \
    FieldTypeDTO
from ib_tasks.interactors.storage_interfaces.stage_dtos import TaskStageIdsDTO
from ib_tasks.interactors.task_dtos import TaskDetailsConfigDTO, SearchQueryDTO


class ElasticSearchStorageImplementation(ElasticSearchStorageInterface):

    def create_task(self, elastic_task_dto: ElasticTaskDTO) -> str:
        from elasticsearch_dsl import connections
        from django.conf import settings
        es = connections.create_connection(
            hosts=[settings.ELASTICSEARCH_ENDPOINT],
            timeout=20)
        task_dict = self._get_task_dict(elastic_task_dto)
        import json
        task_dict = json.dumps(task_dict)
        doc = es.index(
            index=TASK_INDEX_NAME,
            ignore=400,
            doc_type='_doc',
            body=json.loads(task_dict))
        return doc['_id']

    def update_task(self, task_dto: ElasticTaskDTO):
        from elasticsearch_dsl import connections
        from django.conf import settings
        es = connections.create_connection(
            hosts=[settings.ELASTICSEARCH_ENDPOINT],
            timeout=20)

        from ib_tasks.models import ElasticSearchTask
        task_id = task_dto.task_id
        elastic_search_task_id = ElasticSearchTask.objects.get(
            task_id=task_id
        ).elasticsearch_id
        task_dict = self._get_task_dict(task_dto)
        import json
        task_dict = json.dumps(task_dict)
        es.index(
            index=TASK_INDEX_NAME,
            ignore=400,
            doc_type='_doc',
            id=elastic_search_task_id,
            body=json.loads(task_dict))

    def _get_task_dict(self, elastic_task_dto: ElasticTaskDTO):
        task_dict = {
            "project_id": elastic_task_dto.project_id,
            "template_id": elastic_task_dto.template_id,
            "task_id": elastic_task_dto.task_id,
            "title": elastic_task_dto.title
        }
        fields_dict = {}
        for field in elastic_task_dto.fields:
            field_dict = {field.field_id: field.value}
            fields_dict.update(field_dict)
        task_dict.update(fields_dict)
        stages = self._get_stages_dict(elastic_task_dto.stages)
        task_dict['stages'] = stages
        return task_dict

    @staticmethod
    def _get_stages_dict(stages_ids: List[str]) -> List[Dict[str, Any]]:
        return [
            {"stage_id": stage_id}
            for stage_id in stages_ids
        ]

    def filter_tasks(
            self, filter_dtos: List[ApplyFilterDTO], offset: int,
            stage_ids: List[str], limit: int, project_id: str,
            field_type_dtos: List[FieldTypeDTO]) -> Tuple[List[int], int]:
        from elasticsearch_dsl import connections
        from django.conf import settings
        connections.create_connection(hosts=[settings.ELASTICSEARCH_ENDPOINT],
                                      timeout=20)
        search = self._get_filter_task_objects(filter_dtos, field_type_dtos)

        query = Q('terms', stages__stage_id__keyword=stage_ids) \
                & Q('term', project_id__keyword=project_id)

        task_objects = search.filter(query)

        total_tasks = task_objects.count()
        return [
                   task_object.task_id
                   for task_object in task_objects[offset: offset + limit]
               ], total_tasks

    @staticmethod
    def _get_search_task_objects(filter_dtos: List[ApplyFilterDTO]):

        query = None
        for counter, item in enumerate(filter_dtos):
            attribute = item.field_id + '.keyword'
            current_queue = Q('term', project_id__keyword=item.project_id) \
                            & Q('term', template_id__keyword=item.template_id) \
                            & Q('term', **{attribute: item.value})
            if counter == 0:
                query = current_queue
            else:
                query = query & current_queue

        search = Search(index=TASK_INDEX_NAME)
        if query is None:
            task_objects = search
        else:
            task_objects = search.filter(query)
        return task_objects

    def search_tasks(
            self, search_query_dto: SearchQueryDTO,
            apply_filter_dtos: List[ApplyFilterDTO],
            stage_ids: List[str], field_type_dtos: List[FieldTypeDTO]
    ) -> QueryTasksDTO:
        from elasticsearch_dsl import connections
        from django.conf import settings
        connections.create_connection(hosts=[settings.ELASTICSEARCH_ENDPOINT],
                                      timeout=20)
        offset = search_query_dto.offset
        limit = search_query_dto.limit
        project_id = search_query_dto.project_id
        search_query = search_query_dto.query_value
        from elasticsearch_dsl import Q
        search = self._get_filter_task_objects(apply_filter_dtos, field_type_dtos)
        query = Q('term', project_id__keyword=project_id) \
                & Q('terms', stages__stage_id__keyword=stage_ids)
        if search_query:
            query = query & Q("match", title={"query": search_query, "fuzziness": "AUTO"})
        search = search.query(query)
        total_tasks_count = search.count()
        task_ids = [
            hit.task_id
            for hit in search[offset: offset + limit]
        ]
        return QueryTasksDTO(
            total_tasks_count=total_tasks_count,
            task_ids=task_ids
        )

    def filter_tasks_with_stage_ids(
            self, filter_dtos: List[ApplyFilterDTO], field_type_dtos: List[FieldTypeDTO],
            task_details_config: TaskDetailsConfigDTO) -> Tuple[
        List[TaskStageIdsDTO], int]:
        from elasticsearch_dsl import connections
        from django.conf import settings
        connections.create_connection(hosts=[settings.ELASTICSEARCH_ENDPOINT],
                                      timeout=20)
        stage_ids = task_details_config.stage_ids
        search_query = task_details_config.search_query
        search = self._get_filter_task_objects(filter_dtos, field_type_dtos)
        search = search.filter('terms', stages__stage_id__keyword=stage_ids)
        query = Q('terms', stages__stage_id__keyword=stage_ids) \
                & Q('term', project_id__keyword=task_details_config.project_id)

        if search_query:
            query = query & Q(
                    "match",
                    title={
                        "query": search_query,
                        "fuzziness": "AUTO"
                    }
                )
        search = search.query(
           query
        )
        limit = task_details_config.limit
        offset = task_details_config.offset
        total_tasks = search.count()
        task_stage_dtos_list = []
        for task_object in search[offset: offset + limit]:
            task_stage_dtos = self._get_task_stage_dtos(task_object, stage_ids)
            task_stage_dtos_list += task_stage_dtos

        return task_stage_dtos_list, total_tasks

    @staticmethod
    def _get_task_stage_dtos(task_object: Task, stage_ids: List[str]) \
            -> List[TaskStageIdsDTO]:
        return [
            TaskStageIdsDTO(
                task_id=task_object.task_id,
                task_display_id=None,
                stage_id=stage.stage_id
            )
            for stage in task_object.stages
            if stage.stage_id in stage_ids
        ]

    def validate_task_id_in_elasticsearch(self, task_id: int) -> bool:
        from ib_tasks.models import ElasticSearchTask
        return ElasticSearchTask.objects.filter(
            task_id=task_id
        ).exists()

    def _get_filter_task_objects(
            self, filter_dtos: List[ApplyFilterDTO], field_type_dtos: List[FieldTypeDTO]):

        from collections import defaultdict
        filter_operations_map = defaultdict(lambda: [])
        for filter_dto in filter_dtos:
            filter_operations_map[filter_dto.operator].append(filter_dto)

        field_types_map = {}
        for field_type_dto in field_type_dtos:
            field_types_map[field_type_dto.field_id] = field_type_dto.field_type

        query = None
        for key, value in filter_operations_map.items():
            current_queue = self._get_q_object_based_on_operation(
                operation=key, filter_dtos=value, field_types_map=field_types_map
            )
            if query is None:
                query = current_queue
            else:
                query = query & current_queue

        search = Search(index=TASK_INDEX_NAME)
        if query is None:
            task_objects = search
        else:
            task_objects = search.filter(query)
        return task_objects

    def _get_q_object_based_on_operation(
            self, operation: Operators, filter_dtos: List[ApplyFilterDTO],
            field_types_map: Dict[str, FieldTypes]):
        q_object = None
        if operation == Operators.EQ.value:
            q_object = self._prepare_q_objects_for_eq_operation(
                filter_dtos=filter_dtos, field_types_map=field_types_map
            )
        elif operation == Operators.NE.value:
            q_object = self._prepare_q_objects_for_neq_operation(
                filter_dtos=filter_dtos, field_types_map=field_types_map
            )
        elif operation == Operators.GTE.value:
            q_object = self._prepare_q_objects_for_gte_operation(
                filter_dtos=filter_dtos
            )
        elif operation == Operators.GT.value:
            q_object = self._prepare_q_objects_for_gt_operation(
                filter_dtos=filter_dtos
            )
        elif operation == Operators.LTE.value:
            q_object = self._prepare_q_objects_for_lte_operation(
                filter_dtos=filter_dtos
            )
        elif operation == Operators.LT.value:
            q_object = self._prepare_q_objects_for_lt_operation(
                filter_dtos=filter_dtos
            )
        elif operation == Operators.CONTAINS.value:
            q_object = self._prepare_q_objects_for_contains_operation(
                filter_dtos=filter_dtos
            )
        return q_object

    def _prepare_q_objects_for_eq_operation(
            self, filter_dtos: List[ApplyFilterDTO], field_types_map):
        query = None
        for counter, item in enumerate(filter_dtos):
            q_object = self._prepare_q_object_based_on_the_field_type(
                field_type=field_types_map[item.field_id],
                value=item.value, field_id=item.field_id
            )
            current_queue = Q('term', project_id__keyword=item.project_id) \
                            & Q('term', template_id__keyword=item.template_id) \
                            & q_object
            if counter == 0:
                query = current_queue
            else:
                query = query & current_queue
        return query

    def _prepare_q_objects_for_neq_operation(self, filter_dtos: List[ApplyFilterDTO], field_types_map):
        query = None
        for counter, item in enumerate(filter_dtos):
            q_object = self._prepare_q_object_based_on_the_field_type(
                field_type=field_types_map[item.field_id],
                value=item.value, field_id=item.field_id
            )
            current_queue = Q('term', project_id__keyword=item.project_id) \
                            & Q('term', template_id__keyword=item.template_id) \
                            & ~q_object
            if counter == 0:
                query = current_queue
            else:
                query = query & current_queue
        return query

    @staticmethod
    def _prepare_q_object_based_on_the_field_type(
            field_type: FieldTypes, value: Any, field_id: str):
        if field_type == FieldTypes.FLOAT.value:
            return Q('term', **{field_id: float(value)})
        elif field_type == FieldTypes.NUMBER.value:
            return Q('term', **{field_id: int(value)})
        attribute = field_id + '.keyword'
        return Q('term', **{attribute: value})

    @staticmethod
    def _prepare_q_objects_for_gte_operation(filter_dtos: List[ApplyFilterDTO]):
        query = None
        for counter, item in enumerate(filter_dtos):
            current_queue = Q('term', project_id__keyword=item.project_id) \
                            & Q('term', template_id__keyword=item.template_id) \
                            & Q('range', **{item.field_id: {"gte": int(item.value)}})
            if counter == 0:
                query = current_queue
            else:
                query = query & current_queue
        return query

    @staticmethod
    def _prepare_q_objects_for_gt_operation(filter_dtos: List[ApplyFilterDTO]):
        query = None
        for counter, item in enumerate(filter_dtos):
            current_queue = Q('term', project_id__keyword=item.project_id) \
                            & Q('term', template_id__keyword=item.template_id) \
                            & Q('range', **{item.field_id: {"gt": int(item.value)}})
            if counter == 0:
                query = current_queue
            else:
                query = query & current_queue
        return query

    @staticmethod
    def _prepare_q_objects_for_lte_operation(filter_dtos: List[ApplyFilterDTO]):
        query = None
        for counter, item in enumerate(filter_dtos):
            current_queue = Q('term', project_id__keyword=item.project_id) \
                            & Q('term', template_id__keyword=item.template_id) \
                            & Q('range', **{item.field_id: {"lte": int(item.value)}})
            if counter == 0:
                query = current_queue
            else:
                query = query & current_queue
        return query

    @staticmethod
    def _prepare_q_objects_for_lt_operation(filter_dtos: List[ApplyFilterDTO]):
        query = None
        for counter, item in enumerate(filter_dtos):
            current_queue = Q('term', project_id__keyword=item.project_id) \
                            & Q('term', template_id__keyword=item.template_id) \
                            & Q('range', **{item.field_id: {"lt": int(item.value)}})
            if counter == 0:
                query = current_queue
            else:
                query = query & current_queue
        return query

    @staticmethod
    def _prepare_q_objects_for_contains_operation(filter_dtos: List[ApplyFilterDTO]):
        query = None
        for counter, item in enumerate(filter_dtos):
            value = "*" + item.value + "*"
            current_queue = Q('term', project_id__keyword=item.project_id) \
                            & Q('term', template_id__keyword=item.template_id) \
                            & Q('wildcard', **{item.field_id: {"value": value}})
            if counter == 0:
                query = current_queue
            else:
                query = query & current_queue
        return query
