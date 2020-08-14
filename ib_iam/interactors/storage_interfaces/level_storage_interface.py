from abc import ABC, abstractmethod
from typing import List

from ib_iam.interactors.dtos.dtos import TeamMemberLevelDTO, \
    TeamMemberLevelIdWithMemberIdsDTO
from ib_iam.interactors.storage_interfaces.dtos import TeamMemberLevelDetailsDTO


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
