import abc


class GetUserOptionsPresenterInterface(abc.ABC):

    @abc.abstractmethod
    def response_for_user_is_not_admin_exception(self):
        pass

    # TODO: typing
    @abc.abstractmethod
    def get_user_options_details_response(self, configuration_details):
        pass
