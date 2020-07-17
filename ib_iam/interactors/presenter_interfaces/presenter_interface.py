from abc import abstractmethod, ABC

from django.http import HttpResponse

from ib_iam.adapters.auth_service import TokensDTO


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

    def prepare_response_for_tokens_dto(
            self, tokens_dto: TokensDTO, is_admin: bool
    ):
        pass

    @abstractmethod
    def get_success_response_for_reset_password_link_to_user_email(self):
        pass

    @abstractmethod
    def raise_exception_for_token_does_not_exists(self):
        pass

    @abstractmethod
    def raise_exception_for_not_a_strong_password(self):
        pass

    @abstractmethod
    def raise_exception_for_token_has_expired(self):
        pass

    @abstractmethod
    def get_update_user_password_success_response(self):
        pass
