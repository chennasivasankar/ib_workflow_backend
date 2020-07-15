from abc import abstractmethod, ABC

from ib_iam.adapters.auth_service import TokensDTO


class AuthPresenterInterface(ABC):

    @abstractmethod
    def raise_invalid_email(self):
        pass

    @abstractmethod
    def raise_invalid_password(self):
        pass

    @abstractmethod
    def prepare_response_for_tokens_dto(self, tokens_dto: TokensDTO):
        pass

    @abstractmethod
    def raise_user_account_does_not_exist(self):
        pass

    @abstractmethod
    def raise_invalid_email(self):
        pass

    @abstractmethod
    def get_success_response_for_reset_password_link_to_user_email(self):
        pass
