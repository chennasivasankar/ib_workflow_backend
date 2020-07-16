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
    def prepare_response_for_tokens_dto(self, tokens_dto: TokensDTO) -> \
            HttpResponse:
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

    @abstractmethod
    def get_success_response_for_reset_password_link_to_user_email(self) \
            -> HttpResponse:
        pass
