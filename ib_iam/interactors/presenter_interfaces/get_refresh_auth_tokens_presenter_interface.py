from abc import ABC, abstractmethod

from ib_iam.adapters.auth_service import UserTokensDTO


class GetRefreshTokensPresenterInterface(ABC):

    @abstractmethod
    def response_for_access_token_not_found(self):
        pass

    @abstractmethod
    def response_for_refresh_token_expired(self):
        pass

    @abstractmethod
    def response_for_refresh_token_not_found(self):
        pass

    @abstractmethod
    def response_for_user_account_not_found(self):
        pass

    @abstractmethod
    def response_for_user_tokens_dto(self, user_tokens_dto: UserTokensDTO):
        pass
