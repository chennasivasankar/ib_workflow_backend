from ib_iam.interactors.storage_interfaces \
    .company_storage_interface import CompanyStorageInterface
from ib_iam.interactors.presenter_interfaces \
    .get_companies_presenter_interface import GetCompaniesPresenterInterface
from ib_iam.interactors.storage_interfaces.dtos import CompanyDTO
from ib_iam.interactors.presenter_interfaces \
    .get_companies_presenter_interface import CompanyDetailsWithEmployeesCountDTO
from typing import List
from ib_iam.exceptions import UserHasNoAccess


class GetCompaniesInteractor:

    def __init__(self, storage: CompanyStorageInterface):
        self.storage = storage

    def get_companies_wrapper(
            self,
            user_id: str,
            presenter: GetCompaniesPresenterInterface
    ):
        try:
            company_details_dtos = self.get_companies(user_id=user_id)
            response = presenter.get_response_for_get_companies(
                company_details_dtos=company_details_dtos
            )
        except UserHasNoAccess:
            response = presenter.get_user_has_no_access_response_for_get_companies()
        return response

    def get_companies(self, user_id: str):
        self.storage.raise_exception_if_user_is_not_admin(user_id=user_id)
        company_dtos = \
            self.storage.get_company_dtos()
        company_ids = self._get_company_ids_from_company_dtos(
            company_dtos=company_dtos
        )
        company_with_employees_count_dtos = \
            self.storage.get_company_with_employees_count_dtos(
                company_ids=company_ids
            )
        company_details_dtos = CompanyDetailsWithEmployeesCountDTO(
            company_dtos=company_dtos,
            company_with_employees_count_dtos=company_with_employees_count_dtos
        )
        return company_details_dtos

    @staticmethod
    def _get_company_ids_from_company_dtos(
            company_dtos: List[CompanyDTO]
    ) -> List[str]:
        company_ids = [company_dto.company_id for company_dto in company_dtos]
        return company_ids
