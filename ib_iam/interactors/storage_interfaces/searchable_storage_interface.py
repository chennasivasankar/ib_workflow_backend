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
