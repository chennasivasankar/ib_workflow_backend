from abc import ABC, abstractmethod
from typing import List, Optional

from ib_iam.interactors.storage_interfaces.dtos import (
    PaginationDTO, TeamUserIdsDTO, TeamsWithTotalTeamsCountDTO, TeamDTO,
    TeamNameAndDescriptionDTO, TeamIdAndNameDTO)


class TeamStorageInterface(ABC):

    @abstractmethod
    def get_teams_with_total_teams_count_dto(
            self, pagination_dto: PaginationDTO
    ) -> TeamsWithTotalTeamsCountDTO:
        pass

    @abstractmethod
    def get_team_user_ids_dtos(
            self, team_ids: List[str]) -> List[TeamUserIdsDTO]:
        pass

    @abstractmethod
    def get_team_id_if_team_name_already_exists(
            self, name: str) -> Optional[str]:
        pass

    @abstractmethod
    def add_team(
            self, user_id: str,
            team_name_and_description_dto: TeamNameAndDescriptionDTO) -> str:
        pass

    @abstractmethod
    def add_users_to_team(self, team_id: str, user_ids: List[str]):
        pass

    @abstractmethod
    def raise_exception_if_team_not_exists(self, team_id: str):
        pass

    @abstractmethod
    def update_team_details(self, team_dto: TeamDTO):
        pass

    @abstractmethod
    def get_member_ids_of_team(self, team_id: str):
        pass

    @abstractmethod
    def delete_members_from_team(self, team_id: str, user_ids: List[str]):
        pass

    @abstractmethod
    def delete_team(self, team_id: str):
        pass

    @abstractmethod
    def get_team_dtos(self, team_ids: List[str]) -> List[TeamDTO]:
        pass

    @abstractmethod
    def get_valid_team_ids(self, team_ids: List[str]) -> List[str]:
        pass

    @abstractmethod
    def get_team_id_and_name_dtos(
            self, team_ids: List[str]) -> List[TeamIdAndNameDTO]:
        pass
