from typing import List

from ib_iam.documents.elastic_docs import ElasticCountryDTO, ElasticStateDTO, \
    ElasticCityDTO
from ib_iam.interactors.storage_interfaces.elastic_storage_interface \
    import ElasticSearchStorageInterface


class GetSearchResultsInteractor:

    def __init__(self, elastic_storage: ElasticSearchStorageInterface):
        self.elastic_storage = elastic_storage

    def search_users_results(
            self, offset: int, limit: int, search_query: str
    ) -> List[str]:
        user_ids = self.elastic_storage.search_users(
            offset=offset, limit=limit, search_query=search_query
        )
        return user_ids

    def search_countries_results(
            self, offset: int, limit: int, search_query: str
    ) -> List[ElasticCountryDTO]:
        country_dtos = self.elastic_storage.search_countries(
            offset=offset, limit=limit, search_query=search_query
        )
        return country_dtos

    def search_states_results(
            self, offset: int, limit: int, search_query: str
    ) -> List[ElasticStateDTO]:
        state_dtos = self.elastic_storage.search_states(
            offset=offset, limit=limit, search_query=search_query
        )
        return state_dtos

    def search_cities_results(
            self, offset: int, limit: int, search_query: str
    ) -> List[ElasticCityDTO]:
        city_dtos = self.elastic_storage.search_cities(
            offset=offset, limit=limit, search_query=search_query
        )
        return city_dtos
