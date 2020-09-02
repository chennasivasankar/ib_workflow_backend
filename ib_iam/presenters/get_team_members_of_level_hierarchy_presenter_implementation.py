from typing import List

from django_swagger_utils.utils.http_response_mixin import HTTPResponseMixin

from ib_iam.adapters.dtos import UserProfileDTO
from ib_iam.constants.enums import StatusCode
from ib_iam.interactors.presenter_interfaces.level_presenter_interface import \
    GetTeamMembersOfLevelHierarchyPresenterInterface
from ib_iam.interactors.storage_interfaces.dtos import MemberDTO

INVALID_TEAM_ID = (
    "Please send valid team id to get team members of level hierarchy",
    "INVALID_TEAM_ID"
)

INVALID_LEVEL_HIERARCHY = (
    "Please send valid level hierarchy to get team members of level hierarchy",
    "INVALID_LEVEL_HIERARCHY"
)


class GetTeamMembersOfLevelHierarchyPresenterImplementation(
    GetTeamMembersOfLevelHierarchyPresenterInterface, HTTPResponseMixin
):

    def prepare_success_response_for_get_team_members_of_level_hierarchy(
            self, member_dtos: List[MemberDTO],
            user_profile_dtos: List[UserProfileDTO]
    ):
        user_id_wise_user_profile_dto_dict = \
            self.prepare_user_id_wise_user_profile_dto_dict(
                user_profile_dtos=user_profile_dtos)
        member_id_wise_member_dto_dict = self.prepare_member_id_wise_member_dto_dict(
            member_dtos=member_dtos)

        members = [
            {
                "member_id": member_dto.member_id,
                "immediate_superior_team_user_id":
                    member_id_wise_member_dto_dict[
                        member_dto.member_id].immediate_superior_team_user_id,
                "name": user_id_wise_user_profile_dto_dict[
                    member_dto.member_id].name,
                "profile_pic_url": user_id_wise_user_profile_dto_dict[
                    member_dto.member_id].profile_pic_url
            }
            for member_dto in member_dtos
        ]
        response_dict = {"members": members}
        return self.prepare_200_success_response(response_dict=response_dict)

    @staticmethod
    def prepare_member_id_wise_member_dto_dict(member_dtos: List[MemberDTO]):
        member_id_wise_member_dict = {
            member_dto.member_id: member_dto
            for member_dto in member_dtos
        }
        return member_id_wise_member_dict

    @staticmethod
    def prepare_user_id_wise_user_profile_dto_dict(
            user_profile_dtos: List[UserProfileDTO]):
        user_id_wise_user_profile_dict = {
            user_profile_dto.user_id: user_profile_dto
            for user_profile_dto in user_profile_dtos
        }
        return user_id_wise_user_profile_dict

    def response_for_invalid_team_id(self):
        response_dict = {
            "response": INVALID_TEAM_ID[0],
            "http_status_code": StatusCode.BAD_REQUEST.value,
            "res_status": INVALID_TEAM_ID[1]
        }
        return self.prepare_400_bad_request_response(
            response_dict=response_dict)

    def response_for_invalid_level_hierarchy_of_team(self):
        response_dict = {
            "response": INVALID_LEVEL_HIERARCHY[0],
            "http_status_code": StatusCode.BAD_REQUEST.value,
            "res_status": INVALID_LEVEL_HIERARCHY[1]
        }
        return self.prepare_400_bad_request_response(
            response_dict=response_dict)
