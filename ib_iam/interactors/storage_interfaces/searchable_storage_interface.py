import abc
from typing import List

from ib_iam.interactors.storage_interfaces.dtos import SearchableDetailsDTO


class SearchableStorageInterface(abc.ABC):

    @abc.abstractmethod
    def get_searchable_type_city_details_dtos(
            self, ids: List[int]
    ) -> List[SearchableDetailsDTO]:
        pass

    @abc.abstractmethod
    def get_searchable_type_state_details_dtos(
            self, ids: List[int]
    ) -> List[SearchableDetailsDTO]:
        pass

    @abc.abstractmethod
    def get_searchable_type_country_details_dtos(
            self, ids: List[int]
    ) -> List[SearchableDetailsDTO]:
        pass

    @abc.abstractmethod
    def get_valid_user_ids(self, ids: List[str]) -> List[str]:
        pass

    @abc.abstractmethod
    def get_valid_city_ids(self, city_ids: List[int]) -> List[int]:
        pass

    @abc.abstractmethod
    def get_valid_state_ids(self, state_ids: List[int]) -> List[int]:
        pass

    @abc.abstractmethod
    def get_valid_country_ids(self, country_ids: List[int]) -> List[int]:
        pass
