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

    @abc.abstractmethod
    def response_for_invalid_team_id(self):
        pass

    @abc.abstractmethod
    def response_for_duplicate_level_hierarchies(self, err):
        pass

    @abc.abstractmethod
    def response_for_negative_level_hierarchies(self, err):
        pass

    @abc.abstractmethod
    def response_for_duplicate_team_member_level_names(self, err):
        pass

    @abc.abstractmethod
    def response_for_user_is_not_admin(self):
        pass


class GetTeamMemberLevelsPresenterInterface(abc.ABC):

    @abc.abstractmethod
    def response_for_team_member_level_details_dtos(
            self,
            team_member_level_details_dtos: List[TeamMemberLevelDetailsDTO]):
        pass

    @abc.abstractmethod
    def response_for_invalid_team_id(self):
        pass

    @abc.abstractmethod
    def response_for_user_is_not_admin(self):
        pass


class AddMembersToTeamMemberLevelsPresenterInterface(abc.ABC):

    @abc.abstractmethod
    def prepare_success_response_for_add_members_to_team_member_levels(self):
        pass

    @abc.abstractmethod
    def response_for_invalid_team_id(self):
        pass

    @abc.abstractmethod
    def response_for_team_member_level_ids_not_found(self, err):
        pass

    @abc.abstractmethod
    def response_for_team_member_ids_not_found(self, err):
        pass

    @abc.abstractmethod
    def response_for_user_is_not_admin(self):
        pass


class GetTeamMembersOfLevelHierarchyPresenterInterface(abc.ABC):

    @abc.abstractmethod
    def prepare_success_response_for_get_team_members_of_level_hierarchy(
            self, member_dtos: List[MemberDTO],
            user_profile_dtos: List[UserProfileDTO]
    ):
        pass

    @abc.abstractmethod
    def response_for_invalid_team_id(self):
        pass

    @abc.abstractmethod
    def response_for_invalid_level_hierarchy_of_team(self):
        pass

    @abc.abstractmethod
    def response_for_user_is_not_admin(self):
        pass


class AddMembersToSuperiorsPresenterInterface(abc.ABC):

    @abc.abstractmethod
    def prepare_success_response_for_add_members_superiors(self):
        pass

    @abc.abstractmethod
    def response_for_invalid_team_id(self):
        pass

    @abc.abstractmethod
    def response_for_invalid_level_hierarchy_of_team(self):
        pass

    @abc.abstractmethod
    def response_for_team_member_ids_not_found(self, err):
        pass

    @abc.abstractmethod
    def response_for_users_not_belong_to_team_member_level(self, err):
        pass

    @abc.abstractmethod
    def response_for_user_is_not_admin(self):
        pass


class GetTeamMemberLevelsWithMembersPresenterInterface(abc.ABC):

    @abc.abstractmethod
    def prepare_success_response_for_team_member_levels_with_members(
            self,
            complete_team_member_levels_details_dto: CompleteTeamMemberLevelsDetailsDTO
    ):
        pass

    @abc.abstractmethod
    def response_for_invalid_team_id(self):
        pass

    @abc.abstractmethod
    def response_for_user_is_not_admin(self):
        pass
