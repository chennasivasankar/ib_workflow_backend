from typing import List

from django_swagger_utils.utils.http_response_mixin import HTTPResponseMixin

from ib_iam.adapters.dtos import UserProfileDTO
from ib_iam.interactors.presenter_interfaces.level_presenter_interface import \
    GetTeamMembersOfLevelHierarchyPresenterInterface
from ib_iam.interactors.storage_interfaces.dtos import MemberDTO


class GetTeamMembersOfLevelHierarchyPresenterImplementation(
    GetTeamMembersOfLevelHierarchyPresenterInterface, HTTPResponseMixin
):

    def prepare_success_response_for_get_team_members_of_level_hierarchy(
            self, member_dtos: List[MemberDTO],
            user_profile_dtos: List[UserProfileDTO]
    ):
        user_id_wise_user_profile_dto_dict = \
            self._prepare_user_id_wise_user_profile_dto_dict(
                user_profile_dtos=user_profile_dtos)
        member_id_wise_member_dto_dict = self._prepare_member_id_wise_member_dto_dict(
            member_dtos=member_dtos)

        members = [
            {
                "member_id": member_dto.member_id,
                "immediate_superior_team_user_id": member_id_wise_member_dto_dict[
                    member_dto.member_id].immediate_superior_team_user_id,
                "name": user_id_wise_user_profile_dto_dict[member_dto.member_id].name,
                "profile_pic_url": user_id_wise_user_profile_dto_dict[
                    member_dto.member_id].profile_pic_url
            }
            for member_dto in member_dtos
        ]
        response_dict = {"members": members}
        return self.prepare_200_success_response(response_dict=response_dict)

    @staticmethod
    def _prepare_member_id_wise_member_dto_dict(member_dtos: List[MemberDTO]):
        member_id_wise_member_dict = {
            member_dto.member_id: member_dto
            for member_dto in member_dtos
        }
        return member_id_wise_member_dict

    @staticmethod
    def _prepare_user_id_wise_user_profile_dto_dict(
            user_profile_dtos: List[UserProfileDTO]):
        user_id_wise_user_profile_dict = {
            user_profile_dto.user_id: user_profile_dto
            for user_profile_dto in user_profile_dtos
        }
        return user_id_wise_user_profile_dict
