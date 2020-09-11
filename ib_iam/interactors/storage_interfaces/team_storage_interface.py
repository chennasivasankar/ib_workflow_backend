import abc
from typing import List, Optional

from ib_iam.interactors.storage_interfaces.dtos import (
    PaginationDTO, TeamUserIdsDTO, TeamsWithTotalTeamsCountDTO, TeamDTO,
    TeamNameAndDescriptionDTO, TeamIdAndNameDTO, TeamWithUserIdDTO)


class TeamStorageInterface(abc.ABC):

    @abc.abstractmethod
    def get_teams_with_total_teams_count_dto(
            self, pagination_dto: PaginationDTO
    ) -> TeamsWithTotalTeamsCountDTO:
        pass

    @abc.abstractmethod
    def get_team_user_ids_dtos(
            self, team_ids: List[str]) -> List[TeamUserIdsDTO]:
        pass

    @abc.abstractmethod
    def get_team_id_if_team_name_already_exists(
            self, name: str) -> Optional[str]:
        pass

    @abc.abstractmethod
    def add_team(
            self, user_id: str,
            team_name_and_description_dto: TeamNameAndDescriptionDTO) -> str:
        pass

    @abc.abstractmethod
    def add_users_to_team(self, team_id: str, user_ids: List[str]):
        pass

    @abc.abstractmethod
    def raise_exception_if_team_not_exists(self, team_id: str):
        pass

    @abc.abstractmethod
    def update_team_details(self, team_dto: TeamDTO):
        pass

    @abc.abstractmethod
    def get_member_ids_of_team(self, team_id: str) -> List[str]:
        pass

    @abc.abstractmethod
    def delete_members_from_team(self, team_id: str, user_ids: List[str]):
        pass

    @abc.abstractmethod
    def delete_team(self, team_id: str):
        pass

    @abc.abstractmethod
    def get_team_dtos(self, team_ids: List[str]) -> List[TeamDTO]:
        pass

    @abc.abstractmethod
    def get_valid_team_ids(self, team_ids: List[str]) -> List[str]:
        pass

    @abc.abstractmethod
    def get_team_id_and_name_dtos(
            self, team_ids: List[str]) -> List[TeamIdAndNameDTO]:
        pass

    @abc.abstractmethod
    def get_team_user_dtos(
            self, user_ids: List[str], team_ids: List[str]
    ) -> List[TeamWithUserIdDTO]:
        pass
