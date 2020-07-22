from abc import ABC
from abc import abstractmethod
from ib_iam.interactors.storage_interfaces.dtos import (
    CompanyDTO, CompanyWithEmployeesCountDTO
)
from typing import List


class CompanyStorageInterface(ABC):

    @abstractmethod
    def raise_exception_if_user_is_not_admin(self, user_id: str):
        pass

    @abstractmethod
    def get_company_dtos(self) -> List[CompanyDTO]:
        pass

    @abstractmethod
    def get_company_with_employees_count_dtos(
            self, company_ids: List[str]
    ) -> List[CompanyWithEmployeesCountDTO]:
        pass
