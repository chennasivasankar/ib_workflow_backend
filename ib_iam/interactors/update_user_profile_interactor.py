from typing import List

from ib_iam.exceptions.custom_exceptions import (
    InvalidNameLength,
    NameShouldNotContainsNumbersSpecCharacters, InvalidEmail,
    UserAccountAlreadyExistWithThisEmail, RoleIdsAreInvalid)
from ib_iam.interactors.mixins.validation import ValidationMixin
from ib_iam.interactors.presenter_interfaces \
    .update_user_profile_presenter_interface import \
    UpdateUserProfilePresenterInterface
from ib_iam.interactors.storage_interfaces.dtos import \
    UserProfileDTO
from ib_iam.interactors.storage_interfaces.user_storage_interface import \
    UserStorageInterface


class UpdateUserProfileInteractor(ValidationMixin):
    def __init__(self, user_storage: UserStorageInterface):
        self.user_storage = user_storage

    def update_user_profile_wrapper(
            self,
            user_profile_dto: UserProfileDTO,
            role_ids: List[str],
            presenter: UpdateUserProfilePresenterInterface):
        try:
            self.update_user_profile(user_profile_dto=user_profile_dto,
                                     role_ids=role_ids)
            response = presenter.get_success_response_for_update_user_profile()
        except InvalidNameLength:
            response = presenter.raise_invalid_name_length_exception_for_update_user_profile()
        except NameShouldNotContainsNumbersSpecCharacters:
            response = presenter \
                .raise_name_should_not_contain_special_chars_and_numbers_exception_for_update_user_profile()
        except RoleIdsAreInvalid:
            response = presenter.raise_role_ids_are_invalid()
        except InvalidEmail:
            response = presenter.raise_invalid_email_exception_for_update_user_profile()
        except UserAccountAlreadyExistWithThisEmail:
            response = presenter.raise_email_already_in_use_exception_for_update_user_profile()
        return response

    def update_user_profile(
            self, user_profile_dto: UserProfileDTO, role_ids: List[str]):
        name = user_profile_dto.name
        user_id = user_profile_dto.user_id
        self._validate_name_and_throw_exception(name=name)
        self._validate_roles(role_ids=role_ids)
        self._update_user_profile_in_ib_users(
            user_profile_dto=user_profile_dto)
        self.user_storage.update_user_name(user_id=user_id, name=name)
        is_user_admin = self.user_storage.is_user_admin(user_id=user_id)
        if is_user_admin:
            self._update_user_roles(role_ids=role_ids, user_id=user_id)

    def _update_user_profile_in_ib_users(self,
                                         user_profile_dto: UserProfileDTO):
        from ib_iam.adapters.service_adapter import get_service_adapter
        service_adapter = get_service_adapter()
        user_profile_dto = self._create_user_profile_dto(
            user_profile_dto=user_profile_dto)
        service_adapter.user_service.update_user_profile(
            user_id=user_profile_dto.user_id,
            user_profile_dto=user_profile_dto)

    @staticmethod
    def _create_user_profile_dto(user_profile_dto: UserProfileDTO):
        from ib_iam.adapters.dtos import UserProfileDTO
        profile_pic_url = user_profile_dto.profile_pic_url
        if profile_pic_url == "":
            profile_pic_url = None
        user_profile_dto = UserProfileDTO(user_id=user_profile_dto.user_id,
                                          name=user_profile_dto.name,
                                          email=user_profile_dto.email,
                                          profile_pic_url=profile_pic_url)
        return user_profile_dto

    def _update_user_roles(self, role_ids: List[str], user_id: str):
        self.user_storage.remove_roles_for_user(user_id)
        ids_of_role_objects = self.user_storage.get_role_objs_ids(role_ids)
        self.user_storage.add_roles_to_the_user(user_id=user_id,
                                                role_ids=ids_of_role_objects)

    def _validate_roles(self, role_ids: List[str]):
        valid_role_ids = self.user_storage.get_valid_role_ids(role_ids=role_ids)
        # todo check whether duplicate ids sent or invalid role ids sent
        #  then exceptions accordingly and modify the interactors accordingly
        if are_not_valid:
            raise RoleIdsAreInvalid()
