from abc import ABC, abstractmethod


class DeleteUserStorageInterface(ABC):
    @abstractmethod
    def delete_user(self, user_id: str):
        pass

    @abstractmethod
    def delete_user_roles(self, user_id: str):
        pass

    @abstractmethod
    def delete_user_teams(self, user_id: str):
        pass
