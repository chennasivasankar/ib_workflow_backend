"""
Created on: 07/08/20
Author: Pavankumar Pamuru

"""

from ib_tasks.documents.elastic_task import ElasticTaskDTO, Task, QueryTasksDTO
from ib_tasks.interactors.storage_interfaces.elastic_storage_interface import ElasticSearchStorageInterface


class ElasticSearchStorageImplementation(ElasticSearchStorageInterface):

    def create_task(self, elastic_task_dto: ElasticTaskDTO) -> str:

        task_obj = Task(
            template_id=elastic_task_dto.template_id,
            task_id=elastic_task_dto.task_id,
            title=elastic_task_dto.title
        )
        field_dtos = elastic_task_dto.fields
        task_obj.add_fields(field_dtos=field_dtos)
        task_obj.save()
        elastic_task_id = task_obj.meta.id
        return elastic_task_id

    def update_task(self, task_dto: ElasticTaskDTO):
        pass

    def filter_tasks(self):
        pass

    def query_tasks(
            self, offset: int, limit: int, search_query: str
    ) -> QueryTasksDTO:
        from elasticsearch_dsl import Q, Search

        search = Search(index='task')
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
            for hit in search[offset: offset+limit]
        ]
        return QueryTasksDTO(
            total_tasks_count=total_tasks_count,
            task_ids=task_ids
        )
