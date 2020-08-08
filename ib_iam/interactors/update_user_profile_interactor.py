from ib_iam.exceptions.custom_exceptions import (
    NameMinimumLengthShouldBe,
    NameShouldNotContainsNumbersSpecCharacters, InvalidEmail,
    UserAccountAlreadyExistWithThisEmail)
from ib_iam.interactors.mixins.validation import ValidationMixin
from ib_iam.interactors.presenter_interfaces \
    .update_user_profile_presenter_interface import \
    UpdateUserProfilePresenterInterface
from ib_iam.interactors.storage_interfaces.dtos import \
    UserIdNameEmailAndProfilePicUrlDTO
from ib_iam.interactors.storage_interfaces.user_storage_interface import \
    UserStorageInterface


class UpdateUserProfileInteractor(ValidationMixin):
    def __init__(self, user_storage: UserStorageInterface):
        self.user_storage = user_storage

    def update_user_profile_wrapper(
            self,
            user_id_name_email_and_profile_pic_url_dto:
            UserIdNameEmailAndProfilePicUrlDTO,
            presenter: UpdateUserProfilePresenterInterface):
        try:
            self.update_user_profile(
                user_id_name_email_and_profile_pic_url_dto=
                user_id_name_email_and_profile_pic_url_dto)
            response = presenter.get_success_response_for_update_user_profile()
        except NameMinimumLengthShouldBe:
            response = presenter.get_response_for_minimum_name_length()
        except NameShouldNotContainsNumbersSpecCharacters:
            response = presenter \
                .get_response_for_name_contains_special_chars_and_numbers_exception()
        except InvalidEmail:
            response = presenter.get_response_for_invalid_email_exception()
        except UserAccountAlreadyExistWithThisEmail:
            response = presenter.get_response_for_email_already_exists()
        return response

    def update_user_profile(self,
                            user_id_name_email_and_profile_pic_url_dto:
                            UserIdNameEmailAndProfilePicUrlDTO):
        name = user_id_name_email_and_profile_pic_url_dto.name
        user_id = user_id_name_email_and_profile_pic_url_dto.user_id
        self._validate_name_and_throw_exception(name=name)
        self._update_user_profile_in_ib_users(
            user_id_name_email_and_profile_pic_url_dto=
            user_id_name_email_and_profile_pic_url_dto)
        self.user_storage.update_user_name(user_id=user_id, name=name)

    def _update_user_profile_in_ib_users(
            self,
            user_id_name_email_and_profile_pic_url_dto:
            UserIdNameEmailAndProfilePicUrlDTO):
        from ib_iam.adapters.service_adapter import get_service_adapter
        service_adapter = get_service_adapter()
        user_profile_dto = self._create_user_profile_dto(
            user_id_name_email_and_profile_pic_url_dto=
            user_id_name_email_and_profile_pic_url_dto)
        service_adapter.user_service.update_user_profile(
            user_id=user_id_name_email_and_profile_pic_url_dto.user_id,
            user_profile_dto=user_profile_dto)

    @staticmethod
    def _create_user_profile_dto(
            user_id_name_email_and_profile_pic_url_dto:
            UserIdNameEmailAndProfilePicUrlDTO):
        from ib_iam.adapters.dtos import UserProfileDTO
        profile_pic_url = \
            user_id_name_email_and_profile_pic_url_dto.profile_pic_url
        if profile_pic_url == "":
            profile_pic_url = None
        user_profile_dto = UserProfileDTO(
            user_id=user_id_name_email_and_profile_pic_url_dto.user_id,
            name=user_id_name_email_and_profile_pic_url_dto.name,
            email=user_id_name_email_and_profile_pic_url_dto.email,
            profile_pic_url=profile_pic_url
        )
        return user_profile_dto
