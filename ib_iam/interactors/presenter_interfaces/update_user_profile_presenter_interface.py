import abc


class UpdateUserProfilePresenterInterface(abc.ABC):

    @abc.abstractmethod
    def get_success_response_for_update_user_profile(self):
        pass

    @abc.abstractmethod
    def get_response_for_empty_name_exception(self):
        pass

    @abc.abstractmethod
    def get_response_for_minimum_name_length(self):
        pass

    @abc.abstractmethod
    def get_response_for_name_contains_special_chars_and_numbers_exception(
            self):
        pass
