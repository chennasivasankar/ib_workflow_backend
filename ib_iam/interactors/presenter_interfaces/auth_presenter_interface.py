import dataclasses
import abc
from typing import List, Optional

from django.http import HttpResponse

from ib_iam.adapters.dtos import UserTokensDTO
from ib_iam.adapters.dtos import UserProfileDTO
from ib_iam.interactors.dtos.dtos import CompleteUserProfileDTO
from ib_iam.interactors.presenter_interfaces.dtos import \
    UserWithExtraDetailsDTO
from ib_iam.interactors.storage_interfaces.dtos import (
    CompanyDTO, TeamDTO, TeamUserIdsDTO, CompanyIdWithEmployeeIdsDTO,
    UserRoleDTO
)


class AuthPresenterInterface(abc.ABC):

    @abc.abstractmethod
    def raise_exception_for_invalid_email(self) -> HttpResponse:
        pass

    @abc.abstractmethod
    def raise_exception_for_incorrect_password(self) -> HttpResponse:
        pass

    @abc.abstractmethod
    def raise_exception_for_user_account_does_not_exists(self) -> HttpResponse:
        pass

    @abc.abstractmethod
    def raise_exception_for_password_min_length_required(self) -> HttpResponse:
        pass

    @abc.abstractmethod
    def raise_exception_for_password_at_least_one_special_character_required(
            self
    ) -> HttpResponse:
        pass

    def prepare_response_for_user_tokens_dto_and_is_admin(
            self, tokens_dto: UserTokensDTO, is_admin: bool
    ):
        pass

    @abc.abstractmethod
    def get_success_response_for_reset_password_link_to_user_email(self) \
            -> HttpResponse:
        pass

    @abc.abstractmethod
    def raise_exception_for_token_does_not_exists(self):
        pass

    @abc.abstractmethod
    def raise_exception_for_token_has_expired(self):
        pass

    @abc.abstractmethod
    def response_for_update_user_password(self):
        pass

    @abc.abstractmethod
    def raise_exception_for_login_with_not_verify_email(self):
        pass


class GetUserProfilePresenterInterface(abc.ABC):
    @abc.abstractmethod
    def response_for_invalid_user_id_exception(self):
        pass

    @abc.abstractmethod
    def response_for_user_account_does_not_exist_exception(self):
        pass

    @abc.abstractmethod
    def response_for_get_user_profile(
            self, user_with_extra_details_dto: UserWithExtraDetailsDTO
    ):
        pass


class CreateUserAccountPresenterInterface(abc.ABC):
    @abc.abstractmethod
    def raise_account_already_exists_exception(self):
        pass

    @abc.abstractmethod
    def raise_password_not_matched_with_criteria_exception(self):
        pass

    @abc.abstractmethod
    def response_for_invalid_email_exception(self):
        pass

    @abc.abstractmethod
    def raise_invalid_domain_exception(self):
        pass

    @abc.abstractmethod
    def get_response_for_create_user_account(self):
        pass

    @abc.abstractmethod
    def response_for_invalid_name_length_exception(self):
        pass

    @abc.abstractmethod
    def response_for_name_contains_special_character_exception(self):
        pass


class SendVerifyEmailLinkPresenterInterface(abc.ABC):
    @abc.abstractmethod
    def response_for_account_does_not_exist_exception(self):
        pass

    @abc.abstractmethod
    def response_for_email_already_verified_exception(self):
        pass

    @abc.abstractmethod
    def get_response_send_verify_email_link(self):
        pass


class VerifyEmailPresenterInterface(abc.ABC):
    @abc.abstractmethod
    def response_for_email_does_not_exist_exception(self):
        pass

    @abc.abstractmethod
    def response_for_email_already_verified_exception(self):
        pass

    @abc.abstractmethod
    def get_response_for_verified_email(self):
        pass


class GetRefreshTokensPresenterInterface(abc.ABC):

    @abc.abstractmethod
    def response_for_access_token_not_found(self):
        pass

    @abc.abstractmethod
    def response_for_refresh_token_expired(self):
        pass

    @abc.abstractmethod
    def response_for_refresh_token_not_found(self):
        pass

    @abc.abstractmethod
    def response_for_user_account_not_found(self):
        pass

    @abc.abstractmethod
    def response_for_user_tokens_dto(self, user_tokens_dto: UserTokensDTO):
        pass


class UpdateUserProfilePresenterInterface(abc.ABC):

    @abc.abstractmethod
    def get_response_for_update_user_profile(self):
        pass

    @abc.abstractmethod
    def response_for_invalid_name_length_exception(self):
        pass

    @abc.abstractmethod
    def response_for_duplicate_role_ids_exception(self):
        pass

    @abc.abstractmethod
    def response_for_invalid_role_ids_exception(self):
        pass

    @abc.abstractmethod
    def response_for_name_contains_special_character_exception(
            self):
        pass

    @abc.abstractmethod
    def response_for_invalid_email_exception(self):
        pass

    @abc.abstractmethod
    def response_for_email_already_exists_exception(self):
        pass


class UpdateUserPasswordPresenterInterface(abc.ABC):

    @abc.abstractmethod
    def get_success_response_for_update_user_password(self):
        pass

    @abc.abstractmethod
    def response_for_invalid_new_password_exception(self):
        pass

    @abc.abstractmethod
    def response_for_invalid_current_password_exception(self):
        pass

    @abc.abstractmethod
    def response_for_current_password_mismatch_exception(self):
        pass
