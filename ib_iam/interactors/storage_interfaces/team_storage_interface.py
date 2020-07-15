from abc import abstractmethod
from typing import List
from ib_iam.interactors.storage_interfaces.dtos import (
    PaginationDTO, BasicTeamDTO, TeamMembersDTO
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
