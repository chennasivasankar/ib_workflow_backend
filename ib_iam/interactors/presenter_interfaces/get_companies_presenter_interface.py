from abc import ABC
from abc import abstractmethod
from dataclasses import dataclass
from typing import List

from ib_iam.interactors.storage_interfaces.dtos import (
    CompanyDTO, CompanyWithEmployeesCountDTO
)


@dataclass
class CompanyDetailsWithEmployeesCountDTO:
    company_dtos: List[CompanyDTO]
    company_with_employees_count_dtos: List[CompanyWithEmployeesCountDTO]


class GetCompaniesPresenterInterface(ABC):

    @abstractmethod
    def get_user_has_no_access_response_for_get_companies(self):
        pass

    @abstractmethod
    def get_response_for_get_companies(
            self, company_details_dtos: CompanyDetailsWithEmployeesCountDTO
    ):
        pass
