from typing import List

from ib_iam.documents.elastic_docs import *
from ib_iam.interactors.storage_interfaces.elastic_storage_interface \
    import ElasticSearchStorageInterface
from ib_iam.models import ElasticUserIntermediary


class ElasticStorageImplementation(ElasticSearchStorageInterface):

    def create_elastic_user_intermediary(
            self, elastic_user_id: str, user_id: str):

        ElasticUserIntermediary.objects.create(
            user_id=user_id, elastic_user_id=elastic_user_id
        )

    def create_elastic_user(self, user_id: str, name: str, email: str) -> str:
        from elasticsearch_dsl import connections
        from django.conf import settings
        connections.create_connection(hosts=[settings.ELASTICSEARCH_ENDPOINT],
                                      timeout=20)
        elastic_user_obj = ElasticUser(
            user_id=str(user_id), name=name, email=email
        )
        elastic_user_obj.save()
        elastic_user_id = elastic_user_obj.meta.id
        return elastic_user_id

    def update_elastic_user(self, user_id: str, name: str):
        from elasticsearch_dsl import connections
        from django.conf import settings
        connections.create_connection(hosts=[settings.ELASTICSEARCH_ENDPOINT],
                                      timeout=20)
        elastic_user_intermediary = \
            ElasticUserIntermediary.objects.get(user_id=user_id)
        elastic_user_id = elastic_user_intermediary.elastic_user_id
        elastic_user_obj = ElasticUser.get(id=elastic_user_id)
        elastic_user_obj.name = name
        elastic_user_obj.save()

    def delete_elastic_user(self, user_id: str):
        from elasticsearch_dsl import connections
        from django.conf import settings
        connections.create_connection(hosts=[settings.ELASTICSEARCH_ENDPOINT],
                                      timeout=20)
        elastic_user_intermediary = \
            ElasticUserIntermediary.objects.get(user_id=user_id)
        elastic_user_id = elastic_user_intermediary.elastic_user_id
        elastic_user_obj = ElasticUser.get(id=elastic_user_id)
        elastic_user_obj.delete()
        elastic_user_intermediary.delete()

    def search_users(
            self, offset: int, limit: int, search_query: str
    ) -> List[str]:
        from elasticsearch_dsl import connections
        from django.conf import settings
        connections.create_connection(
            hosts=[settings.ELASTICSEARCH_ENDPOINT], timeout=20
        )
        from elasticsearch_dsl import Q, Search

        search = Search(index=USER_INDEX_NAME)
        if search_query:
            search = search.query(
                Q(
                    "multi_match", query=search_query, type='bool_prefix',
                    fields=[
                        "name",
                        "name._2gram",
                        "name._3gram",
                        "name._index_prefix"
                    ]
                )
            )
        user_ids = [
            hit.user_id
            for hit in search[offset: offset + limit]
        ]
        return user_ids

    def create_elastic_country(self, country_dto: ElasticCountryDTO):
        from elasticsearch_dsl import connections
        from django.conf import settings
        connections.create_connection(hosts=[settings.ELASTICSEARCH_ENDPOINT],
                                      timeout=20)
        country_obj = Country(
            country_id=country_dto.country_id,
            country_name=country_dto.country_name
        )
        country_obj.save()
        elastic_country_id = country_obj.meta.id
        return elastic_country_id

    def search_countries(
            self, offset: int, limit: int, search_query: str
    ) -> List[ElasticCountryDTO]:
        from elasticsearch_dsl import connections
        from django.conf import settings
        connections.create_connection(hosts=[settings.ELASTICSEARCH_ENDPOINT],
                                      timeout=20)
        from elasticsearch_dsl import Q, Search

        search = Search(index=COUNTRY_INDEX_NAME)
        if search_query:
            search = search.query(
                Q(
                    "multi_match", query=search_query, type='bool_prefix',
                    fields=[
                        "country_name",
                        "country_name._2gram",
                        "country_name._3gram",
                        "country_name._index_prefix"
                    ]
                )
            )
        country_dtos = [
            ElasticCountryDTO(
                country_id=hit.country_id,
                country_name=hit.country_name
            )
            for hit in search[offset: offset + limit]
        ]
        return country_dtos

    def create_elastic_state(self, state_dto: ElasticStateDTO):
        from elasticsearch_dsl import connections
        from django.conf import settings
        connections.create_connection(hosts=[settings.ELASTICSEARCH_ENDPOINT],
                                      timeout=20)
        state_obj = State(
            state_id=state_dto.state_id, state_name=state_dto.state_name
        )
        state_obj.save()
        elastic_state_id = state_obj.meta.id
        return elastic_state_id

    def search_states(
            self, offset: int, limit: int, search_query: str
    ) -> List[ElasticStateDTO]:
        from elasticsearch_dsl import connections
        from django.conf import settings
        connections.create_connection(hosts=[settings.ELASTICSEARCH_ENDPOINT],
                                      timeout=20)
        from elasticsearch_dsl import Q, Search

        search = Search(index=STATE_INDEX_NAME)
        if search_query:
            search = search.query(
                Q(
                    "multi_match", query=search_query, type='bool_prefix',
                    fields=[
                        "state_name",
                        "state_name._2gram",
                        "state_name._3gram",
                        "state_name._index_prefix"
                    ]
                )
            )
        state_dtos = [
            ElasticStateDTO(
                state_id=hit.state_id,
                state_name=hit.state_name
            )
            for hit in search[offset: offset + limit]
        ]
        return state_dtos

    def create_elastic_city(self, city_dto: ElasticCityDTO):
        from elasticsearch_dsl import connections
        from django.conf import settings
        connections.create_connection(hosts=[settings.ELASTICSEARCH_ENDPOINT],
                                      timeout=20)
        city_obj = City(
            city_id=city_dto.city_id, city_name=city_dto.city_name
        )
        city_obj.save()
        elastic_city_id = city_obj.meta.id
        return elastic_city_id

    def search_cities(
            self, offset: int, limit: int, search_query: str
    ) -> List[ElasticCityDTO]:
        from elasticsearch_dsl import connections
        from django.conf import settings
        connections.create_connection(
            hosts=[settings.ELASTICSEARCH_ENDPOINT],
            timeout=20
        )
        from elasticsearch_dsl import Q, Search

        search = Search(index=CITY_INDEX_NAME)
        if search_query:
            search = search.query(
                Q(
                    "multi_match", query=search_query, type='bool_prefix',
                    fields=[
                        "city_name",
                        "city_name._2gram",
                        "city_name._3gram",
                        "city_name._index_prefix"
                    ]
                )
            )
        city_dtos = [
            ElasticCityDTO(
                city_id=hit.city_id,
                city_name=hit.city_name
            )
            for hit in search[offset: offset + limit]
        ]
        return city_dtos
