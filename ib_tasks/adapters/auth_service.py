import dataclasses
from typing import List

from ib_tasks.adapters.dtos import UserDTO, UserDetailsDTO
from ib_tasks.interactors.field_dtos import SearchableFieldDetailDTO


class AuthService:
    @property
    def interface(self):
        from ib_iam.app_interfaces.service_interface import ServiceInterface
        return ServiceInterface()

    def get_user_dtos_based_on_limit_and_offset(self, limit: int, offset: int,
                                                search_query: str) -> \
            List[SearchableFieldDetailDTO]:
        user_dtos = self.interface.get_user_dtos_based_on_limit_and_offset(
            limit=limit, offset=offset, search_query=search_query)

        searchable_value_detail_dtos = [
            SearchableFieldDetailDTO(id=user_dto.user_id, name=user_dto.name)
            for user_dto in user_dtos
        ]
        return searchable_value_detail_dtos

    def get_all_user_dtos_based_on_query(self, search_query: str) -> \
            List[SearchableFieldDetailDTO]:
        user_dtos = self.interface.get_all_user_dtos_based_on_query(
            search_query=search_query)

        searchable_value_detail_dtos = [
            SearchableFieldDetailDTO(id=user_dto.user_id, name=user_dto.name)
            for user_dto in user_dtos
        ]
        return searchable_value_detail_dtos

    def get_permitted_user_details(self, role_ids: List[str]) \
            -> List[UserDetailsDTO]:
        user_details_dto = self.interface.get_permitted_user_details(
            role_ids=role_ids)
        return user_details_dto
