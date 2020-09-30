import abc
from typing import List, Optional

from ib_iam.exceptions.custom_exceptions import InvalidTeamId, \
    UsersNotBelongToGivenLevelHierarchy, InvalidLevelHierarchyOfTeam, \
    UserNotBelongToTeam
from ib_iam.interactors.dtos.dtos import TeamMemberLevelDTO, \
    TeamMemberLevelIdWithMemberIdsDTO, ImmediateSuperiorUserIdWithUserIdsDTO
from ib_iam.interactors.storage_interfaces.dtos import \
    TeamMemberLevelDetailsDTO, MemberDTO, MemberIdWithSubordinateMemberIdsDTO, \
    MemberLevelAndHierarchyDTO


class TeamMemberLevelStorageInterface(abc.ABC):

    @abc.abstractmethod
    def add_team_member_levels(
            self, team_id: str,
            team_member_level_dtos: List[TeamMemberLevelDTO]):
        pass

    @abc.abstractmethod
    def get_team_member_level_details_dtos(self, team_id: str) -> \
            List[TeamMemberLevelDetailsDTO]:
        pass

    @abc.abstractmethod
    def add_members_to_levels_for_a_team(
            self,
            team_member_level_id_with_member_ids_dtos: List[
                TeamMemberLevelIdWithMemberIdsDTO]
    ):
        pass

    @abc.abstractmethod
    def get_member_details(self, team_id: str, level_hierarchy: int) \
            -> List[MemberDTO]:
        pass

    @abc.abstractmethod
    def add_members_to_superiors(
            self, team_id: str, member_level_hierarchy: int,
            immediate_superior_user_id_with_member_ids_dtos: List[
                ImmediateSuperiorUserIdWithUserIdsDTO]
    ):
        pass

    @abc.abstractmethod
    def get_immediate_superior_user_id(self, team_id: str,
                                       user_id: str) -> str:
        pass

    @abc.abstractmethod
    def get_member_id_with_subordinate_member_ids_dtos(
            self, team_id: str, member_ids: List[str]
    ) -> List[MemberIdWithSubordinateMemberIdsDTO]:
        pass

    @abc.abstractmethod
    def validate_team_id(self, team_id: str) -> Optional[InvalidTeamId]:
        pass

    @abc.abstractmethod
    def get_team_member_level_ids(self, team_id: str) -> List[str]:
        pass

    @abc.abstractmethod
    def get_team_member_ids(self, team_id: str) -> List[str]:
        pass

    @abc.abstractmethod
    def validate_level_hierarchy_of_team(
            self, team_id: str, level_hierarchy: int
    ) -> Optional[InvalidLevelHierarchyOfTeam]:
        pass

    @abc.abstractmethod
    def validate_users_belong_to_given_level_hierarchy_in_a_team(
            self, team_id: str, user_ids: List[str], level_hierarchy: int
    ) -> [UsersNotBelongToGivenLevelHierarchy, InvalidLevelHierarchyOfTeam]:
        pass

    @abc.abstractmethod
    def validate_user_in_a_team(self, team_id: str, user_id: str) \
            -> Optional[UserNotBelongToTeam]:
        pass

    @abc.abstractmethod
    def get_team_member_level_id_and_hierarchy(
            self, team_id: str
    ) -> List[MemberLevelAndHierarchyDTO]:
        pass

    @abc.abstractmethod
    def get_or_create_team_member_level_hierarchy(
            self, team_id: str, level_hierarchy: int, level_name: str
    ) -> str:
        pass

    @abc.abstractmethod
    def get_user_id_with_subordinate_user_ids_dto(self, user_id: str,
                                                  project_id: str) \
            -> MemberIdWithSubordinateMemberIdsDTO:
        pass

    @abc.abstractmethod
    def is_user_in_a_least_level(self, user_id: str, project_id: str) -> bool:
        pass
