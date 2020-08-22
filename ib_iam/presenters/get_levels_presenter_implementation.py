from typing import List

from django_swagger_utils.utils.http_response_mixin import HTTPResponseMixin

from ib_iam.interactors.presenter_interfaces.level_presenter_interface import \
    GetTeamMemberLevelsPresenterInterface
from ib_iam.interactors.storage_interfaces.dtos import TeamMemberLevelDetailsDTO


class GetTeamMemberLevelsPresenterImplementation(
    GetTeamMemberLevelsPresenterInterface, HTTPResponseMixin
):

    def response_for_team_member_level_details_dtos(
            self, team_member_level_details_dtos: List[TeamMemberLevelDetailsDTO]):
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
