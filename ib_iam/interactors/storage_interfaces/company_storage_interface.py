from abc import ABC
from abc import abstractmethod
from typing import List
from ib_iam.interactors.storage_interfaces.dtos import (
    CompanyDTO, CompanyWithEmployeesCountDTO, CompanyDetailsWithUserIdsDTO
)


class CompanyStorageInterface(ABC):

    @abstractmethod
    def validate_is_user_admin(self, user_id: str):
        pass

    @abstractmethod
    def get_company_dtos(self) -> List[CompanyDTO]:
        pass

    @abstractmethod
    def get_company_with_employees_count_dtos(
            self, company_ids: List[str]
    ) -> List[CompanyWithEmployeesCountDTO]:
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
