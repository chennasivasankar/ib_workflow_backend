from abc import ABC, abstractmethod


class GetUserOptionsPresenterInterface(ABC):

    @abstractmethod
    def raise_user_is_not_admin_exception(self):
        pass

    @abstractmethod
    def get_user_options_details_response(self, configuration_details):
        pass
