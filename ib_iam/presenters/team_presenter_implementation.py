from django_swagger_utils.utils.http_response_mixin import HTTPResponseMixin

from ib_iam.interactors.presenter_interfaces.dtos import TeamWithMembersDetailsDTO
from ib_iam.interactors.presenter_interfaces.team_presenter_interface import TeamPresenterInterface
from ib_iam.constants.exception_messages import (
    USER_HAS_NO_ACCESS, INVALID_LIMIT, INVALID_OFFSET
)


class TeamPresenterImplementation(TeamPresenterInterface, HTTPResponseMixin):

    def raise_exception_for_user_has_no_access(self):
        response_dict = {
            "response": USER_HAS_NO_ACCESS[0],
            "http_status_code": 401,
            "res_status": USER_HAS_NO_ACCESS[1]
        }
        return self.prepare_401_unauthorized_response(
            response_dict=response_dict
        )

    def raise_exception_for_invalid_limit(self):
        response_dict = {
            "response": INVALID_LIMIT[0],
            "http_status_code": 400,
            "res_status": INVALID_LIMIT[1]
        }
        return self.prepare_400_bad_request_response(
            response_dict=response_dict
        )

    def raise_exception_for_invalid_offset(self):
        response_dict = {
            "response": INVALID_OFFSET[0],
            "http_status_code": 400,
            "res_status": INVALID_OFFSET[1]
        }
        return self.prepare_400_bad_request_response(
            response_dict=response_dict
        )

    def get_response_for_get_list_of_teams(
            self, team_details_dtos: TeamWithMembersDetailsDTO
    ):
        team_details_dict = self._make_all_teams_details_dict(team_details_dtos=team_details_dtos)
        return self.prepare_200_success_response(response_dict=team_details_dict)

    def _make_all_teams_details_dict(self, team_details_dtos: TeamWithMembersDetailsDTO):
        team_dtos = team_details_dtos.team_dtos
        team_member_ids_dtos = team_details_dtos.team_member_ids_dtos
        members_dtos = team_details_dtos.member_dtos
        all_members_dict = self._get_all_members_details_dict(members_dtos=members_dtos)
        team_member_ids_dict = self.get_team_members_dict_from_team_member_ids_dtos(
            team_member_ids_dtos=team_member_ids_dtos
        )
        teams_details_dict_list = []
        for team_dto in team_dtos:
            teams_details_dict = self._make_single_team_details_dict(
                team_member_ids_dict=team_member_ids_dict,
                all_members_dict=all_members_dict,
                team_dto=team_dto
            )
            teams_details_dict_list.append(teams_details_dict)
        return teams_details_dict_list

    def _make_single_team_details_dict(
            self,
            team_member_ids_dict,
            all_members_dict,
            team_dto
    ):
        team_members_dict_list = self._get_members_dict_list(
            members_ids=team_member_ids_dict[team_dto.team_id],
            all_members_dict=all_members_dict
        )
        team_details_dict = self._make_team_dict(
            team_dto=team_dto,
            team_members_dict_list=team_members_dict_list
        )
        return team_details_dict

    @staticmethod
    def _make_team_dict(team_dto, team_members_dict_list):
        team_details_dict = {
            "team_id": team_dto.team_id,
            "name": team_dto.name,
            "description": team_dto.description,
            "no_of_members": len(team_members_dict_list),
            "members": team_members_dict_list
        }
        return team_details_dict

    @staticmethod
    def _get_members_dict_list(members_ids, all_members_dict):
        members_dict_list = [
            all_members_dict[member_id] for member_id in members_ids
        ]
        return members_dict_list

    @staticmethod
    def _get_all_members_details_dict(members_dtos):
        from collections import defaultdict
        members_dict = defaultdict()
        for member_dto in members_dtos:
            members_dict[member_dto.member_id] = {
                "member_id": member_dto.member_id,
                "name": member_dto.name,
                "profile_pic_url": member_dto.profile_pic_url
            }
        return members_dict

    @staticmethod
    def get_team_members_dict_from_team_member_ids_dtos(
            team_member_ids_dtos
    ):
        from collections import defaultdict
        team_member_ids_dict = defaultdict(list)
        for team_member_ids_dto in team_member_ids_dtos:
            team_member_ids_dict[
                team_member_ids_dto.team_id
            ] = team_member_ids_dto.member_ids
        return team_member_ids_dict
