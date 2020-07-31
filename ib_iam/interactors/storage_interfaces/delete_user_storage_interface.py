from abc import ABC, abstractmethod

from ib_iam.interactors.storage_interfaces.dtos import UserDTO


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

    @abstractmethod
    def check_is_admin_user(self, user_id: str) -> bool:
        pass

    @abstractmethod
    def get_user_details(self, user_id: str) -> UserDTO:
        pass
