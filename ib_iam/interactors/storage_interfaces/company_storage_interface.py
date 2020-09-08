import abc

from typing import List
from ib_iam.interactors.storage_interfaces.dtos import (
    CompanyDTO, CompanyIdWithEmployeeIdsDTO)
from ib_iam.interactors.storage_interfaces.dtos import \
    CompanyNameLogoAndDescriptionDTO


class CompanyStorageInterface(abc.ABC):

    @abc.abstractmethod
    def get_company_dtos(self) -> List[CompanyDTO]:
        pass

    @abc.abstractmethod
    def get_company_employee_ids_dtos(self, company_ids: List[str]) -> \
            List[CompanyIdWithEmployeeIdsDTO]:
        pass

    # TODO: Typing
    @abc.abstractmethod
    def get_company_id_if_company_name_already_exists(self, name: str):
        pass

    @abc.abstractmethod
    def add_company(
            self, company_name_logo_and_description_dto:
            CompanyNameLogoAndDescriptionDTO):
        pass

    @abc.abstractmethod
    def add_users_to_company(self, company_id: str, user_ids: List[str]):
        pass

    # TODO: Typing
    @abc.abstractmethod
    def validate_is_company_exists(self, company_id: str):
        pass

    @abc.abstractmethod
    def delete_company(self, company_id: str):
        pass

    @abc.abstractmethod
    def update_company_details(self, company_dto: CompanyDTO):
        pass

    @abc.abstractmethod
    def delete_all_existing_employees_of_company(self, company_id: str):
        pass
