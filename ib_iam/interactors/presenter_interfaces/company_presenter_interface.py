from abc import ABC
from abc import abstractmethod


class CompanyPresenterInterface(ABC):

    @abstractmethod
    def get_response_for_add_company(self, company_id: str):
        pass

    @abstractmethod
    def get_user_has_no_access_response_for_add_company(self):
        pass

    @abstractmethod
    def get_company_name_already_exists_response_for_add_company(
            self, exception
    ):
        pass

    @abstractmethod
    def get_duplicate_users_response_for_add_company(self):
        pass

    @abstractmethod
    def get_invalid_users_response_for_add_company(self):
        pass
