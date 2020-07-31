from django_swagger_utils.utils.http_response_mixin import HTTPResponseMixin

from ib_iam.constants.enums import StatusCode
from ib_iam.interactors.presenter_interfaces.dtos \
    import UserOptionsDetailsDTO
from ib_iam.interactors.presenter_interfaces.get_user_options_presenter_interface import \
    GetUserOptionsPresenterInterface


class GetUserOptionsPresenterImplementation(GetUserOptionsPresenterInterface,
                                            HTTPResponseMixin):
    def get_user_options_details_response(
            self, configuration_details: UserOptionsDetailsDTO):
        companies = configuration_details.companies
        teams = configuration_details.teams
        roles = configuration_details.roles
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

    def raise_user_is_not_admin_exception(self):
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
    def _get_company_details(companies):
        companies_details = []
        for company in companies:
            companies_details.append({
                "company_id": company.company_id,
                "company_name": company.company_name
            })
        return companies_details

    @staticmethod
    def _get_role_details(roles):
        roles_details = []
        for role in roles:
            roles_details.append({
                "role_id": role.role_id,
                "role_name": role.name
            })
        return roles_details

    @staticmethod
    def _get_team_details(teams):
        teams_details = []
        for team in teams:
            teams_details.append({
                "team_id": team.team_id,
                "team_name": team.team_name
            })
        return teams_details
