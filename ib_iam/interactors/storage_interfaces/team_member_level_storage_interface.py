from abc import ABC, abstractmethod
from typing import List

from ib_iam.interactors.dtos.dtos import TeamMemberLevelDTO, \
    TeamMemberLevelIdWithMemberIdsDTO, ImmediateSuperiorUserIdWithUserIdsDTO
from ib_iam.interactors.storage_interfaces.dtos import \
    TeamMemberLevelDetailsDTO, MemberDTO, MemberIdWithSubordinateMemberIdsDTO


class TeamMemberLevelStorageInterface(ABC):

    @abstractmethod
    def add_team_member_levels(
            self, team_id: str,
            team_member_level_dtos: List[TeamMemberLevelDTO]):
        pass

    @abstractmethod
    def get_team_member_level_details_dtos(self, team_id: str) -> \
            List[TeamMemberLevelDetailsDTO]:
        pass

    @abstractmethod
    def add_members_to_levels_for_a_team(
            self,
            team_member_level_id_with_member_ids_dtos: List[
                TeamMemberLevelIdWithMemberIdsDTO]
    ):
        pass

    @abstractmethod
    def get_member_details(self, team_id: str, level_hierarchy: int) \
            -> List[MemberDTO]:
        pass

    @abstractmethod
    def add_members_to_superiors(
            self, team_id: str, member_level_hierarchy: int,
            immediate_superior_user_id_with_member_ids_dtos: List[
                ImmediateSuperiorUserIdWithUserIdsDTO]
    ):
        pass

    @abstractmethod
    def get_immediate_superior_user_id(self, team_id: str, user_id: str) -> str:
        pass

    @abstractmethod
    def get_member_id_with_subordinate_member_ids_dtos(
            self, team_id: str, member_ids: List[str]
    ) -> List[MemberIdWithSubordinateMemberIdsDTO]:
        pass
