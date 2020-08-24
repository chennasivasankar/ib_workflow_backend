from abc import ABC
from abc import abstractmethod
from typing import List, Optional

from ib_iam.app_interfaces.dtos import UserTeamsDTO
from ib_iam.interactors.storage_interfaces.dtos import (
    PaginationDTO, TeamUserIdsDTO, TeamsWithTotalTeamsCountDTO,
    TeamIdAndNameDTO)
from ib_iam.interactors.storage_interfaces.dtos import TeamDTO
from ib_iam.interactors.storage_interfaces.dtos import \
    TeamNameAndDescriptionDTO


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
    def delete_all_members_of_team(self, team_id: str):
        pass

    @abstractmethod
    def delete_team(self, team_id: str):
        pass

    @abstractmethod
    def get_team_id_and_name_dtos(
            self, team_ids: List[str]) -> List[TeamIdAndNameDTO]:
        pass
