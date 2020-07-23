from abc import ABC, abstractmethod
from typing import List, Optional

from ib_iam.exceptions.custom_exceptions import InvalidUserId, InvalidUserIds
from ib_iam.interactors.storage_interfaces.dtos \
    import UserTeamDTO, UserRoleDTO, UserCompanyDTO, UserDTO, CompanyDTO, \
    TeamDTO, RoleIdAndNameDTO, RoleDTO


class StorageInterface(ABC):

    @abstractmethod
    def check_is_admin_user(self, user_id: str) -> bool:
        pass

    @abstractmethod
    def get_users_who_are_not_admins(
            self, offset=0, limit=10) -> List[UserDTO]:
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
    def add_new_user(self, user_id: str, is_admin: bool, company_id: str,
                     role_ids: List[int], team_ids: List[str]):
        pass

    @abstractmethod
    def get_companies(self) -> List[CompanyDTO]:
        pass

    @abstractmethod
    def get_teams(self) -> List[TeamDTO]:
        pass

    @abstractmethod
    def get_roles(self) -> List[RoleIdAndNameDTO]:
        pass

    @abstractmethod
    def validate_role_ids(self, role_ids):
        pass

    @abstractmethod
    def validate_company(self, company_id):
        pass

    @abstractmethod
    def validate_teams(self, team_ids):
        pass

    @abstractmethod
    def create_roles(self, role_dtos: List[RoleDTO]):
        pass

    @abstractmethod
    def get_valid_role_ids(self, role_ids: List[str]):
        pass

    @abstractmethod
    def get_role_objs_ids(self, roles):
        pass

    @abstractmethod
    def get_is_admin_of_given_user_id(self, user_id: str):
        pass

    @abstractmethod
    def validate_user_id(self, user_id) -> Optional[InvalidUserId]:
        pass

    @abstractmethod
    def get_user_role_ids(self, user_id: str):
        pass

    @abstractmethod
    def validate_user_ids(self, user_ids: List[str]) \
            -> Optional[InvalidUserIds]:
        pass

    @abstractmethod
    def get_user_id_with_role_ids_dtos(self, user_ids: List[str]):
        pass
