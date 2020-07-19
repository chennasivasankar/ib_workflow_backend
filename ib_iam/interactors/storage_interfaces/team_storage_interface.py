from abc import abstractmethod
from typing import List, Optional
from ib_iam.interactors.storage_interfaces.dtos import (
    PaginationDTO, TeamMemberIdsDTO, TeamNameAndDescriptionDTO,
    TeamsWithTotalTeamsCountDTO
)


class TeamStorageInterface:

    @abstractmethod
    def raise_exception_if_user_is_not_admin(self, user_id: str):
        pass

    @abstractmethod
    def get_teams_with_total_teams_count_dto(
            self, pagination_dto: PaginationDTO
    ) -> TeamsWithTotalTeamsCountDTO:
        pass

    @abstractmethod
    def get_team_member_ids_dtos(
            self, team_ids: List[str]
    ) -> List[TeamMemberIdsDTO]:
        pass

    @abstractmethod
    def is_team_name_already_exists(self, name: str) -> bool:
        pass

    @abstractmethod
    def add_team(
            self,
            user_id: str,
            team_name_and_description_dto: TeamNameAndDescriptionDTO
    ) -> str:
        pass
