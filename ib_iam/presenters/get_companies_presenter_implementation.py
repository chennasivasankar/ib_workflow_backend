from django_swagger_utils.utils.http_response_mixin import HTTPResponseMixin

from ib_iam.adapters.dtos import UserProfileDTO
from ib_iam.constants.exception_messages import \
    USER_HAS_NO_ACCESS_FOR_GET_COMPANIES
from ib_iam.interactors.presenter_interfaces \
    .get_companies_presenter_interface import \
    GetCompaniesPresenterInterface
from ib_iam.interactors.presenter_interfaces \
    .get_companies_presenter_interface import \
    CompanyWithEmployeeIdsAndUserDetailsDTO
from ib_iam.interactors.storage_interfaces.dtos import (
    CompanyDTO)
from ib_iam.interactors.storage_interfaces.dtos import EmployeeDTO


class GetCompaniesPresenterImplementation(
    GetCompaniesPresenterInterface, HTTPResponseMixin
):

    def get_user_has_no_access_response_for_get_companies(self):
        from ib_iam.constants.enums import StatusCode
        response_dict = {
            "response": USER_HAS_NO_ACCESS_FOR_GET_COMPANIES[0],
            "http_status_code": StatusCode.UNAUTHORIZED.value,
            "res_status": USER_HAS_NO_ACCESS_FOR_GET_COMPANIES[1]
        }
        return self.prepare_401_unauthorized_response(
            response_dict=response_dict
        )

    def get_response_for_get_companies(
            self,
            company_details_dtos: CompanyWithEmployeeIdsAndUserDetailsDTO
    ):
        company_details_dictionaries = \
            self._convert_company_details_dtos_into_company_dictionaries(
                company_details_dtos=company_details_dtos)
        response_dict = {"companies": company_details_dictionaries}
        return self.prepare_200_success_response(response_dict=response_dict)

    def _convert_company_details_dtos_into_company_dictionaries(
            self, company_details_dtos):
        company_dtos = company_details_dtos.company_dtos
        company_id_with_employee_ids_dtos = \
            company_details_dtos.company_id_with_employee_ids_dtos
        employees_dictionary = self._get_employees_dictionary(
            user_dtos=company_details_dtos.user_dtos)
        company_employee_ids_dictionary = self \
            ._get_company_employees_dictionary_from_company_employee_ids_dtos(
            company_id_with_employee_ids_dtos=company_id_with_employee_ids_dtos)
        company_details = [
            self._convert_to_company_details_dictionary(
                company_employee_ids_dict=company_employee_ids_dictionary,
                employees_dictionary=employees_dictionary,
                company_dto=company_dto
            ) for company_dto in company_dtos
        ]
        return company_details

    def _convert_to_company_details_dictionary(
            self,
            company_employee_ids_dict,
            employees_dictionary,
            company_dto):
        company_employees = self._get_employees(
            employees_ids=company_employee_ids_dict[
                company_dto.company_id],
            employees_dictionary=employees_dictionary)
        company_dictionary = self._convert_to_company_dictionary(
            company_dto=company_dto,
            company_employees=company_employees)
        return company_dictionary

    def _convert_to_company_dictionary(self, company_dto,
                                       company_employees):
        company_details_dict = self._convert_company_dto_to_company_dictionary(
            company_dto=company_dto)
        company_details_dict["employees"] = company_employees
        return company_details_dict

    @staticmethod
    def _convert_company_dto_to_company_dictionary(company_dto: CompanyDTO):
        company_dictionary = {
            "company_id": company_dto.company_id,
            "name": company_dto.name,
            "description": company_dto.description,
            "logo_url": company_dto.logo_url
        }
        return company_dictionary

    @staticmethod
    def _get_employees(employees_ids, employees_dictionary):
        employees_dict_list = [
            employees_dictionary[employee_id] for employee_id in employees_ids
        ]
        return employees_dict_list

    def _get_employees_dictionary(self, user_dtos):
        from collections import defaultdict
        employees_dictionaries = defaultdict()
        for user_dto in user_dtos:
            employees_dictionaries[user_dto.user_id] = \
                self._convert_user_dto_to_employee_dictionary(
                    user_dto=user_dto)
        return employees_dictionaries

    @staticmethod
    def _convert_user_dto_to_employee_dictionary(
            user_dto: UserProfileDTO):
        employee_dictionary = {"employee_id": user_dto.user_id,
                               "name": user_dto.name,
                               "profile_pic_url": user_dto.profile_pic_url}
        return employee_dictionary

    @staticmethod
    def _get_company_employees_dictionary_from_company_employee_ids_dtos(
            company_id_with_employee_ids_dtos):
        from collections import defaultdict
        company_id_with_employee_ids_dictionary = defaultdict(list)
        for company_id_with_employee_ids_dto in \
                company_id_with_employee_ids_dtos:
            company_id_with_employee_ids_dictionary[
                company_id_with_employee_ids_dto.company_id
            ] = company_id_with_employee_ids_dto.employee_ids
        return company_id_with_employee_ids_dictionary
