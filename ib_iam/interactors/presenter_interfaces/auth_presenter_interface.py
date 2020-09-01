import dataclasses
from abc import abstractmethod, ABC
from typing import List, Optional

from django.http import HttpResponse

from ib_iam.adapters.auth_service import UserTokensDTO
from ib_iam.adapters.dtos import UserProfileDTO
from ib_iam.interactors.dtos.dtos import CompleteUserProfileDTO
from ib_iam.interactors.storage_interfaces.dtos import (
    CompanyDTO, TeamDTO, TeamUserIdsDTO, CompanyIdWithEmployeeIdsDTO,
    UserRoleDTO)


@dataclasses.dataclass
class UserWithExtraDetailsDTO:
    user_profile_dto: CompleteUserProfileDTO
    company_dto: Optional[CompanyDTO]
    team_dtos: List[TeamDTO]
    team_user_ids_dto: List[TeamUserIdsDTO]
    company_id_with_employee_ids_dto: Optional[CompanyIdWithEmployeeIdsDTO]
    user_dtos: List[UserProfileDTO]
    role_dtos: List[UserRoleDTO]


class AuthPresenterInterface(ABC):

    @abstractmethod
    def raise_exception_for_invalid_email(self) -> HttpResponse:
        pass

    @abstractmethod
    def raise_exception_for_incorrect_password(self) -> HttpResponse:
        pass

    @abstractmethod
    def raise_exception_for_user_account_does_not_exists(self) -> HttpResponse:
        pass

    @abstractmethod
    def raise_exception_for_password_min_length_required(self) -> HttpResponse:
        pass

    @abstractmethod
    def raise_exception_for_password_at_least_one_special_character_required(
            self
    ) -> HttpResponse:
        pass

    def prepare_response_for_user_tokens_dto_and_is_admin(
            self, tokens_dto: UserTokensDTO, is_admin: bool
    ):
        pass

    @abstractmethod
    def get_success_response_for_reset_password_link_to_user_email(self) \
            -> HttpResponse:
        pass

    @abstractmethod
    def raise_exception_for_token_does_not_exists(self):
        pass

    @abstractmethod
    def raise_exception_for_token_has_expired(self):
        pass

    @abstractmethod
    def get_update_user_password_success_response(self):
        pass

    @abstractmethod
    def raise_exception_for_login_with_not_verify_email(self):
        pass


class GetUserProfilePresenterInterface(ABC):
    @abstractmethod
    def raise_exception_for_invalid_user_id(self):
        pass

    @abstractmethod
    def raise_exception_for_user_account_does_not_exist(self):
        pass

    @abstractmethod
    def prepare_response_for_get_user_profile(
            self,
            user_with_extra_details_dto: UserWithExtraDetailsDTO):
        pass


class CreateUserAccountPresenterInterface(ABC):
    @abstractmethod
    def raise_account_already_exists_exception(self):
        pass

    @abstractmethod
    def raise_password_not_matched_with_criteria_exception(self):
        pass

    @abstractmethod
    def raise_invalid_email_exception(self):
        pass

    @abstractmethod
    def raise_invalid_domain_exception(self):
        pass

    @abstractmethod
    def get_response_for_create_user_account(self):
        pass

    @abstractmethod
    def raise_invalid_name_length_exception(self):
        pass

    @abstractmethod
    def raise_name_should_not_contain_special_characters_exception(self):
        pass


class SendVerifyEmailLinkPresenterInterface(ABC):
    @abstractmethod
    def raise_account_does_not_exist_exception(self):
        pass

    @abstractmethod
    def raise_email_already_verified_exception(self):
        pass

    @abstractmethod
    def get_response_send_verify_email_link(self):
        pass


class VerifyEmailPresenterInterface(ABC):
    @abstractmethod
    def raise_email_does_not_exist_to_verify_exception(self):
        pass

    @abstractmethod
    def raise_email_already_verified_exception(self):
        pass

    @abstractmethod
    def get_response_for_verified_email(self):
        pass
