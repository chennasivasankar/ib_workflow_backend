from typing import List

from django_swagger_utils.utils.http_response_mixin import HTTPResponseMixin

from ib_iam.constants.enums import StatusCode
from ib_iam.interactors.presenter_interfaces.dtos \
    import UserOptionsDetailsDTO
from ib_iam.interactors.presenter_interfaces.user_presenter_interface import \
    GetUserOptionsPresenterInterface
from ib_iam.interactors.storage_interfaces.dtos import CompanyIdAndNameDTO, \
    RoleIdAndNameDTO, TeamIdAndNameDTO


class GetUserOptionsPresenterImplementation(GetUserOptionsPresenterInterface,
                                            HTTPResponseMixin):
    def get_user_options_details_response(
            self, configuration_details_dto: UserOptionsDetailsDTO):
        companies = configuration_details_dto.companies
        teams = configuration_details_dto.teams
        roles = configuration_details_dto.roles
        companies_details = self._get_company_details(companies)
        teams_details = self._get_team_details(teams)
        roles_details = self._get_role_details(roles)
        response_dict = {
            "companies": companies_details,
            "teams": teams_details,
            "roles": roles_details
        }
        return self.prepare_200_success_response(
            response_dict=response_dict)

    def response_for_user_is_not_admin_exception(self):
        from ib_iam.constants.exception_messages import \
            USER_DOES_NOT_HAVE_PERMISSION
        response_dict = {
            "response": USER_DOES_NOT_HAVE_PERMISSION[0],
            "http_status_code": StatusCode.FORBIDDEN.value,
            "res_status": USER_DOES_NOT_HAVE_PERMISSION[1]
        }
        return self.prepare_403_forbidden_response(
            response_dict=response_dict)

    @staticmethod
    def _get_company_details(
            company_dtos: List[CompanyIdAndNameDTO]) -> List[dict]:
        companies = [
            {
                "company_id": company_id_and_name_dto.company_id,
                "company_name": company_id_and_name_dto.company_name
            } for company_id_and_name_dto in company_dtos
        ]
        return companies

    @staticmethod
    def _get_role_details(role_dtos: List[RoleIdAndNameDTO]) -> List[dict]:
        roles = [
            {
                "role_id": role_id_and_name_dto.role_id,
                "role_name": role_id_and_name_dto.name
            } for role_id_and_name_dto in role_dtos
        ]
        return roles

    @staticmethod
    def _get_team_details(team_dtos: List[TeamIdAndNameDTO]) -> List[dict]:
        teams = [
            {
                "team_id": team_id_and_name_dto.team_id,
                "team_name": team_id_and_name_dto.team_name
            } for team_id_and_name_dto in team_dtos
        ]
        return teams
