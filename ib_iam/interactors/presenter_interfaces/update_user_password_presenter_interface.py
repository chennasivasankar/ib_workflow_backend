import abc


class UpdateUserPasswordPresenterInterface(abc.ABC):

    @abc.abstractmethod
    def get_success_response_for_update_user_password(self):
        pass

    @abc.abstractmethod
    def raise_invalid_new_password_exception(self):
        pass

    @abc.abstractmethod
    def raise_invalid_current_password_exception(self):
        pass

    @abc.abstractmethod
    def raise_current_password_mismatch_exception(self):
        pass
