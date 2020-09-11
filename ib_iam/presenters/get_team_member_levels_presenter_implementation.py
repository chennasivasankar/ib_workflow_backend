from typing import List

from django_swagger_utils.utils.http_response_mixin import HTTPResponseMixin

from ib_iam.constants.enums import StatusCode
from ib_iam.interactors.presenter_interfaces.level_presenter_interface import \
    GetTeamMemberLevelsPresenterInterface
from ib_iam.interactors.storage_interfaces.dtos import \
    TeamMemberLevelDetailsDTO

INVALID_TEAM_ID = (
    "Please send valid team id to get team member level details",
    "INVALID_TEAM_ID"
)

USER_DOES_NOT_HAVE_ACCESS = (
    "User does not have provision to access",
    "USER_DOES_NOT_HAVE_ACCESS"
)


class GetTeamMemberLevelsPresenterImplementation(
    GetTeamMemberLevelsPresenterInterface, HTTPResponseMixin
):

    def response_for_team_member_level_details_dtos(
            self,
            team_member_level_details_dtos: List[TeamMemberLevelDetailsDTO]):
        level_details_list = [
            {
                "team_member_level_id": team_member_level_details_dto.team_member_level_id,
                "team_member_level_name": team_member_level_details_dto.team_member_level_name,
                "level_hierarchy": team_member_level_details_dto.level_hierarchy
            }
            for team_member_level_details_dto in team_member_level_details_dtos
        ]
        level_details_list = sorted(
            level_details_list,
            key=lambda x: x["level_hierarchy"]
        )
        response = {
            "levels": level_details_list
        }
        return self.prepare_200_success_response(response_dict=response)

    def response_for_invalid_team_id(self):
        response_dict = {
            "response": INVALID_TEAM_ID[0],
            "http_status_code": StatusCode.BAD_REQUEST.value,
            "res_status": INVALID_TEAM_ID[1]
        }
        return self.prepare_400_bad_request_response(
            response_dict=response_dict)

    def response_for_user_is_not_admin(self):
        response_dict = {
            "response": USER_DOES_NOT_HAVE_ACCESS[0],
            "http_status_code": StatusCode.FORBIDDEN.value,
            "res_status": USER_DOES_NOT_HAVE_ACCESS[1]
        }
        return self.prepare_403_forbidden_response(
            response_dict=response_dict
        )
