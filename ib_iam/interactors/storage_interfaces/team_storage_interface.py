from abc import ABC
from abc import abstractmethod
from typing import List, Optional
from ib_iam.interactors.storage_interfaces.dtos import (
    PaginationDTO, BasicTeamDTO, TeamMembersDTO, AddTeamParametersDTO, UpdateTeamParametersDTO
)


class TeamStorageInterface(ABC):

    @abstractmethod
    def is_user_admin(self, user_id: str):
        pass

    @abstractmethod
    def get_team_dtos_along_with_count(
            self, user_id: str, pagination_dto: PaginationDTO
    ) -> (List[BasicTeamDTO], int):
        pass

    @abstractmethod
    def get_team_member_ids_dtos(
            self, team_ids: List[str]
    ) -> List[TeamMembersDTO]:
        pass

    @abstractmethod
    def add_team(
            self, user_id: str, add_team_params_dto: AddTeamParametersDTO
    ) -> Optional[str]:
        pass

    @abstractmethod
    def is_valid_team(self, team_id: str):
        pass

    @abstractmethod
    def is_duplicate_team_name(self, team_id: str, name: str):
        pass

    @abstractmethod
    def update_team_details(
            self, update_team_parameters_dto: UpdateTeamParametersDTO
    ):
        pass

    @abstractmethod
    def delete_team(self, team_id: str):
        pass
