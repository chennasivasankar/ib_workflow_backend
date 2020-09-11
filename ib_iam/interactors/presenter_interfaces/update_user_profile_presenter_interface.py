import abc


class UpdateUserProfilePresenterInterface(abc.ABC):

    @abc.abstractmethod
    def get_response_for_update_user_profile(self):
        pass

    @abc.abstractmethod
    def response_for_invalid_name_length_exception(self):
        pass

    @abc.abstractmethod
    def response_for_duplicate_role_ids_exception(self):
        pass

    @abc.abstractmethod
    def response_for_invalid_role_ids_exception(self):
        pass

    @abc.abstractmethod
    def response_for_name_contains_special_character_exception(
            self):
        pass

    @abc.abstractmethod
    def response_for_invalid_email_exception(self):
        pass

    @abc.abstractmethod
    def response_for_email_already_exists_exception(self):
        pass
