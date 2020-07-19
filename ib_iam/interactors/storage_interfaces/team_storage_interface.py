from abc import abstractmethod
from typing import List, Optional
from ib_iam.interactors.storage_interfaces.dtos import (
    PaginationDTO, TeamMemberIdsDTO,
    TeamsWithTotalTeamsCountDTO, AddTeamParametersDTO
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
    def get_team_id_if_team_name_already_exists(
            self, name: str
    ) -> Optional[str]:
        pass

    @abstractmethod
    def get_valid_member_ids_among_the_given_member_ids(
            self, member_ids: List[str]
    ) -> List[str]:
        pass

    @abstractmethod
    def add_team(
            self,
            user_id: str,
            add_team_parameters_dto: AddTeamParametersDTO
    ) -> str:
        pass

    @abstractmethod
    def add_members_to_team(self, team_id: str, member_ids: List[str]):
        pass
