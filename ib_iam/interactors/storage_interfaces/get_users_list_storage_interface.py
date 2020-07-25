from abc import ABC, abstractmethod
from typing import List

from ib_iam.interactors.storage_interfaces.dtos \
    import UserDTO, UserTeamDTO, UserRoleDTO, UserCompanyDTO


class GetUsersListStorageInterface(ABC):
    @abstractmethod
    def check_is_admin_user(self, user_id: str) -> bool:
        pass

    @abstractmethod
    def get_users_who_are_not_admins(self, offset: int, limit: int) -> List[
        UserDTO]:
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

    @abstractmethod
    def get_total_count_of_users_for_query(self):
        pass

    @abstractmethod
    def get_user_details_dtos_based_on_limit_offset_and_search_query(
            self, limit: int, offset: int, search_query: str
    ):
        pass
