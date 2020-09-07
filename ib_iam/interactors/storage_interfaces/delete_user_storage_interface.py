import abc

from ib_iam.interactors.storage_interfaces.dtos import UserDTO


class DeleteUserStorageInterface(abc.ABC):
    @abc.abstractmethod
    def delete_user(self, user_id: str):
        pass

    @abc.abstractmethod
    def delete_user_roles(self, user_id: str):
        pass

    @abc.abstractmethod
    def delete_user_teams(self, user_id: str):
        pass

    @abc.abstractmethod
    def get_user_details(self, user_id: str) -> UserDTO:
        pass
