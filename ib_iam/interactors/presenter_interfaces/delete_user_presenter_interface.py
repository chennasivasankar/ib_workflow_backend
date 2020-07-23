from abc import ABC, abstractmethod


class DeleteUserPresenterInterface(ABC):
    @abstractmethod
    def get_delete_user_response(self):
        pass

    @abstractmethod
    def raise_user_is_not_admin_exception(self):
        pass

    @abstractmethod
    def raise_user_is_not_found_exception(self):
        pass

    @abstractmethod
    def raise_user_does_not_have_delete_permission_exception(self):
        pass
