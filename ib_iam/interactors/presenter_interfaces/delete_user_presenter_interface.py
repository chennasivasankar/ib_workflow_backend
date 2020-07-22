from abc import ABC, abstractmethod


class DeleteUserPresenterInterface(ABC):
    @abstractmethod
    def get_delete_user_response(self):
        pass
