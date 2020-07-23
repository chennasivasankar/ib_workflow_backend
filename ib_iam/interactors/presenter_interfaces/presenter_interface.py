from abc import abstractmethod, ABC

from ib_iam.interactors.presenter_interfaces.dtos \
    import CompleteUsersDetailsDTO


class PresenterInterface(ABC):

    @abstractmethod
    def raise_user_is_not_admin_exception(self):
        pass

    @abstractmethod
    def get_user_options_details_response(self, configuration_details):
        pass

    # ADD USER
    @abstractmethod
    def user_created_response(self):
        pass

    @abstractmethod
    def raise_invalid_name_exception(cls):
        pass

    @abstractmethod
    def raise_invalid_email_exception(cls):
        pass

    @abstractmethod
    def raise_user_account_already_exist_with_this_email_exception(cls):
        pass

    @abstractmethod
    def raise_role_ids_are_invalid(self):
        pass

    @abstractmethod
    def raise_company_ids_is_invalid(self):
        pass

    @abstractmethod
    def raise_team_ids_are_invalid(self):
        pass

    @abstractmethod
    def raise_name_should_not_contain_special_characters_exception(self):
        pass

    # GET USERS
    @abstractmethod
    def raise_invalid_offset_value_exception(self):
        pass

    @abstractmethod
    def raise_invalid_limit_value_exception(self):
        pass

    @abstractmethod
    def raise_offset_value_is_greater_than_limit_value_exception(self):
        pass

    @abstractmethod
    def response_for_get_users(
            self, complete_user_details_dtos: CompleteUsersDetailsDTO):
        pass

    # ADD ROLES

    @abstractmethod
    def raise_role_name_should_not_be_empty_exception(self):
        pass

    @abstractmethod
    def raise_role_description_should_not_be_empty_exception(self):
        pass

    @abstractmethod
    def raise_role_id_format_is_invalid_exception(self):
        pass

    @abstractmethod
    def raise_duplicate_role_ids_exception(self):
        pass


from abc import abstractmethod, ABC

from django.http import HttpResponse

from ib_iam.adapters.auth_service import UserTokensDTO


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
