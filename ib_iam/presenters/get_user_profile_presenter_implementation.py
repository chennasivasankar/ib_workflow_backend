from typing import List, Optional

from django_swagger_utils.utils.http_response_mixin import HTTPResponseMixin

from ib_iam.adapters.dtos import UserProfileDTO
from ib_iam.constants.enums import StatusCode
from ib_iam.interactors.dtos.dtos import CompleteUserProfileDTO
from ib_iam.interactors.presenter_interfaces.auth_presenter_interface import \
    GetUserProfilePresenterInterface
from ib_iam.interactors.presenter_interfaces.dtos import \
    UserWithExtraDetailsDTO
from ib_iam.interactors.storage_interfaces.dtos import TeamDTO, CompanyDTO, \
    CompanyIdWithEmployeeIdsDTO, TeamUserIdsDTO, UserRoleDTO

INVALID_USER_ID = (
    "Please send valid user id, given user id is empty",
    "INVALID_USER_ID"
)

USER_ACCOUNT_DOES_NOT_EXIST = (
    "Please send valid user id",
    "USER_ACCOUNT_DOES_NOT_EXIST"
)


class GetUserProfilePresenterImplementation(
    GetUserProfilePresenterInterface, HTTPResponseMixin
):

    def response_for_invalid_user_id_exception(self):
        response_dict = {
            "response": INVALID_USER_ID[0],
            "http_status_code": StatusCode.BAD_REQUEST.value,
            "res_status": INVALID_USER_ID[1]
        }
        return self.prepare_400_bad_request_response(
            response_dict=response_dict
        )

    def response_for_user_account_does_not_exist_exception(self):
        response_dict = {
            "response": USER_ACCOUNT_DOES_NOT_EXIST[0],
            "http_status_code": StatusCode.NOT_FOUND.value,
            "res_status": USER_ACCOUNT_DOES_NOT_EXIST[1]
        }
        return self.prepare_404_not_found_response(response_dict=response_dict)

    def response_for_get_user_profile(
            self,
            user_with_extra_details_dto: UserWithExtraDetailsDTO):
        user_profile_dto = user_with_extra_details_dto.user_profile_dto
        teams = self._convert_team_dtos_to_teams(
            team_dtos=user_with_extra_details_dto.team_dtos,
            user_dtos=user_with_extra_details_dto.user_dtos,
            team_user_ids_dtos=user_with_extra_details_dto.team_user_ids_dto
        )
        company_dictionary = self._get_company_dictionary(
            company_dto=user_with_extra_details_dto.company_dto,
            user_dtos=user_with_extra_details_dto.user_dtos,
            company_id_with_employee_ids_dto=user_with_extra_details_dto.company_id_with_employee_ids_dto
        )
        roles = self._get_roles(
            role_dtos=user_with_extra_details_dto.role_dtos
        )
        response_dict = self._get_user_profile_dict_from_user_profile_dto(
            user_profile_dto=user_profile_dto, teams=teams, roles=roles,
            company=company_dictionary
        )
        return self.prepare_200_success_response(response_dict=response_dict)

    @staticmethod
    def _get_user_profile_dict_from_user_profile_dto(
            user_profile_dto: CompleteUserProfileDTO, teams: List[dict],
            company: Optional[dict], roles: List[dict]
    ) -> dict:
        cover_page_url = user_profile_dto.cover_page_url
        if cover_page_url is None:
            cover_page_url = ""
        user_profile_dictionary = {
            "user_id": user_profile_dto.user_id, "name": user_profile_dto.name,
            "is_admin": user_profile_dto.is_admin,
            "email": user_profile_dto.email,
            "profile_pic_url": user_profile_dto.profile_pic_url,
            "cover_page_url": cover_page_url, "teams": teams, "roles": roles
        }
        if company is not None:
            user_profile_dictionary["company"] = company
        else:
            user_profile_dictionary["company"] = None
        return user_profile_dictionary

    @staticmethod
    def _get_roles(role_dtos: List[UserRoleDTO]):
        roles = [
            {"role_id": role_dto.role_id, "role_name": role_dto.name}
            for role_dto in role_dtos
        ]
        return roles

    def _convert_team_dtos_to_teams(
            self, team_dtos: List[TeamDTO], user_dtos: List[UserProfileDTO],
            team_user_ids_dtos: List[TeamUserIdsDTO]
    ):
        teams = []
        for team_dto in team_dtos:
            team_dictionary = self._convert_to_team_dictionary(team_dto)
            team_dictionary["members"] = self._get_team_members(
                team_dto=team_dto, team_user_ids_dtos=team_user_ids_dtos,
                user_dtos=user_dtos)
            teams.append(team_dictionary)
        return teams

    # Todo: Typing
    def _get_team_members(self, team_dto, team_user_ids_dtos, user_dtos):
        members = []
        for team_user_ids_dto in team_user_ids_dtos:
            if team_user_ids_dto.team_id == team_dto.team_id:
                members = [
                    self._convert_user_dto_to_member_dictionary(user_dto)
                    for user_dto in user_dtos
                    if user_dto.user_id in team_user_ids_dto.user_ids
                ]
        return members

    @staticmethod
    def _convert_user_dto_to_member_dictionary(user_dto: UserProfileDTO):
        member_dictionary = {
            "member_id": user_dto.user_id,
            "name": user_dto.name,
            "profile_pic_url": user_dto.profile_pic_url
        }
        return member_dictionary

    # Todo: Typing
    @staticmethod
    def _convert_to_team_dictionary(team_dto):
        team_details_dict = {
            "team_id": team_dto.team_id,
            "name": team_dto.name, "description": team_dto.description
        }
        return team_details_dict

    # TODO: conditional encapsulation, decrease indent depth
    def _get_company_dictionary(
            self, company_dto: CompanyDTO, user_dtos: List[UserProfileDTO],
            company_id_with_employee_ids_dto: CompanyIdWithEmployeeIdsDTO
    ):
        if company_dto is None:
            return None
        company_dictionary = self._convert_company_dto_to_dictionary(
            company_dto=company_dto)
        employees = []
        for user_id in company_id_with_employee_ids_dto.employee_ids:
            for user_dto in user_dtos:
                if user_dto.user_id == user_id:
                    employees.append(
                        self._convert_user_dto_to_employee_dictionary(
                            user_dto=user_dto)
                    )
        company_dictionary["employees"] = employees
        return company_dictionary

    @staticmethod
    def _convert_company_dto_to_dictionary(company_dto: CompanyDTO):
        company_dictionary = {
            "company_id": company_dto.company_id, "name": company_dto.name,
            "description": company_dto.description,
            "logo_url": company_dto.logo_url
        }
        return company_dictionary

    @staticmethod
    def _convert_user_dto_to_employee_dictionary(
            user_dto: UserProfileDTO):
        employee_dictionary = {
            "employee_id": user_dto.user_id, "name": user_dto.name,
            "profile_pic_url": user_dto.profile_pic_url
        }
        return employee_dictionary
