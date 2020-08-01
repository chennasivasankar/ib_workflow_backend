from abc import ABC, abstractmethod
from typing import List, Optional

from ib_iam.exceptions.custom_exceptions import InvalidUserId, InvalidUserIds
from ib_iam.interactors.storage_interfaces.dtos import UserDTO, UserTeamDTO, \
    UserRoleDTO, UserCompanyDTO, CompanyIdAndNameDTO, TeamIdAndNameDTO, \
    RoleIdAndNameDTO, UserIdAndNameDTO


class UserStorageInterface(ABC):
    @abstractmethod
    def check_is_admin_user(self, user_id: str) -> bool:
        pass

    @abstractmethod
    def is_user_exist(self, user_id: str) -> bool:
        pass

    @abstractmethod
    def get_role_objs_ids(self, roles):
        pass

    @abstractmethod
    def check_are_valid_role_ids(self, role_ids) -> bool:
        pass

    @abstractmethod
    def check_is_exists_company_id(self, company_id) -> bool:
        pass

    @abstractmethod
    def check_are_valid_team_ids(self, team_ids) -> bool:
        pass

    @abstractmethod
    def remove_roles_for_user(self, user_id: str):
        pass

    @abstractmethod
    def remove_teams_for_user(self, user_id: str):
        pass

    @abstractmethod
    def add_roles_to_the_user(self, user_id: str, role_ids: List[str]):
        pass

    @abstractmethod
    def add_user_to_the_teams(self, user_id: str, team_ids: List[str]):
        pass

    @abstractmethod
    def update_user_details(self, company_id: str, user_id: str, name: str):
        pass

    @abstractmethod
    def add_new_user(self, user_id: str, is_admin: bool, company_id: str,
                     role_ids, team_ids: List[str], name: str):
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
    def get_companies(self) -> List[CompanyIdAndNameDTO]:
        pass

    @abstractmethod
    def get_teams(self) -> List[TeamIdAndNameDTO]:
        pass

    @abstractmethod
    def get_roles(self) -> List[RoleIdAndNameDTO]:
        pass

    @abstractmethod
    def validate_user_id(self, user_id) -> Optional[InvalidUserId]:
        pass

    @abstractmethod
    def validate_user_ids(self, user_ids: List[str]) \
            -> Optional[InvalidUserIds]:
        pass

    @abstractmethod
    def get_valid_user_ids(self, user_ids: List[str]) -> List[str]:
        pass

    @abstractmethod
    def get_user_details_dtos_based_on_limit_offset_and_search_query(
            self, limit: int, offset: int, search_query: str
    ) -> List[UserIdAndNameDTO]:
        pass

    @abstractmethod
    def get_user_details_dtos_based_on_search_query(
            self, search_query: str
    ) -> List[UserIdAndNameDTO]:
        pass
