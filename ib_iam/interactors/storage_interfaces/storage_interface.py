from abc import ABC, abstractmethod
from typing import List


class StorageInterface(ABC):

    @abstractmethod
    def validate_user_is_admin(self, user_id: str):
        pass

    @abstractmethod
    def get_users(self):
        pass

    @abstractmethod
    def get_team_details_of_users_bulk(self, user_ids: List[str]):
        pass

    @abstractmethod
    def get_role_details_of_users_bulk(self, user_ids: List[str]):
        pass

    @abstractmethod
    def get_company_details_of_users_bulk(self, company_ids: List[str]):
        pass
