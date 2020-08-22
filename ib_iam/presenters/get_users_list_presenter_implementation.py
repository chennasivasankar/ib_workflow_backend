from typing import List, Optional

from django_swagger_utils.utils.http_response_mixin import HTTPResponseMixin

from ib_iam.adapters.dtos import UserProfileDTO
from ib_iam.constants.enums import StatusCode
from ib_iam.interactors.presenter_interfaces.dtos import ListOfCompleteUsersDTO
from ib_iam.interactors.presenter_interfaces.get_users_list_presenter_interface \
    import GetUsersListPresenterInterface
from ib_iam.interactors.storage_interfaces.dtos import UserTeamDTO, \
    UserRoleDTO, UserCompanyDTO, TeamIdAndNameDTO, RoleIdAndNameDTO, RoleDTO


class GetUsersListPresenterImplementation(GetUsersListPresenterInterface,
                                          HTTPResponseMixin):
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

    def raise_invalid_offset_value_exception(self):
        from ib_iam.constants.exception_messages import INVALID_OFFSET_VALUE
        response_dict = {
            "response": INVALID_OFFSET_VALUE[0],
            "http_status_code": StatusCode.BAD_REQUEST.value,
            "res_status": INVALID_OFFSET_VALUE[1]
        }
        return self.prepare_400_bad_request_response(
            response_dict=response_dict)

    def raise_invalid_limit_value_exception(self):
        from ib_iam.constants.exception_messages import INVALID_LIMIT_VALUE
        response_dict = {
            "response": INVALID_LIMIT_VALUE[0],
            "http_status_code": StatusCode.BAD_REQUEST.value,
            "res_status": INVALID_LIMIT_VALUE[1]
        }
        return self.prepare_400_bad_request_response(
            response_dict=response_dict)

    def response_for_get_users(
            self, complete_user_details_dtos: ListOfCompleteUsersDTO):
        user_dtos = complete_user_details_dtos.users
        team_dtos = complete_user_details_dtos.teams
        # role_dtos = complete_user_details_dtos.roles
        company_dtos = complete_user_details_dtos.companies
        total_no_of_users = complete_user_details_dtos.total_no_of_users
        users = self._prepare_response_for_user_details(
            user_dtos, team_dtos, company_dtos)
        response = {
            "users": users,
            "total": total_no_of_users
        }
        return self.prepare_200_success_response(
            response_dict=response)

    def _prepare_response_for_user_details(
            self, user_dtos, team_dtos, company_dtos):
        users = []
        for user_profile_dto in user_dtos:
            user_id = user_profile_dto.user_id
            user_team_dtos = self._get_user_teams(team_dtos, user_id)
            # user_role_dtos = self._get_user_roles(role_dtos, user_id)
            user_company_dto = self._get_company(company_dtos, user_id)
            user_response_dict = self._convert_user_response_dict(
                user_profile_dto, user_team_dtos, user_role_dtos,
                user_company_dto)
            users.append(user_response_dict)
        return users

    def _convert_user_response_dict(
            self, user_profile_dto: UserProfileDTO,
            user_team_dtos: List[UserTeamDTO],
            user_role_dtos: List[UserRoleDTO],
            user_company_dto: UserCompanyDTO):
        user_response_dict = {
            "user_id": user_profile_dto.user_id,
            "name": user_profile_dto.name,
            "email": user_profile_dto.email,
            "teams": self._convert_to_teams_dict(user_team_dtos),
            "company": self._convert_to_company_dict(user_company_dto)
        }
        return user_response_dict

    @staticmethod
    def _convert_to_company_dict(
            user_company_dto: Optional[UserCompanyDTO]) -> Optional[dict]:
        if user_company_dto is None:
            return user_company_dto
        return {
            "company_name": user_company_dto.company_name,
            "company_id": user_company_dto.company_id
        }

    def raise_invalid_user(self):
        from ib_iam.constants.exception_messages import \
            INVALID_USER
        response_dict = {
            "response": INVALID_USER[0],
            "http_status_code": StatusCode.NOT_FOUND.value,
            "res_status": INVALID_USER[1]
        }
        return self.prepare_404_not_found_response(
            response_dict=response_dict)

    @staticmethod
    def _get_user_teams(
            team_dtos: List[UserTeamDTO], user_id: str) -> List[UserTeamDTO]:
        user_teams = [
            user_team
            for user_team in team_dtos if user_team.user_id == user_id]
        return user_teams

    # @staticmethod
    # def _get_user_roles(
    #         user_role_dtos: List[UserRoleDTO], user_id: str
    # ) -> List[UserRoleDTO]:
    #     user_roles = [
    #         user_role
    #         for user_role in user_role_dtos if user_role.user_id == user_id]
    #     return user_roles

    @staticmethod
    def _get_company(
            company_dtos: List[UserCompanyDTO], user_id: str
    ) -> Optional[UserCompanyDTO]:
        for company_dto in company_dtos:
            if company_dto.user_id == user_id:
                if company_dto.company_id is None:
                    return None
                return company_dto

    @staticmethod
    def _convert_to_teams_dict(
            team_dtos: List[UserTeamDTO]) -> List[dict]:
        teams = [
            {
                "team_id": team_dto.team_id, "team_name": team_dto.team_name
            } for team_dto in team_dtos]
        return teams

    # @staticmethod
    # def _convert_to_roles_dict(
    #         role_dtos: List[UserRoleDTO]) -> List[dict]:
    #     roles = [
    #         {
    #             "role_id": role_dto.role_id, "role_name": role_dto.name
    #         } for role_dto in role_dtos
    #     ]
    #     return roles
