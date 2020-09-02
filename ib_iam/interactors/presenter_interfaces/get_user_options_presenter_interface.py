import abc


class GetUserOptionsPresenterInterface(abc.ABC):

    @abc.abstractmethod
    def raise_user_is_not_admin_exception(self):
        pass

    @abc.abstractmethod
    def get_user_options_details_response(self, configuration_details):
        pass
