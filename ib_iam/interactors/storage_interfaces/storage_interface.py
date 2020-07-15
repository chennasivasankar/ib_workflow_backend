from abc import ABC, abstractmethod


class StorageInterface(ABC):
    @abstractmethod
    def get_user_ids(self):
        pass

    @abstractmethod
    def validate_user_is_admin(self, user_id: str):
        pass

    @abstractmethod
    def get_team_details_of_users_bulk(self, user_ids):
        pass

    @abstractmethod
    def get_role_details_of_users_bulk(self, user_ids):
        pass
