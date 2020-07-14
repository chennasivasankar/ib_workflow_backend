from abc import abstractmethod, ABC

from ib_iam.adapters.auth_service import TokensDTO


class PresenterInterface(ABC):

    @abstractmethod
    def raise_invalid_email(self):
        pass

    @abstractmethod
    def raise_invalid_password(self):
        pass

    @abstractmethod
    def prepare_response_for_tokens_dto(self, tokens_dto: TokensDTO):
        pass
