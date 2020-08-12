import abc


class UpdateUserProfilePresenterInterface(abc.ABC):

    @abc.abstractmethod
    def get_success_response_for_update_user_profile(self):
        pass

    @abc.abstractmethod
    def raise_invalid_name_length_exception_for_update_user_profile(self):
        pass

    @abc.abstractmethod
    def raise_name_should_not_contain_special_chars_and_numbers_exception_for_update_user_profile(
            self):
        pass

    @abc.abstractmethod
    def raise_invalid_email_exception_for_update_user_profile(self):
        pass

    @abc.abstractmethod
    def raise_email_already_in_use_exception_for_update_user_profile(self):
        pass
