from abc import ABC
from abc import abstractmethod
from typing import List, Optional
from ib_iam.interactors.storage_interfaces.dtos import (
    PaginationDTO, TeamMemberIdsDTO,
    TeamsWithTotalTeamsCountDTO, TeamDetailsWithUserIdsDTO,
    TeamWithUserIdsDTO
)


class TeamStorageInterface(ABC):

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
    def get_valid_user_ids_among_the_given_user_ids(
            self, user_ids: List[str]
    ) -> List[str]:
        pass

    @abstractmethod
    def add_team(
            self,
            user_id: str,
            team_details_with_user_ids_dto: TeamDetailsWithUserIdsDTO
    ) -> str:
        pass

    @abstractmethod
    def add_users_to_team(self, team_id: str, user_ids: List[str]):
        pass

    @abstractmethod
    def raise_exception_if_team_not_exists(self, team_id: str):
        pass

    @abstractmethod
    def update_team_details(
            self, team_with_user_ids_dto: TeamWithUserIdsDTO
    ):
        pass

    @abstractmethod
    def get_member_ids_of_team(self, team_id: str):
        pass

    @abstractmethod
    def delete_members_from_team(self, team_id: str, member_ids: List[str]):
        pass

    @abstractmethod
    def delete_team(self, team_id: str):
        pass
