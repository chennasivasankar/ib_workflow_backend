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
    def prepare_response_for_tokens_dto(self, tokens_dto: TokensDTO,
                                        is_admin: bool):
        pass

    @abstractmethod
    def raise_user_account_does_not_exist(self):
        pass

    @abstractmethod
    def get_success_response_for_reset_password_link_to_user_email(self):
        pass

    @abstractmethod
    def raise_token_does_not_exists(self):
        pass

    @abstractmethod
    def raise_not_a_strong_password(self):
        pass

    @abstractmethod
    def raise_token_has_expired(self):
        pass

    @abstractmethod
    def get_update_user_password_success_response(self):
        pass
