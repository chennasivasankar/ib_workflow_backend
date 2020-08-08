"""
Created on: 07/08/20
Author: Pavankumar Pamuru

"""
from typing import Tuple

from elasticsearch_dsl import Q, Search

from ib_tasks.documents.elastic_task import *
from ib_tasks.interactors.storage_interfaces.elastic_storage_interface import \
    ApplyFilterDTO
from ib_tasks.interactors.storage_interfaces.elastic_storage_interface import \
    ElasticSearchStorageInterface


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
            self, filter_dtos: List[ApplyFilterDTO], offset: int, limit: int) -> Tuple[List[int], int]:
        query = None
        for counter, item in enumerate(filter_dtos):
            current_queue = Q('term', template_id__keyword=item.template_id) \
                            & Q('term', fields__field_id__keyword=item.field_id) \
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
        total_tasks = task_objects.count()
        return [
            task_object.task_id
            for task_object in task_objects[offset: offset + limit]
        ], total_tasks

    @staticmethod
    def _get_field_objects(field_dtos: List[ElasticFieldDTO]) -> List[Field]:
        return [
            Field(
                field_id=field_dto.field_id,
                value=field_dto.value
            )
            for field_dto in field_dtos
        ]

    def query_tasks(
            self, offset: int, limit: int, search_query: str
    ) -> QueryTasksDTO:
        from elasticsearch_dsl import Q, Search

        search = Search(index=TASK_INDEX_NAME)
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

    def create_elastic_user(self, user_dto: ElasticUserDTO):

        user_obj = User(user_id=user_dto.user_id, username=user_dto.username)
        user_obj.save()
        elastic_user_id = user_obj.meta.id
        return elastic_user_id

    def query_users(
            self, offset: int, limit: int, search_query: str
    ) -> List[ElasticUserDTO]:
        from elasticsearch_dsl import Q, Search

        search = Search(index=USER_INDEX_NAME)
        search = search.query(
            Q(
                "match",
                username={
                    "query": search_query,
                    "fuzziness": "2"
                }
            )
        )
        user_dtos = [
            ElasticUserDTO(
                user_id=hit.user_id,
                username=hit.username,
                elastic_user_id=None
            )
            for hit in search[offset: offset+limit]
        ]
        return user_dtos

    def create_elastic_country(self, country_dto: ElasticCountryDTO):
        country_obj = Country(
            country_id=country_dto.country_id, country_name=country_dto.country_name
        )
        country_obj.save()
        elastic_country_id = country_obj.meta.id
        return elastic_country_id

    def query_countries(
            self, offset: int, limit: int, search_query: str
    ) -> List[ElasticCountryDTO]:
        from elasticsearch_dsl import Q, Search

        search = Search(index=COUNTRY_INDEX_NAME)
        search = search.query(
            Q(
                "match",
                country_name={
                    "query": search_query,
                    "fuzziness": "2"
                }
            )
        )
        total_countries_count = search.count()
        country_dtos = [
            ElasticCountryDTO(
                country_id=hit.country_id,
                country_name=hit.country_name,
                elastic_country_id=None
            )
            for hit in search[offset: offset + limit]
        ]
        return country_dtos

    def create_elastic_state(self, state_dto: ElasticStateDTO):
        state_obj = State(
            state_id=state_dto.state_id, state_name=state_dto.state_name
        )
        state_obj.save()
        elastic_state_id = state_obj.meta.id
        return elastic_state_id

    def query_states(
            self, offset: int, limit: int, search_query: str
    ) -> List[ElasticStateDTO]:
        from elasticsearch_dsl import Q, Search

        search = Search(index=STATE_INDEX_NAME)
        search = search.query(
            Q(
                "match",
                state_name={
                    "query": search_query,
                    "fuzziness": "2"
                }
            )
        )
        total_states_count = search.count()
        state_dtos = [
            ElasticStateDTO(
                state_id=hit.state_id,
                state_name=hit.state_name,
                elastic_state_name=None
            )
            for hit in search[offset: offset + limit]
        ]
        return state_dtos

    def create_elastic_city(self, city_dto: ElasticCityDTO):
        city_obj = City(
            city_id=city_dto.city_id, city_name=city_dto.city_name
        )
        city_obj.save()
        elastic_city_id = city_obj.meta.id
        return elastic_city_id

    def query_cities(
            self, offset: int, limit: int, search_query: str
    ) -> List[ElasticCityDTO]:
        from elasticsearch_dsl import Q, Search

        search = Search(index=CITY_INDEX_NAME)
        search = search.query(
            Q(
                "match",
                city_name={
                    "query": search_query,
                    "fuzziness": "2"
                }
            )
        )
        total_cities_count = search.count()
        city_dtos = [
            ElasticCityDTO(
                city_id=hit.city_id,
                city_name=hit.city_name,
                elastic_city_name=None
            )
            for hit in search[offset: offset + limit]
        ]
        return city_dtos
