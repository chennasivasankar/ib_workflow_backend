from abc import ABC, abstractmethod
from typing import List


class AddNewUserStorageInterface(ABC):
    @abstractmethod
    def check_is_admin_user(self, user_id: str) -> bool:
        pass

    @abstractmethod
    def get_role_objs_ids(self, roles):
        pass

    @abstractmethod
    def add_new_user(self, user_id: str, is_admin: bool, company_id: str,
                     role_ids, team_ids: List[str]):
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
