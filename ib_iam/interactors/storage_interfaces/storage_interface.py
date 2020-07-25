from abc import ABC, abstractmethod


class StorageInterface(ABC):

    @abstractmethod
    def check_is_admin_user(self, user_id: str) -> bool:
        pass
