from typing import List, Optional

from ib_tasks.adapters.dtos import SearchableDetailsDTO
from ib_tasks.interactors.task_dtos import SearchableDTO


class InvalidUserIdsException(Exception):
    def __init__(self, user_ids: List[str]):
        self.user_ids = user_ids


class InvalidStateIdsException(Exception):
    def __init__(self, state_ids: List[int]):
        self.state_ids = state_ids


class InvalidCountryIdsException(Exception):
    def __init__(self, country_ids: List[int]):
        self.country_ids = country_ids


class InvalidCityIdsException(Exception):
    def __init__(self, city_ids: List[int]):
        self.city_ids = city_ids


class SearchableDetailsService:

    @property
    def interface(self):
        from ib_iam.app_interfaces.service_interface import ServiceInterface
        return ServiceInterface()

    def get_searchable_details_dtos(
            self, searchable_dtos: List[SearchableDTO]
    ) -> Optional[List[SearchableDetailsDTO]]:
        from ib_iam.exceptions.custom_exceptions import (
            InvalidCityIds, InvalidStateIds, InvalidCountryIds, InvalidUserIds
        )
        try:
            return self._get_searchable_details_dtos(searchable_dtos)
        except InvalidCityIds as err:
            raise InvalidCityIdsException(err.city_ids)
        except InvalidStateIds as err:
            raise InvalidStateIdsException(err.state_ids)
        except InvalidCountryIds as err:
            raise InvalidCountryIdsException(err.country_ids)
        except InvalidUserIds as err:
            raise InvalidUserIdsException(err.user_ids)

    def _get_searchable_details_dtos(
            self,
            searchable_dtos: List[SearchableDTO]
    ) -> List[SearchableDetailsDTO]:
        searchable_dtos = self.interface.get_searchable_details_dtos(
            searchable_dtos
        )
        searchable_details_dtos = [
            SearchableDetailsDTO(
                search_type=searchable_dto.search_type,
                id=searchable_dto.id,
                value=searchable_dto.value
            )
            for searchable_dto in searchable_dtos
        ]
        return searchable_details_dtos


