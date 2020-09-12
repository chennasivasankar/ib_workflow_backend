import abc


class UpdateCompanyPresenterInterface(abc.ABC):

    @abc.abstractmethod
    def get_success_response_for_update_company(self):
        pass

    @abc.abstractmethod
    def get_user_has_no_access_response_for_update_company(self):
        pass

    @abc.abstractmethod
    def get_invalid_company_response_for_update_company(self):
        pass

    @abc.abstractmethod
    def get_company_name_already_exists_response_for_update_company(
            self, exception
    ):
        pass

    @abc.abstractmethod
    def get_duplicate_users_response_for_update_company(self):
        pass

    @abc.abstractmethod
    def get_invalid_users_response_for_update_company(self):
        pass
