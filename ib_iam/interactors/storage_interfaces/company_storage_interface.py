from abc import ABC
from abc import abstractmethod
from ib_iam.interactors.storage_interfaces.dtos import (
    PaginationDTO, BasicCompanyDTO, CompanyWithEmployeeCountDTO
)
from typing import List


class CompanyStorageInterface(ABC):

    @abstractmethod
    def is_user_admin(self, user_id: str):
        pass

    @abstractmethod
    def get_company_dtos_along_with_count(
            self, user_id: str, pagination_dto: PaginationDTO
    ) -> (List[BasicCompanyDTO], int):
        pass

    @abstractmethod
    def get_company_employee_ids_dtos(
            self, company_ids: List[str]
    ) -> List[CompanyWithEmployeeCountDTO]:
        pass
