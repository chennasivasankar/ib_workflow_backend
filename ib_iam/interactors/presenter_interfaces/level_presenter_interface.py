from abc import ABC, abstractmethod
from typing import List

from ib_iam.adapters.dtos import UserProfileDTO
from ib_iam.interactors.dtos.dtos import CompleteTeamMemberLevelsDetailsDTO
from ib_iam.interactors.storage_interfaces.dtos import \
    TeamMemberLevelDetailsDTO, MemberDTO


class AddTeamMemberLevelsPresenterInterface(ABC):

    @abstractmethod
    def prepare_success_response_for_add_team_member_levels_to_team(self):
        pass

    @abstractmethod
    def response_for_invalid_team_id(self):
        pass

    @abstractmethod
    def response_for_duplicate_level_hierarchies(self, err):
        pass

    @abstractmethod
    def response_for_negative_level_hierarchies(self, err):
        pass


class GetTeamMemberLevelsPresenterInterface(ABC):

    @abstractmethod
    def response_for_team_member_level_details_dtos(
            self,
            team_member_level_details_dtos: List[TeamMemberLevelDetailsDTO]):
        pass


class AddMembersToLevelPresenterInterface(ABC):

    @abstractmethod
    def prepare_success_response_for_add_members_to_levels(self):
        pass


class GetTeamMembersOfLevelHierarchyPresenterInterface(ABC):

    @abstractmethod
    def prepare_success_response_for_get_team_members_of_level_hierarchy(
            self, member_dtos: List[MemberDTO],
            user_profile_dtos: List[UserProfileDTO]
    ):
        pass


class AddMembersToSuperiorsPresenterInterface(ABC):

    @abstractmethod
    def prepare_success_response_for_add_members_superiors(self):
        pass


class GetTeamMemberLevelsWithMembersPresenterInterface(ABC):

    @abstractmethod
    def prepare_success_response_for_team_member_levels_with_members(
            self,
            complete_team_member_levels_details_dto: CompleteTeamMemberLevelsDetailsDTO
    ):
        pass
