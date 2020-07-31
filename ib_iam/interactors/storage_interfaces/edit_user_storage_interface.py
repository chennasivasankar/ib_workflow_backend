from abc import ABC, abstractmethod
from typing import List


class EditUserStorageInterface(ABC):
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
    def validate_role_ids(self, role_ids):
        pass

    @abstractmethod
    def validate_company(self, company_id):
        pass

    @abstractmethod
    def validate_teams(self, team_ids):
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
    def update_user_details(self, company_id: str, user_id: str, name):
        pass
