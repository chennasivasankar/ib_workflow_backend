from ib_iam.interactors.storage_interfaces \
    .company_storage_interface import CompanyStorageInterface
from ib_iam.interactors.presenter_interfaces \
    .get_list_of_companies_presenter_interface import (
        GetListOfCompaniesPresenterInterface
    )
from ib_iam.interactors.storage_interfaces.dtos import (
    PaginationDTO, BasicCompanyDTO
)
from typing import List
from ib_iam.exceptions.custom_exceptions import (
    UserHasNoAccess, InvalidLimit, InvalidOffset
)


class GetListOfCompaniesInteractor:

    def __init__(self, storage: CompanyStorageInterface):
        self.storage = storage

    def get_list_of_companies_wrapper(
            self,
            user_id: str,
            pagination_dto: PaginationDTO,
            presenter: GetListOfCompaniesPresenterInterface
    ):
        try:
            company_details_dtos = self.get_list_of_companies(
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

    def get_list_of_companies(self, user_id: str, pagination_dto: PaginationDTO):
        self.storage.is_user_admin(user_id=user_id)
        self._is_invalid_limit(pagination_dto.limit)
        self._is_invalid_offset(pagination_dto.offset)

        (company_dtos, total_companies) = self.storage.get_company_dtos_along_with_count(
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
    def _is_invalid_limit(limit: int):
        is_invalid_limit = limit <= 0
        if is_invalid_limit:
            raise InvalidLimit()

    @staticmethod
    def _is_invalid_offset(offset: int):
        is_invalid_offset = offset < 0
        if is_invalid_offset:
            raise InvalidOffset()

    @staticmethod
    def _get_company_ids_from_company_dtos(
            company_dtos: List[BasicCompanyDTO]
    ) -> List[str]:
        company_ids = [
            company_dto.company_id for company_dto in company_dtos
        ]
        return company_ids
