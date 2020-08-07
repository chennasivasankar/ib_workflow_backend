"""
Created on: 07/08/20
Author: Pavankumar Pamuru

"""
from typing import List

from elasticsearch_dsl import Q, Search

from ib_tasks.documents.elastic_task import ElasticTaskDTO, ElasticFieldDTO, \
    Field, QueryTasksDTO
from ib_tasks.interactors.storage_interfaces.elastic_storage_interface import \
    ApplyFilterDTO, ElasticSearchStorageInterface


class ElasticSearchStorageImplementation(ElasticSearchStorageInterface):

    def create_task(self, elastic_task_dto: ElasticTaskDTO) -> str:
        pass

    def update_task(self, task_dto: ElasticTaskDTO):
        from ib_tasks.models import ElasticSearchTask
        task_id = task_dto.task_id
        fields = task_dto.fields
        field_objects = self._get_field_objects(field_dtos=fields)
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
            self, filter_dtos: List[ApplyFilterDTO], offset: int, limit: int) -> List[int]:
        query = None
        for counter, item in enumerate(filter_dtos):
            current_queue = Q('term', template_id__keyword=item.template_id) \
                            & Q('term', fields__field_id__keyword=item.field_id) \
                            & Q('term', fields__value__keyword=item.value)
            if counter == 0:
                query = current_queue
            else:
                query = query & current_queue

        search = Search(index='task')
        task_objects = search.filter(query)
        if query is None:
            return []
        return [
            task_object.task_id
            for task_object in task_objects[offset: offset + limit]
        ]

    def query_tasks(
            self, offset: int, limit: int, search_query: str) -> QueryTasksDTO:
        pass

    @staticmethod
    def _get_field_objects(field_dtos: List[ElasticFieldDTO]) -> List[Field]:
        return [
            Field(
                field_id=field_dto.field_id,
                value=field_dto.value
            )
            for field_dto in field_dtos
        ]
