from abc import ABC
from abc import abstractmethod
from dataclasses import dataclass
from typing import List

from ib_iam.interactors.storage_interfaces.dtos import (
    CompanyWithEmployeeCountDTO, BasicCompanyDTO
)


@dataclass
class GetListOfCompaniesResponseDTO:
    total_companies: int
    company_dtos: List[BasicCompanyDTO]
    company_employee_count_dtos: List[CompanyWithEmployeeCountDTO]


class GetListOfCompaniesPresenterInterface(ABC):

    @abstractmethod
    def get_response_for_get_list_of_companies(
            self, company_details_dtos: GetListOfCompaniesResponseDTO
    ):
        pass
