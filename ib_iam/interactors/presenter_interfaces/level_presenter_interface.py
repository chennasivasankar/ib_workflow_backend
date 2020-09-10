import abc
from typing import List

from ib_iam.adapters.dtos import UserProfileDTO
from ib_iam.interactors.dtos.dtos import CompleteTeamMemberLevelsDetailsDTO
from ib_iam.interactors.storage_interfaces.dtos import \
    TeamMemberLevelDetailsDTO, MemberDTO


class AddTeamMemberLevelsPresenterInterface(abc.ABC):

    @abc.abstractmethod
    def prepare_success_response_for_add_team_member_levels_to_team(self):
        pass


class GetTeamMemberLevelsPresenterInterface(abc.ABC):

    @abc.abstractmethod
    def response_for_team_member_level_details_dtos(
            self,
            team_member_level_details_dtos: List[TeamMemberLevelDetailsDTO]):
        pass


class AddMembersToLevelPresenterInterface(abc.ABC):

    @abc.abstractmethod
    def prepare_success_response_for_add_members_to_levels(self):
        pass


class GetTeamMembersOfLevelHierarchyPresenterInterface(abc.ABC):

    @abc.abstractmethod
    def prepare_success_response_for_get_team_members_of_level_hierarchy(
            self, member_dtos: List[MemberDTO],
            user_profile_dtos: List[UserProfileDTO]
    ):
        pass


class AddMembersToSuperiorsPresenterInterface(abc.ABC):

    @abc.abstractmethod
    def prepare_success_response_for_add_members_superiors(self):
        pass


class GetTeamMemberLevelsWithMembersPresenterInterface(abc.ABC):

    @abc.abstractmethod
    def prepare_success_response_for_team_member_levels_with_members(
            self,
            complete_team_member_levels_details_dto: CompleteTeamMemberLevelsDetailsDTO
    ):
        pass
