import abc
from typing import List

from ib_iam.documents.elastic_docs import ElasticUserDTO, ElasticCountryDTO, ElasticStateDTO, ElasticCityDTO


class ElasticSearchStorageInterface(abc.ABC):

    @abc.abstractmethod
    def create_elastic_user(self, user_id: str, name: str):
        pass

    @abc.abstractmethod
    def create_elastic_user_intermediary(
            self, elastic_user_id: str, user_id: str):
        pass

    @abc.abstractmethod
    def update_elastic_user(self, user_id: str, name: str):
        pass

    @abc.abstractmethod
    def delete_elastic_user(self, user_id: str):
        pass

    @abc.abstractmethod
    def search_users(
            self, offset: int, limit: int, search_query: str
    ) -> List[str]:
        pass

    @abc.abstractmethod
    def create_elastic_country(self, country_dto: ElasticCountryDTO):
        pass

    @abc.abstractmethod
    def search_countries(
            self, offset: int, limit: int, search_query: str
    ) -> List[ElasticCountryDTO]:
        pass

    @abc.abstractmethod
    def create_elastic_state(self, state_dto: ElasticStateDTO):
        pass

    @abc.abstractmethod
    def search_states(
            self, offset: int, limit: int, search_query: str
    ) -> List[ElasticStateDTO]:
        pass

    @abc.abstractmethod
    def create_elastic_city(self, city_dto: ElasticCityDTO):
        pass

    @abc.abstractmethod
    def search_cities(
            self, offset: int, limit: int, search_query: str
    ) -> List[ElasticCityDTO]:
        pass