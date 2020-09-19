import abc
from ib_iam.interactors.presenter_interfaces.dtos import \
    CompanyWithEmployeeIdsAndUserDetailsDTO


class UpdateCompanyPresenterInterface(abc.ABC):

    @abc.abstractmethod
    def get_response_for_update_company(self):
        pass

    @abc.abstractmethod
    def response_for_user_has_no_access_exception(self):
        pass

    @abc.abstractmethod
    def response_for_invalid_company_id_exception(self):
        pass

    @abc.abstractmethod
    def response_for_company_name_already_exists_exception(
            self, err
    ):
        pass

    @abc.abstractmethod
    def response_for_duplicate_user_ids_exception(self):
        pass

    @abc.abstractmethod
    def response_for_invalid_user_ids_exception(self):
        pass


class GetCompaniesPresenterInterface(abc.ABC):

    @abc.abstractmethod
    def response_for_user_has_no_access_exception(self):
        pass

    @abc.abstractmethod
    def get_response_for_get_companies(
            self, company_details_dtos: CompanyWithEmployeeIdsAndUserDetailsDTO
    ):
        pass


class DeleteCompanyPresenterInterface(abc.ABC):

    @abc.abstractmethod
    def get_success_response_for_delete_company(self):
        pass

    @abc.abstractmethod
    def response_for_user_has_no_access_exception(self):
        pass

    @abc.abstractmethod
    def response_for_invalid_company_id_exception(self):
        pass


class AddCompanyPresenterInterface(abc.ABC):

    @abc.abstractmethod
    def get_response_for_add_company(self, company_id: str):
        pass

    @abc.abstractmethod
    def response_for_user_has_no_access_exception(self):
        pass

    @abc.abstractmethod
    def response_for_company_name_already_exists_exception(
            self, err
    ):
        pass

    @abc.abstractmethod
    def response_for_duplicate_user_ids_exception(self):
        pass

    @abc.abstractmethod
    def response_for_invalid_user_ids_exception(self):
        pass
