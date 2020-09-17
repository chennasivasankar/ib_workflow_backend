from typing import List

from ib_iam.adapters.dtos import UserProfileDTO
from ib_iam.exceptions.custom_exceptions import (
    InvalidNameLength, NameShouldNotContainsNumbersSpecCharacters,
    InvalidEmail, UserAccountAlreadyExistWithThisEmail, RoleIdsAreInvalid,
    RoleIdsAreDuplicated
)
from ib_iam.interactors.dtos.dtos import CompleteUserProfileDTO
from ib_iam.interactors.mixins.validation import ValidationMixin
from ib_iam.interactors.presenter_interfaces \
    .auth_presenter_interface import \
    UpdateUserProfilePresenterInterface
from ib_iam.interactors.storage_interfaces.user_storage_interface import \
    UserStorageInterface


class UpdateUserProfileInteractor(ValidationMixin):

    def __init__(self, user_storage: UserStorageInterface):
        self.user_storage = user_storage

    def update_user_profile_wrapper(
            self, user_profile_dto: CompleteUserProfileDTO,
            role_ids: List[str], presenter: UpdateUserProfilePresenterInterface
    ):
        try:
            self.update_user_profile(
                user_profile_dto=user_profile_dto, role_ids=role_ids
            )
            response = presenter.get_response_for_update_user_profile()
        except InvalidNameLength:
            response = presenter.response_for_invalid_name_length_exception()
        except NameShouldNotContainsNumbersSpecCharacters:
            response = presenter.response_for_name_contains_special_character_exception()
        except RoleIdsAreDuplicated:
            response = presenter.response_for_duplicate_role_ids_exception()
        except RoleIdsAreInvalid:
            response = presenter.response_for_invalid_role_ids_exception()
        except InvalidEmail:
            response = presenter.response_for_invalid_email_exception()
        except UserAccountAlreadyExistWithThisEmail:
            response = presenter.response_for_email_already_exists_exception()
        return response

    def update_user_profile(
            self, user_profile_dto: CompleteUserProfileDTO, role_ids: List[str]
    ):
        self._validate_name_and_throw_exception(name=user_profile_dto.name)
        is_user_admin = self.user_storage.is_user_admin(
            user_id=user_profile_dto.user_id
        )
        if is_user_admin:
            self._validate_role_ids(role_ids=role_ids)
            self._update_user_roles(
                role_ids=role_ids, user_id=user_profile_dto.user_id
            )
        self._update_user_profile_in_ib_users(
            user_profile_dto=user_profile_dto
        )
        self.user_storage.update_user_name_and_cover_page_url(
            name=user_profile_dto.name, user_id=user_profile_dto.user_id,
            cover_page_url=user_profile_dto.cover_page_url
        )

    @staticmethod
    def _update_user_profile_in_ib_users(
            user_profile_dto: CompleteUserProfileDTO
    ):
        from ib_iam.adapters.service_adapter import get_service_adapter
        service_adapter = get_service_adapter()
        user_profile_dto = UserProfileDTO(
            user_id=user_profile_dto.user_id, name=user_profile_dto.name,
            email=user_profile_dto.email,
            profile_pic_url=user_profile_dto.profile_pic_url
        )
        service_adapter.user_service.update_user_profile(
            user_id=user_profile_dto.user_id,
            user_profile_dto=user_profile_dto
        )

        return user_profile_dto

    def _update_user_roles(self, role_ids: List[str], user_id: str):
        pass

    def _validate_role_ids(self, role_ids: List[str]):
        self._validate_duplicate_role_ids(role_ids=role_ids)
        are_exists_invalid_role_ids = not self.user_storage.check_are_valid_role_ids(
            role_ids=role_ids
        )
        if are_exists_invalid_role_ids:
            raise RoleIdsAreInvalid()

    @staticmethod
    def _validate_duplicate_role_ids(role_ids: List[str]):
        is_duplicate_role_ids_exist = len(role_ids) != len(set(role_ids))
        if is_duplicate_role_ids_exist:
            raise RoleIdsAreDuplicated()
