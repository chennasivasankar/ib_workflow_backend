from typing import List

from ib_iam.adapters.dtos import UserProfileDTO
from ib_iam.adapters.service_adapter import get_service_adapter
from ib_iam.app_interfaces.dtos import SearchableDTO
from ib_iam.constants.enums import Searchable
from ib_iam.exceptions.custom_exceptions import InvalidStateIds, \
    InvalidCountryIds, InvalidUserIds
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
        valid_user_ids = self._get_valid_user_ids(ids)
        self._validate_user_ids(ids, valid_user_ids)
        user_details_dtos = self._get_user_details_dtos(ids)
        searchable_type_user_details_dtos = []
        for user_details_dto in user_details_dtos:
            searchable_type_user_details_dto = \
                self._get_searchable_type_user_details_dto(
                    user_details_dto
                )
            searchable_type_user_details_dtos.append(
                searchable_type_user_details_dto
            )
        return searchable_type_user_details_dtos

    def _get_valid_user_ids(self, ids: List[str]):
        valid_user_ids = self.storage.get_valid_user_ids(ids)
        return valid_user_ids

    @staticmethod
    def _validate_user_ids(ids: List[str], valid_user_ids: List[str]):
        invalid_user_ids = []
        for id in ids:
            if id not in valid_user_ids:
                invalid_user_ids.append(id)
        if invalid_user_ids:
            raise InvalidUserIds(invalid_user_ids)

    @staticmethod
    def _get_user_details_dtos(ids: List[str]) -> List[UserProfileDTO]:
        service_adapter = get_service_adapter()
        user_service = service_adapter.user_service
        user_details_dtos = user_service.get_basic_user_dtos(user_ids=ids)
        return user_details_dtos

    @staticmethod
    def _get_searchable_type_user_details_dto(
            user_details_dto: UserProfileDTO
    ) -> SearchableDetailsDTO:
        import json
        name = user_details_dto.name
        profile_pic_url = user_details_dto.profile_pic_url
        value = {
            "name": name,
            "profile_pic_url": profile_pic_url
        }
        value = json.dumps(value)
        searchable_type_user_details_dto = SearchableDetailsDTO(
            search_type=Searchable.USER.value,
            id=user_details_dto.user_id,
            value=value
        )
        return searchable_type_user_details_dto

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
        self._validate_country_ids(ids, searchable_type_country_details_dtos)
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
        self._validate_state_ids(ids, searchable_type_state_details_dtos)
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
        self._validate_city_ids(ids, searchable_type_city_details_dtos)
        return searchable_type_city_details_dtos

    @staticmethod
    def _validate_city_ids(
            ids: List[int],
            searchable_type_city_details_dtos: List[SearchableDetailsDTO]
    ):
        actual_ids = [
            searchable_type_city_details_dto.id
            for searchable_type_city_details_dto in
            searchable_type_city_details_dtos
        ]
        invalid_ids = []
        for id in ids:
            if id not in actual_ids:
                invalid_ids.append(id)
        if invalid_ids:
            from ib_iam.exceptions.custom_exceptions import InvalidCityIds
            raise InvalidCityIds(invalid_ids)

    @staticmethod
    def _validate_state_ids(
            ids: List[int],
            searchable_type_state_details_dtos: List[SearchableDetailsDTO]
    ):
        actual_ids = [
            searchable_type_state_details_dto.id
            for searchable_type_state_details_dto in
            searchable_type_state_details_dtos
        ]
        invalid_ids = []
        for id in ids:
            if id not in actual_ids:
                invalid_ids.append(id)
        if invalid_ids:
            raise InvalidStateIds(invalid_ids)

    @staticmethod
    def _validate_country_ids(
            ids: List[int],
            searchable_type_country_details_dtos: List[SearchableDetailsDTO]
    ):
        actual_ids = [
            searchable_type_country_details_dto.id
            for searchable_type_country_details_dto in
            searchable_type_country_details_dtos
        ]
        invalid_ids = []
        for id in ids:
            if id not in actual_ids:
                invalid_ids.append(id)
        if invalid_ids:
            raise InvalidCountryIds(invalid_ids)
