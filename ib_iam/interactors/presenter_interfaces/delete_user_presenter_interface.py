import abc


class DeleteUserPresenterInterface(abc.ABC):
    @abc.abstractmethod
    def get_delete_user_response(self):
        pass

    @abc.abstractmethod
    def raise_user_is_not_admin_exception(self):
        pass

    @abc.abstractmethod
    def raise_user_is_not_found_exception(self):
        pass

    @abc.abstractmethod
    def raise_user_does_not_have_delete_permission_exception(self):
        pass
