from abc import ABC, abstractmethod
from typing import List

from ib_iam.interactors.storage_interfaces.dtos \
    import UserTeamDTO, UserRoleDTO, UserCompanyDTO


class StorageInterface(ABC):

    @abstractmethod
    def validate_user_is_admin(self, user_id: str) -> bool:
        pass

    @abstractmethod
    def get_users_who_are_not_admins(self, offset: int, limit: int):
        pass

    @abstractmethod
    def get_team_details_of_users_bulk(
            self, user_ids: List[str]) -> List[UserTeamDTO]:
        pass

    @abstractmethod
    def get_role_details_of_users_bulk(
            self, user_ids: List[str]) -> List[UserRoleDTO]:
        pass

    @abstractmethod
    def get_company_details_of_users_bulk(
            self, user_ids: List[str]) -> List[UserCompanyDTO]:
        pass
