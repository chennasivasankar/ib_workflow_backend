from django_swagger_utils.utils.http_response_mixin \
    import HTTPResponseMixin

from ib_iam.interactors.presenter_interfaces.dtos import CompleteUserDetailsDTO
from ib_iam.interactors.presenter_interfaces.presenter_interface \
    import PresenterInterface


class PresenterImplementation(PresenterInterface, HTTPResponseMixin):
    def raise_user_is_not_admin_exception(self):
        from ib_iam.constants.exception_messages import USER_DOES_NOT_HAVE_PERMISSION
        response_dict = {
            "response": USER_DOES_NOT_HAVE_PERMISSION[0],
            "http_status_code": 403,
            "res_status": USER_DOES_NOT_HAVE_PERMISSION[1]
        }
        return self.prepare_403_forbidden_response(
            response_dict=response_dict)

    def raise_invalid_offset_value_exception(self):
        from ib_iam.constants.exception_messages import INVALID_OFFSET_VALUE
        response_dict = {
            "response": INVALID_OFFSET_VALUE[0],
            "http_status_code": 400,
            "res_status": INVALID_OFFSET_VALUE[1]
        }
        return self.prepare_400_bad_request_response(
            response_dict=response_dict)

    def raise_invalid_limit_value_exception(self):
        from ib_iam.constants.exception_messages import INVALID_LIMIT_VALUE
        response_dict = {
            "response": INVALID_LIMIT_VALUE[0],
            "http_status_code": 400,
            "res_status": INVALID_LIMIT_VALUE[1]
        }
        return self.prepare_400_bad_request_response(
            response_dict=response_dict)

    def raise_offset_value_is_greater_than_limit_value_exception(self):
        from ib_iam.constants.exception_messages import OFFSET_VALUE_IS_GREATER_THAN_LIMIT
        response_dict = {
            "response": OFFSET_VALUE_IS_GREATER_THAN_LIMIT[0],
            "http_status_code": 400,
            "res_status": OFFSET_VALUE_IS_GREATER_THAN_LIMIT[1]
        }
        return self.prepare_400_bad_request_response(
            response_dict=response_dict)

    def response_for_get_users(
            self, complete_user_details_dtos: CompleteUserDetailsDTO):
        response = []
        user_dtos = complete_user_details_dtos.users
        team_dtos = complete_user_details_dtos.teams
        role_dtos = complete_user_details_dtos.roles
        company_dtos = complete_user_details_dtos.companies

        total_no_of_users = complete_user_details_dtos.total_no_of_users
        users = []
        for user_profile_dto in user_dtos:
            user_id = user_profile_dto.user_id
            user_team_dtos = self._get_user_teams(team_dtos, user_id)
            user_role_dtos = self._get_user_roles(role_dtos, user_id)
            user_company_dto = self._get_company(company_dtos, user_id)
            user_response_dict = self._convert_user_response_dict(
                user_profile_dto, user_team_dtos, user_role_dtos,
                user_company_dto)
            users.append(user_response_dict)
        response = {
            "users": users,
            "total":total_no_of_users
        }
        return response

    def _convert_user_response_dict(
            self, user_profile_dto, user_team_dtos, user_role_dtos,
            user_company_dto):

        user_response_dict = {
            "user_id": user_profile_dto.user_id,
            "name": user_profile_dto.name,
            "email": user_profile_dto.email,
            "teams": self._convert_to_teams_dict(user_team_dtos),
            "roles": self._convert_to_roles_dict(user_role_dtos),
            "company": {
                "company_name": user_company_dto.company_id,
                "company_id": user_company_dto.company_name
            }
        }
        return user_response_dict

    @staticmethod
    def _get_user_teams(team_dtos, user_id):
        teams = []
        for team_dto in team_dtos:
            if team_dto.user_id == user_id:
                teams.append(team_dto)
        return teams

    @staticmethod
    def _get_user_roles(role_dtos, user_id):
        roles = []
        for role_dto in role_dtos:
            if role_dto.user_id == user_id:
                roles.append(role_dto)
        return roles

    @staticmethod
    def _get_company(company_dtos, user_id):
        for company_dto in company_dtos:
            if company_dto.user_id == user_id:
                return company_dto

    @staticmethod
    def _convert_to_teams_dict(team_dtos):
        teams = []
        for team_dto in team_dtos:
            teams.append({
                "team_id": team_dto.team_id,
                "team_name": team_dto.team_name
            })
        return teams

    @staticmethod
    def _convert_to_roles_dict(role_dtos):
        roles = []
        for role_dto in role_dtos:
            roles.append({
                "role_id": role_dto.role_id,
                "role_name": role_dto.role_name
            })
        return roles
