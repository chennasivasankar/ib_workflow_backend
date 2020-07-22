from abc import ABC, abstractmethod


class DeleteUserStorageInterface(ABC):
    @abstractmethod
    def delete_user(self, user_id: str, delete_user_id: str):
        pass
