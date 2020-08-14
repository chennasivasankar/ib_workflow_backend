"""
Created on: 07/08/20
Author: Pavankumar Pamuru

"""
from typing import Tuple

from elasticsearch_dsl import Q, Search

from ib_tasks.documents.elastic_task import *
from ib_tasks.documents.elastic_task import ElasticFieldDTO, \
    Field
from ib_tasks.documents.elastic_task import ElasticTaskDTO, Task, QueryTasksDTO
from ib_tasks.interactors.storage_interfaces.elastic_storage_interface import \
    ApplyFilterDTO
from ib_tasks.interactors.storage_interfaces.elastic_storage_interface import \
    ElasticSearchStorageInterface
from ib_tasks.interactors.storage_interfaces.stage_dtos import TaskStageIdsDTO
from ib_tasks.interactors.task_dtos import TaskDetailsConfigDTO


class ElasticSearchStorageImplementation(ElasticSearchStorageInterface):

    def create_task(self, elastic_task_dto: ElasticTaskDTO) -> str:
        from elasticsearch_dsl import connections
        from django.conf import settings
        connections.create_connection(hosts=[settings.ELASTICSEARCH_ENDPOINT],
                                      timeout=20)

        task_obj = Task(
            template_id=elastic_task_dto.template_id,
            task_id=elastic_task_dto.task_id,
            title=elastic_task_dto.title
        )
        field_dtos = elastic_task_dto.fields
        stages = elastic_task_dto.stages
        task_obj.add_fields(field_dtos=field_dtos)
        task_obj.add_stages(stages)
        task_obj.save()
        elastic_task_id = task_obj.meta.id
        return elastic_task_id

    def update_task(self, task_dto: ElasticTaskDTO):
        from elasticsearch_dsl import connections
        from django.conf import settings
        connections.create_connection(hosts=[settings.ELASTICSEARCH_ENDPOINT],
                                      timeout=20)

        from ib_tasks.models import ElasticSearchTask
        task_id = task_dto.task_id
        fields = task_dto.fields
        stage_ids = task_dto.stages
        field_objects = self._get_field_objects(field_dtos=fields)
        stage_objects = self.get_stage_objects(stages_ids=stage_ids)
        elastic_search_task_id = ElasticSearchTask.objects.get(
            task_id=task_id
        ).elasticsearch_id
        from ib_tasks.documents.elastic_task import Task
        task = Task.get(id=elastic_search_task_id)
        task.template_id = task_dto.template_id
        task.title = task_dto.title
        task.fields = field_objects
        task.save()

    def filter_tasks(
            self, filter_dtos: List[ApplyFilterDTO], offset: int,
            limit: int) -> Tuple[List[int], int]:
        from elasticsearch_dsl import connections
        from django.conf import settings
        connections.create_connection(hosts=[settings.ELASTICSEARCH_ENDPOINT],
                                      timeout=20)
        task_objects = self._get_search_task_objects(filter_dtos)

        total_tasks = task_objects.count()
        return [
                   task_object.task_id
                   for task_object in task_objects[offset: offset + limit]
               ], total_tasks

    @staticmethod
    def _get_search_task_objects(filter_dtos: List[ApplyFilterDTO]):

        query = None
        for counter, item in enumerate(filter_dtos):
            current_queue = Q('term', template_id__keyword=item.template_id) \
                            & Q('term',
                                fields__field_id__keyword=item.field_id) \
                            & Q('term', fields__value__keyword=item.value)
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
            self, offset: int, limit: int, search_query: str,
            apply_filter_dtos: List[ApplyFilterDTO]
    ) -> QueryTasksDTO:
        from elasticsearch_dsl import connections
        from django.conf import settings
        connections.create_connection(hosts=[settings.ELASTICSEARCH_ENDPOINT],
                                      timeout=20)

        from elasticsearch_dsl import Q
        search = self._get_search_task_objects(apply_filter_dtos)

        if search_query:
            search = search.query(
                Q(
                    "match",
                    title={
                        "query": search_query,
                        "fuzziness": "2"
                    }
                )
            )
        total_tasks_count = search.count()
        task_ids = [
            hit.task_id
            for hit in search[offset: offset + limit]
        ]
        return QueryTasksDTO(
            total_tasks_count=total_tasks_count,
            task_ids=task_ids
        )

    @staticmethod
    def _get_field_objects(field_dtos: List[ElasticFieldDTO]) -> List[Field]:
        return [
            Field(
                field_id=field_dto.field_id,
                value=field_dto.value
            )
            for field_dto in field_dtos
        ]

    def filter_tasks_with_stage_ids(
            self, filter_dtos: List[ApplyFilterDTO],
            task_details_config: TaskDetailsConfigDTO) -> Tuple[List[TaskStageIdsDTO], int]:
        from elasticsearch_dsl import connections
        from django.conf import settings
        connections.create_connection(hosts=[settings.ELASTICSEARCH_ENDPOINT],
                                      timeout=20)
        stage_ids = task_details_config.stage_ids
        search_query = task_details_config.search_query
        search = self._get_search_task_objects(filter_dtos)
        search = search.filter('terms', stages__stage_id__keyword=stage_ids)

        if search_query:
            search = search.query(
                Q(
                    "match",
                    title={
                        "query": search_query,
                        "fuzziness": "2"
                    }
                )
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
    def _get_task_stage_dtos(task_object: Task, stage_ids: List[str]) -> List[TaskStageIdsDTO]:
        stages = task_object.stages
        stage_id = stages[0].stage_id
        return [
            TaskStageIdsDTO(
                task_id=task_object.task_id,
                stage_id=stage.stage_id
            )
            for stage in task_object.stages
            if stage.stage_id in stage_ids
        ]

    @staticmethod
    def get_stage_objects(stages_ids: List[str]) -> List[Stage]:
        return [
            Stage(stage_id=stage_id)
            for stage_id in stages_ids
        ]

    def validate_task_id_in_elasticsearch(self, task_id: int) -> bool:
        from ib_tasks.models import ElasticSearchTask
        return ElasticSearchTask.objects.filter(
            task_id=task_id
        ).exists()
