from abc import ABC
from abc import abstractmethod


class DeleteCompanyPresenterInterface(ABC):

    @abstractmethod
    def get_success_response_for_delete_company(self):
        pass

    @abstractmethod
    def get_user_has_no_access_response_for_delete_company(self):
        pass

    @abstractmethod
    def get_invalid_company_response_for_delete_company(self):
        pass
