from django_swagger_utils.utils.http_response_mixin import HTTPResponseMixin

from ib_iam.constants.exception_messages import USER_HAS_NO_ACCESS_FOR_GET_COMPANIES
from ib_iam.interactors.presenter_interfaces.get_companies_presenter_interface import \
    GetCompaniesPresenterInterface

from ib_iam.interactors.presenter_interfaces.get_companies_presenter_interface import \
    CompanyDetailsWithEmployeesCountDTO
from ib_iam.interactors.storage_interfaces.dtos import (
    CompanyDTO, CompanyWithEmployeesCountDTO
)


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
            company_details_dtos: CompanyDetailsWithEmployeesCountDTO
    ):
        company_details_dictionaries = \
            self._convert_company_details_dtos_into_company_dictionaries(
                company_details_dtos=company_details_dtos
            )
        response_dict = {
            "companies": company_details_dictionaries
        }
        return self.prepare_200_success_response(response_dict=response_dict)

    def _convert_company_details_dtos_into_company_dictionaries(
            self, company_details_dtos
    ):

        company_details_dictionaries = [
            self._convert_company_details_dto_into_company_details_dictionary(
                company_dto=company_dto,
                company_with_employees_count_dto=company_with_employees_count_dto
            ) for company_dto, company_with_employees_count_dto in zip(
                company_details_dtos.company_dtos,
                company_details_dtos.company_with_employees_count_dtos
            )
        ]
        return company_details_dictionaries

    def _convert_company_details_dto_into_company_details_dictionary(
            self,
            company_dto,
            company_with_employees_count_dto
    ):
        company_dictionary = self._convert_company_dto_to_company_dictionary(
            company_dto=company_dto
        )
        company_with_employees_count_dictionary = company_dictionary
        company_with_employees_count_dictionary["no_of_employees"] = \
            company_with_employees_count_dto.no_of_employees
        return company_with_employees_count_dictionary

    @staticmethod
    def _convert_company_dto_to_company_dictionary(company_dto: CompanyDTO):
        company_dictionary = {
            "company_id": company_dto.company_id,
            "name": company_dto.name,
            "description": company_dto.description,
            "logo_url": company_dto.logo_url
        }
        return company_dictionary
