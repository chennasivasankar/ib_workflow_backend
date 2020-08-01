from typing import List
from ib_iam.adapters.service_adapter import get_service_adapter
from ib_iam.interactors.presenter_interfaces \
    .get_companies_presenter_interface import GetCompaniesPresenterInterface
from ib_iam.interactors.storage_interfaces \
    .company_storage_interface import CompanyStorageInterface
from ib_iam.interactors.presenter_interfaces \
    .get_companies_presenter_interface import CompanyWithEmployeesDetailsDTO
from ib_iam.interactors.storage_interfaces.dtos import (
    CompanyDTO, CompanyIdWithEmployeeIdsDTO, EmployeeDTO)
from ib_iam.adapters.dtos import UserProfileDTO
from ib_iam.exceptions.custom_exceptions import UserHasNoAccess


class GetCompaniesInteractor:

    def __init__(self, storage: CompanyStorageInterface):
        self.storage = storage

    def get_companies_wrapper(
            self,
            user_id: str,
            presenter: GetCompaniesPresenterInterface):
        try:
            company_details_dtos = self.get_companies(user_id=user_id)
            response = presenter.get_response_for_get_companies(
                company_details_dtos=company_details_dtos)
        except UserHasNoAccess:
            response = presenter \
                .get_user_has_no_access_response_for_get_companies()
        return response

    def get_companies(self, user_id: str):
        self.storage.validate_is_user_admin(user_id=user_id)
        company_dtos = self.storage.get_company_dtos()
        company_ids = self._get_company_ids_from_company_dtos(
            company_dtos=company_dtos)
        company_id_with_employee_ids_dtos = self.storage \
            .get_company_employee_ids_dtos(company_ids=company_ids)
        employee_ids = \
            self._get_all_employee_ids_from_company_employee_ids_dtos(
                company_id_with_employee_ids_dtos=
                company_id_with_employee_ids_dtos)
        employee_dtos = self._get_employees_dtos_from_service(
            employee_ids=employee_ids)
        company_with_employees_dto = CompanyWithEmployeesDetailsDTO(
            company_dtos=company_dtos,
            company_id_with_employee_ids_dtos=company_id_with_employee_ids_dtos,
            employee_dtos=employee_dtos)
        return company_with_employees_dto

    @staticmethod
    def _get_company_ids_from_company_dtos(company_dtos: List[CompanyDTO]) -> \
            List[str]:
        company_ids = [company_dto.company_id for company_dto in company_dtos]
        return company_ids

    @staticmethod
    def _get_all_employee_ids_from_company_employee_ids_dtos(
            company_id_with_employee_ids_dtos: List[
                CompanyIdWithEmployeeIdsDTO]):
        employee_ids = []
        for company_employee_ids_dto in company_id_with_employee_ids_dtos:
            employee_ids.extend(company_employee_ids_dto.employee_ids)
        unique_employee_ids = list(set(employee_ids))
        return unique_employee_ids

    def _get_employees_dtos_from_service(self, employee_ids: List[str]):
        service = get_service_adapter()
        user_dtos = service.user_service.get_basic_user_dtos(
            user_ids=employee_ids)
        employee_dtos = self._convert_user_dtos_to_employee_dtos(
            user_dtos=user_dtos)
        return employee_dtos

    @staticmethod
    def _convert_user_dtos_to_employee_dtos(user_dtos: List[UserProfileDTO]) \
            -> List[EmployeeDTO]:
        employee_dtos = [
            EmployeeDTO(employee_id=user_dto.user_id,
                        name=user_dto.name,
                        profile_pic_url=user_dto.profile_pic_url)
            for user_dto in user_dtos
        ]
        return employee_dtos
