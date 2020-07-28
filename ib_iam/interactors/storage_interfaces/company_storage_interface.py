from abc import ABC
from abc import abstractmethod
from typing import List
from ib_iam.interactors.storage_interfaces.dtos import (
    CompanyDTO, CompanyEmployeeIdsDTO, CompanyDetailsWithUserIdsDTO,
    CompanyWithUserIdsDTO
)


class CompanyStorageInterface(ABC):

    @abstractmethod
    def validate_is_user_admin(self, user_id: str):
        pass

    @abstractmethod
    def get_company_dtos(self) -> List[CompanyDTO]:
        pass

    @abstractmethod
    def get_company_employee_ids_dtos(self, company_ids: List[str]) -> \
            List[CompanyEmployeesIdsDTO]:
        pass

    @abstractmethod
    def get_valid_user_ids_among_the_given_user_ids(self, user_ids: List[str]):
        pass

    @abstractmethod
    def get_company_id_if_company_name_already_exists(self, name: str):
        pass

    @abstractmethod
    def add_company(
            self,
            user_id: str,
            company_details_with_user_ids_dto: CompanyDetailsWithUserIdsDTO
    ):
        pass

    @abstractmethod
    def add_users_to_company(self, company_id: str, user_ids: List[str]):
        pass

    @abstractmethod
    def validate_is_company_exists(self, company_id: str):
        pass

    @abstractmethod
    def delete_company(self, company_id: str):
        pass

    @abstractmethod
    def update_company_details(
            self, company_with_user_ids_dto: CompanyWithUserIdsDTO
    ):
        pass

    @abstractmethod
    def get_employee_ids_of_company(self, company_id: str):
        pass

    @abstractmethod
    def delete_employees_from_company(self, company_id: str, employee_ids: List[str]):
        pass
