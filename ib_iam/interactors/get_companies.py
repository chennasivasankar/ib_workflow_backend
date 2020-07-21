from ib_iam.interactors.storage_interfaces \
    .company_storage_interface import CompanyStorageInterface
from ib_iam.interactors.presenter_interfaces \
    .get_companies_presenter_interface import GetCompaniesPresenterInterface
from ib_iam.interactors.storage_interfaces.dtos import (
    PaginationDTO, CompanyDTO
)
from typing import List
from ib_iam.exceptions import (
    UserHasNoAccess, InvalidLimit, InvalidOffset
)


class GetCompaniesInteractor:

    def __init__(self, storage: CompanyStorageInterface):
        self.storage = storage

    def get_companies_wrapper(
            self,
            user_id: str,
            pagination_dto: PaginationDTO,
            presenter: GetCompaniesPresenterInterface
    ):
        try:
            company_details_dtos = self.get_companies(
                user_id=user_id, pagination_dto=pagination_dto
            )
            response = presenter.get_response_for_get_list_of_companies(
                company_details_dtos=company_details_dtos
            )
        except UserHasNoAccess:
            response = presenter.raise_exception_for_user_has_no_access()
        except InvalidLimit:
            response = presenter.raise_exception_for_invalid_limit()
        except InvalidOffset:
            response = presenter.raise_exception_for_invalid_offset()
        return response

    def get_companies(self, user_id: str, pagination_dto: PaginationDTO):
        self._validate_pagination_details(pagination_dto=pagination_dto)
        self.storage.is_user_admin(user_id=user_id)

        company_with_total_companies_count_dto = \
            self.storage.get_company_dtos_along_with_count(
                user_id=user_id,
                pagination_dto=pagination_dto
            )
        company_ids = self._get_company_ids_from_company_dtos(
            company_dtos=company_dtos
        )

        company_employee_count_dtos = self.storage.get_company_employee_ids_dtos(
            company_ids=company_ids
        )
        # Dto like c_id and no_of_employee
        company_details_dtos = GetListOfCompaniesResponseDTO(
            total_companies=total_companies,
            company_dtos=company_dtos,
            company_employee_count_dtos=company_employee_count_dtos
        )
        return company_details_dtos

    @staticmethod
    def _validate_pagination_details(pagination_dto: PaginationDTO):
        if pagination_dto.limit <= 0:
            raise InvalidLimit()
        if pagination_dto.offset < 0:
            raise InvalidOffset()

    @staticmethod
    def _get_company_ids_from_company_dtos(
            company_dtos: List[BasicCompanyDTO]
    ) -> List[str]:
        company_ids = [
            company_dto.company_id for company_dto in company_dtos
        ]
        return company_ids
