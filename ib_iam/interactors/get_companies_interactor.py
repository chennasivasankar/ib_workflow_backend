from typing import List
from ib_iam.interactors.mixins.validation import ValidationMixin
from ib_iam.interactors.presenter_interfaces \
    .get_companies_presenter_interface import GetCompaniesPresenterInterface
from ib_iam.interactors.storage_interfaces \
    .company_storage_interface import CompanyStorageInterface
from ib_iam.interactors.presenter_interfaces \
    .get_companies_presenter_interface import CompanyWithEmployeeIdsAndUserDetailsDTO
from ib_iam.interactors.storage_interfaces.dtos import (
    CompanyDTO, CompanyIdWithEmployeeIdsDTO)
from ib_iam.interactors.storage_interfaces.user_storage_interface import \
    UserStorageInterface


class GetCompaniesInteractor(ValidationMixin):

    def __init__(self,
                 company_storage: CompanyStorageInterface,
                 user_storage: UserStorageInterface):
        self.user_storage = user_storage
        self.company_storage = company_storage

    def get_companies_wrapper(self, user_id: str,
                              presenter: GetCompaniesPresenterInterface):
        from ib_iam.exceptions.custom_exceptions import UserIsNotAdmin
        try:
            company_details_dtos = self.get_companies(user_id=user_id)
            response = presenter.get_response_for_get_companies(
                company_details_dtos=company_details_dtos)
        except UserIsNotAdmin:
            response = presenter \
                .get_user_has_no_access_response_for_get_companies()
        return response

    def get_companies(self, user_id: str):
        self._validate_is_user_admin(user_id=user_id)
        company_dtos = self.company_storage.get_company_dtos()
        company_ids = self._get_company_ids_from_company_dtos(
            company_dtos=company_dtos)
        company_id_with_employee_ids_dtos = self.company_storage \
            .get_company_employee_ids_dtos(company_ids=company_ids)
        employee_ids = \
            self._get_all_employee_ids_from_company_employee_ids_dtos(
                company_id_with_employee_ids_dtos=
                company_id_with_employee_ids_dtos)
        user_dtos = self._get_user_dtos_from_service(
            employee_ids=employee_ids)
        company_with_employee_ids_and_users_dto = \
            CompanyWithEmployeeIdsAndUserDetailsDTO(
                company_dtos=company_dtos,
                company_id_with_employee_ids_dtos=company_id_with_employee_ids_dtos,
                user_dtos=user_dtos)
        return company_with_employee_ids_and_users_dto

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

    @staticmethod
    def _get_user_dtos_from_service(employee_ids: List[str]):
        from ib_iam.adapters.service_adapter import get_service_adapter
        service = get_service_adapter()
        user_dtos = service.user_service.get_basic_user_dtos(
            user_ids=employee_ids)
        return user_dtos
