from abc import abstractmethod
from typing import List, Optional
from ib_iam.interactors.storage_interfaces.dtos import (
    PaginationDTO, BasicTeamDTO, TeamMembersDTO, AddTeamParametersDTO
)


class TeamStorageInterface:

    @abstractmethod
    def is_user_admin(self, user_id: str):
        pass

    @abstractmethod
    def get_team_dtos_created_by_user(
            self, user_id: str, pagination_dto: PaginationDTO
    ) -> List[BasicTeamDTO]:
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
