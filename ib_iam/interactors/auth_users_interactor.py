from typing import List

from ib_iam.interactors.dtos.dtos import AuthUserDTO
from ib_iam.interactors.storage_interfaces.user_storage_interface import \
    UserStorageInterface


class AuthUsersInteractor:

    def __init__(self, user_storage: UserStorageInterface):
        self.user_storage = user_storage

    def auth_user_dtos(self, auth_user_dtos: List[AuthUserDTO]):
        for auth_user_dto in auth_user_dtos:
            self._create_auth_user_details(auth_user_dto=auth_user_dto)

    def _create_auth_user_details(self, auth_user_dto: AuthUserDTO):
        from ib_iam.adapters.service_adapter import get_service_adapter
        service_adapter = get_service_adapter()
        user_id = service_adapter.user_service.create_user_account_with_email(
            email=auth_user_dto.email, password=auth_user_dto.email
        )
        from ib_iam.adapters.dtos import UserProfileDTO
        user_profile_dto = UserProfileDTO(
            user_id=user_id, name=auth_user_dto.name,
            email=auth_user_dto.email
        )

        service_adapter.user_service.create_user_profile(
            user_id=user_id, user_profile_dto=user_profile_dto
        )
        self.user_storage.create_user(
            user_id=user_id, name=auth_user_dto.name, is_admin=False
        )
        self.user_storage.create_auth_user(
            user_id=user_id, token=auth_user_dto.token)
        return
