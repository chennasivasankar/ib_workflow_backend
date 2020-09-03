import abc

from dataclasses import dataclass
from typing import List

from ib_iam.interactors.storage_interfaces.dtos import BasicUserDetailsDTO
from ib_iam.interactors.storage_interfaces.dtos import (
    CompanyDTO, CompanyIdWithEmployeeIdsDTO, EmployeeDTO
)


@dataclass
class CompanyWithEmployeeIdsAndUserDetailsDTO:
    company_dtos: List[CompanyDTO]
    company_id_with_employee_ids_dtos: List[CompanyIdWithEmployeeIdsDTO]
    user_dtos: List[BasicUserDetailsDTO]


class GetCompaniesPresenterInterface(abc.ABC):

    @abc.abstractmethod
    def get_user_has_no_access_response_for_get_companies(self):
        pass

    @abc.abstractmethod
    def get_response_for_get_companies(
            self, company_details_dtos: CompanyWithEmployeeIdsAndUserDetailsDTO
    ):
        pass
