from typing import List

from django_swagger_utils.utils.http_response_mixin import HTTPResponseMixin

from ib_iam.constants.enums import StatusCode
from ib_iam.interactors.dtos.dtos import CompleteTeamMemberLevelsDetailsDTO
from ib_iam.interactors.presenter_interfaces.level_presenter_interface import \
    GetTeamMemberLevelsWithMembersPresenterInterface
from ib_iam.interactors.storage_interfaces.dtos import \
    MemberIdWithSubordinateMemberIdsDTO, TeamMemberLevelDetailsDTO

INVALID_TEAM_ID = (
    "Please send valid team id to get team member levels with members",
    "INVALID_TEAM_ID"
)

USER_DOES_NOT_HAVE_ACCESS = (
    "User does not have provision to access",
    "USER_DOES_NOT_HAVE_ACCESS"
)


class GetTeamMemberLevelsWithMembersPresenterImplementation(
    GetTeamMemberLevelsWithMembersPresenterInterface, HTTPResponseMixin
):

    def prepare_success_response_for_team_member_levels_with_members(
            self,
            complete_team_member_levels_details_dto: CompleteTeamMemberLevelsDetailsDTO
    ):
        (member_id_wise_member_dto_dict,
         member_id_wise_subordinate_member_ids_dict,
         team_member_id_wise_team_member_level_details_dict,
         user_id_wise_user_profile_dto_dict) = \
            self._get_id_wise_details_for_each_in_complete_team_member_levels_details_dto(
                complete_team_member_levels_details_dto)

        team_member_level_id_with_member_ids_dtos = \
            complete_team_member_levels_details_dto.team_member_level_id_with_member_ids_dtos
        team_member_levels_with_members = []
        for team_member_level_id_with_member_ids_dto in team_member_level_id_with_member_ids_dtos:
            team_member_level_details_dict = {
                "level_details":
                    team_member_id_wise_team_member_level_details_dict[
                        team_member_level_id_with_member_ids_dto.team_member_level_id
                    ],
                "level_members": self._prepare_members_details_list(
                    member_ids=team_member_level_id_with_member_ids_dto.member_ids,
                    user_id_wise_user_profile_dto_dict=user_id_wise_user_profile_dto_dict,
                    member_id_wise_member_dto_dict=member_id_wise_member_dto_dict,
                    member_id_wise_subordinate_member_ids_dict=member_id_wise_subordinate_member_ids_dict
                )
            }
            team_member_levels_with_members.append(
                team_member_level_details_dict)
        response_dict = {
            "team_member_levels_with_members": team_member_levels_with_members
        }
        return self.prepare_200_success_response(response_dict=response_dict)

    def _get_id_wise_details_for_each_in_complete_team_member_levels_details_dto(
            self,
            complete_team_member_levels_details_dto: CompleteTeamMemberLevelsDetailsDTO
    ):
        member_dtos = complete_team_member_levels_details_dto.member_dtos
        user_profile_dtos = \
            complete_team_member_levels_details_dto.user_profile_dtos
        from ib_iam.presenters.get_team_members_of_level_hierarchy_presenter_implementation import \
            GetTeamMembersOfLevelHierarchyPresenterImplementation
        presenter = GetTeamMembersOfLevelHierarchyPresenterImplementation()
        user_id_wise_user_profile_dto_dict = \
            presenter.prepare_user_id_wise_user_profile_dto_dict(
                user_profile_dtos=user_profile_dtos)
        member_id_wise_member_dto_dict = \
            presenter.prepare_member_id_wise_member_dto_dict(
                member_dtos=member_dtos
            )
        team_member_level_details_dtos = \
            complete_team_member_levels_details_dto.team_member_level_details_dtos
        team_member_id_wise_team_member_level_details_dict = \
            self._prepare_team_member_id_wise_team_member_level_details_dict(
                team_member_level_details_dtos=team_member_level_details_dtos
            )
        member_id_with_subordinate_member_ids_dtos = \
            complete_team_member_levels_details_dto.member_id_with_subordinate_member_ids_dtos
        member_id_wise_subordinate_member_ids_dict = \
            self._prepare_member_id_wise_subordinate_member_ids_dict(
                member_id_with_subordinate_member_ids_dtos=member_id_with_subordinate_member_ids_dtos
            )
        return (
            member_id_wise_member_dto_dict,
            member_id_wise_subordinate_member_ids_dict,
            team_member_id_wise_team_member_level_details_dict,
            user_id_wise_user_profile_dto_dict
        )

    @staticmethod
    def _prepare_member_id_wise_subordinate_member_ids_dict(
            member_id_with_subordinate_member_ids_dtos: List[
                MemberIdWithSubordinateMemberIdsDTO]
    ):
        member_id_wise_subordinate_member_ids_dict = {
            member_id_with_subordinate_member_ids_dto.member_id:
                member_id_with_subordinate_member_ids_dto.subordinate_member_ids
            for member_id_with_subordinate_member_ids_dto in
            member_id_with_subordinate_member_ids_dtos
        }
        return member_id_wise_subordinate_member_ids_dict

    @staticmethod
    def _prepare_team_member_id_wise_team_member_level_details_dict(
            team_member_level_details_dtos: List[TeamMemberLevelDetailsDTO]
    ):
        team_member_id_wise_team_member_level_details_dict = {
            team_member_level_details_dto.team_member_level_id: {
                "team_member_level_id": team_member_level_details_dto.team_member_level_id,
                "team_member_level_name": team_member_level_details_dto.team_member_level_name,
                "level_hierarchy": team_member_level_details_dto.level_hierarchy
            }
            for team_member_level_details_dto in team_member_level_details_dtos
        }
        return team_member_id_wise_team_member_level_details_dict

    def _prepare_members_details_list(
            self, member_ids, user_id_wise_user_profile_dto_dict,
            member_id_wise_member_dto_dict,
            member_id_wise_subordinate_member_ids_dict
    ):
        member_details_list = []
        for member_id in member_ids:
            subordinate_member_ids = \
                member_id_wise_subordinate_member_ids_dict[
                    member_id]
            member_details_dict = {
                "member_id": member_id,
                "immediate_superior_team_user_id":
                    member_id_wise_member_dto_dict[
                        member_id].immediate_superior_team_user_id,
                "name": user_id_wise_user_profile_dto_dict[member_id].name,
                "profile_pic_url": user_id_wise_user_profile_dto_dict[
                    member_id].profile_pic_url,
                "immediate_subordinate_team_members":
                    self._prepare_subordinate_members_details_list(
                        subordinate_member_ids=subordinate_member_ids,
                        user_id_wise_user_profile_dto_dict=user_id_wise_user_profile_dto_dict
                    )
            }
            member_details_list.append(member_details_dict)
        return member_details_list

    @staticmethod
    def _prepare_subordinate_members_details_list(
            subordinate_member_ids,
            user_id_wise_user_profile_dto_dict,
    ):
        subordinate_members_details_list = [
            {
                "member_id": subordinate_member_id,
                "name": user_id_wise_user_profile_dto_dict[
                    subordinate_member_id].name,
                "profile_pic_url": user_id_wise_user_profile_dto_dict[
                    subordinate_member_id].profile_pic_url,
            }
            for subordinate_member_id in subordinate_member_ids
        ]
        return subordinate_members_details_list

    def response_for_invalid_team_id(self):
        response_dict = {
            "response": INVALID_TEAM_ID[0],
            "http_status_code": StatusCode.BAD_REQUEST.value,
            "res_status": INVALID_TEAM_ID[1]
        }
        return self.prepare_400_bad_request_response(
            response_dict=response_dict
        )

    def response_for_user_is_not_admin(self):
        response_dict = {
            "response": USER_DOES_NOT_HAVE_ACCESS[0],
            "http_status_code": StatusCode.FORBIDDEN.value,
            "res_status": USER_DOES_NOT_HAVE_ACCESS[1]
        }
        return self.prepare_403_forbidden_response(
            response_dict=response_dict
        )
