from abc import ABC
from abc import abstractmethod
from dataclasses import dataclass
from typing import List

from ib_iam.interactors.storage_interfaces.dtos import (
    CompanyDTO, CompanyIdWithEmployeeIdsDTO, EmployeeDTO
)


@dataclass
class CompanyWithEmployeesDetailsDTO:
    company_dtos: List[CompanyDTO]
    company_id_with_employee_ids_dtos: List[CompanyIdWithEmployeeIdsDTO]
    employee_dtos: List[EmployeeDTO]


class GetCompaniesPresenterInterface(ABC):

    @abstractmethod
    def get_user_has_no_access_response_for_get_companies(self):
        pass

    @abstractmethod
    def get_response_for_get_companies(
            self, company_details_dtos: CompanyWithEmployeesDetailsDTO
    ):
        pass
