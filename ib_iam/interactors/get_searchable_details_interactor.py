from typing import List

from ib_iam.app_interfaces.dtos import SearchableDTO
from ib_iam.constants.enums import Searchable
from ib_iam.interactors.storage_interfaces.dtos import SearchableDetailsDTO
from ib_iam.interactors.storage_interfaces.searchable_storage_interface \
    import \
    SearchableStorageInterface


class GetSearchableDetailsInteractor:
    def __init__(self, storage: SearchableStorageInterface):
        self.storage = storage

    def get_searchable_details_dtos(
            self, searchable_dtos: List[SearchableDTO]
    ) -> List[SearchableDetailsDTO]:
        searchable_type_city_details_dtos = \
            self._get_searchable_type_city_details_dtos(
                searchable_dtos)
        searchable_type_state_details_dtos = \
            self._get_searchable_type_state_details_dtos(
                searchable_dtos)
        searchable_type_country_details_dtos = \
            self._get_searchable_type_country_details_dtos(
                searchable_dtos)
        searchable_type_user_details_dtos = \
            self._get_searchable_type_user_details_dtos(
                searchable_dtos)
        searchable_details_dtos = (
                searchable_type_city_details_dtos +
                searchable_type_state_details_dtos +
                searchable_type_country_details_dtos +
                searchable_type_user_details_dtos
        )
        return searchable_details_dtos

    def _get_searchable_type_user_details_dtos(
            self, searchable_dtos: List[SearchableDTO]
    ) -> List[SearchableDetailsDTO]:
        searchable_type_user_dtos = [
            searchable_dto
            for searchable_dto in searchable_dtos
            if searchable_dto.search_type == Searchable.USER.value
        ]
        is_searchable_type_user_dtos_empty = not searchable_type_user_dtos
        if is_searchable_type_user_dtos_empty:
            return []

        ids = [
            searchable_type_user_dto.id
            for searchable_type_user_dto in searchable_type_user_dtos
        ]
        searchable_type_user_details_dtos = \
            self.storage.get_searchable_type_user_details_dtos(
                ids)
        return searchable_type_user_details_dtos

    def _get_searchable_type_country_details_dtos(
            self, searchable_dtos: List[SearchableDTO]
    ) -> List[SearchableDetailsDTO]:
        searchable_type_country_dtos = [
            searchable_dto
            for searchable_dto in searchable_dtos
            if searchable_dto.search_type == Searchable.COUNTRY.value
        ]
        is_searchable_type_country_dtos_empty = not \
            searchable_type_country_dtos
        if is_searchable_type_country_dtos_empty:
            return []

        ids = [
            searchable_type_country_dto.id
            for searchable_type_country_dto in searchable_type_country_dtos
        ]
        searchable_type_country_details_dtos = \
            self.storage.get_searchable_type_country_details_dtos(
                ids)
        return searchable_type_country_details_dtos

    def _get_searchable_type_state_details_dtos(
            self, searchable_dtos: List[SearchableDTO]
    ) -> List[SearchableDetailsDTO]:
        searchable_type_state_dtos = [
            searchable_dto
            for searchable_dto in searchable_dtos
            if searchable_dto.search_type == Searchable.STATE.value
        ]
        is_searchable_type_state_dtos_empty = not searchable_type_state_dtos
        if is_searchable_type_state_dtos_empty:
            return []

        ids = [
            searchable_type_state_dto.id
            for searchable_type_state_dto in searchable_type_state_dtos
        ]
        searchable_type_state_details_dtos = \
            self.storage.get_searchable_type_state_details_dtos(
                ids)
        return searchable_type_state_details_dtos

    def _get_searchable_type_city_details_dtos(
            self, searchable_dtos: List[SearchableDTO]
    ) -> List[SearchableDetailsDTO]:
        searchable_type_city_dtos = [
            searchable_dto
            for searchable_dto in searchable_dtos
            if searchable_dto.search_type == Searchable.CITY.value
        ]
        is_searchable_type_city_dtos_empty = not searchable_type_city_dtos
        if is_searchable_type_city_dtos_empty:
            return []

        ids = [
            searchable_type_city_dto.id
            for searchable_type_city_dto in searchable_type_city_dtos
        ]
        searchable_type_city_details_dtos = \
            self.storage.get_searchable_type_city_details_dtos(
                ids)
        return searchable_type_city_details_dtos
