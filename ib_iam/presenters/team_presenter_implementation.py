from django_swagger_utils.utils.http_response_mixin import HTTPResponseMixin
from ib_iam.constants.enums import StatusCode
from ib_iam.interactors.presenter_interfaces.dtos import TeamWithMembersDetailsDTO
from ib_iam.interactors.presenter_interfaces.team_presenter_interface import TeamPresenterInterface
from ib_iam.constants.exception_messages import (
    USER_HAS_NO_ACCESS, INVALID_LIMIT, INVALID_OFFSET, TEAM_NAME_ALREADY_EXISTS
)


class TeamPresenterImplementation(TeamPresenterInterface, HTTPResponseMixin):

    def raise_exception_for_user_has_no_access(self):
        response_dict = {
            "response": USER_HAS_NO_ACCESS[0],
            "http_status_code": StatusCode.UNAUTHORIZED.value,
            "res_status": USER_HAS_NO_ACCESS[1]
        }
        return self.prepare_401_unauthorized_response(
            response_dict=response_dict
        )

    def raise_exception_for_invalid_limit(self):
        response_dict = {
            "response": INVALID_LIMIT[0],
            "http_status_code": StatusCode.BAD_REQUEST.value,
            "res_status": INVALID_LIMIT[1]
        }
        return self.prepare_400_bad_request_response(
            response_dict=response_dict
        )

    def raise_exception_for_invalid_offset(self):
        response_dict = {
            "response": INVALID_OFFSET[0],
            "http_status_code": StatusCode.BAD_REQUEST.value,
            "res_status": INVALID_OFFSET[1]
        }
        return self.prepare_400_bad_request_response(
            response_dict=response_dict
        )

    def raise_exception_if_team_name_already_exists(self, exception):
        response_dict = {
            "response": TEAM_NAME_ALREADY_EXISTS[0] % exception.team_name,
            "http_status_code": StatusCode.BAD_REQUEST.value,
            "res_status": TEAM_NAME_ALREADY_EXISTS[1]
        }
        return self.prepare_400_bad_request_response(
            response_dict=response_dict
        )

    def get_response_for_get_list_of_teams(
            self, team_details_dtos: TeamWithMembersDetailsDTO
    ):
        teams = self._convert_team_details_dtos_to_teams_list(team_details_dtos=team_details_dtos)
        response_dict = {
            "total_teams_count": team_details_dtos.total_teams_count,
            "teams": teams
        }
        return self.prepare_200_success_response(
            response_dict=response_dict
        )

    def get_response_for_add_team(self, team_id: str):
        return self.prepare_201_created_response(
            response_dict={"team_id": team_id}
        )

    def _convert_team_details_dtos_to_teams_list(
            self, team_details_dtos: TeamWithMembersDetailsDTO
    ):
        team_dtos = team_details_dtos.team_dtos
        team_member_ids_dtos = team_details_dtos.team_member_ids_dtos
        member_dtos = team_details_dtos.member_dtos
        members_dictionary = self._get_members_dictionary(member_dtos=member_dtos)
        team_member_ids_dict = self._get_team_members_dict_from_team_member_ids_dtos(
            team_member_ids_dtos=team_member_ids_dtos
        )
        teams_details_dict_list = [
            self._convert_to_team_details_dictionary(
                team_member_ids_dict=team_member_ids_dict,
                members_dictionary=members_dictionary,
                team_dto=team_dto
            ) for team_dto in team_dtos
        ]
        # for team_dto in team_dtos:
        #     teams_details_dict = self._convert_to_team_details_dictionary(
        #         team_member_ids_dict=team_member_ids_dict,
        #         members_dictionary=members_dictionary,
        #         team_dto=team_dto
        #     )
        #     teams_details_dict_list.append(teams_details_dict)
        return teams_details_dict_list

    def _convert_to_team_details_dictionary(
            self,
            team_member_ids_dict,
            members_dictionary,
            team_dto
    ):
        team_members_dict_list = self._get_members(
            members_ids=team_member_ids_dict[team_dto.team_id],
            members_dictionary=members_dictionary
        )
        team_dictionary = self._convert_to_team_dictionary(
            team_dto=team_dto,
            team_members_dict_list=team_members_dict_list
        )
        return team_dictionary

    @staticmethod
    def _convert_to_team_dictionary(team_dto, team_members_dict_list):
        team_details_dict = {
            "team_id": team_dto.team_id,
            "name": team_dto.name,
            "description": team_dto.description,
            "no_of_members": len(team_members_dict_list),
            "members": team_members_dict_list
        }
        return team_details_dict

    @staticmethod
    def _get_members(members_ids, members_dictionary):
        members_dict_list = [
            members_dictionary[member_id] for member_id in members_ids
        ]
        return members_dict_list

    @staticmethod
    def _get_members_dictionary(member_dtos):
        from collections import defaultdict
        members_dict = defaultdict()
        for member_dto in member_dtos:
            members_dict[member_dto.member_id] = {
                "member_id": member_dto.member_id,
                "name": member_dto.name,
                "profile_pic_url": member_dto.profile_pic_url
            }
        return members_dict

    @staticmethod
    def _get_team_members_dict_from_team_member_ids_dtos(
            team_member_ids_dtos
    ):
        from collections import defaultdict
        team_member_ids_dict = defaultdict(list)
        for team_member_ids_dto in team_member_ids_dtos:
            team_member_ids_dict[
                team_member_ids_dto.team_id
            ] = team_member_ids_dto.member_ids
        return team_member_ids_dict
