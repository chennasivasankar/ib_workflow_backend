from abc import ABC, abstractmethod
from typing import List


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
    def change_company_for_user(self, company_id: str, user_id: str):
        pass

    @abstractmethod
    def add_new_user(self, user_id: str, is_admin: bool, company_id: str,
                     role_ids, team_ids: List[str]):
        pass
