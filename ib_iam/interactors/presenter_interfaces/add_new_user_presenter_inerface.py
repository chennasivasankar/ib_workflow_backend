import abc


class AddUserPresenterInterface(abc.ABC):
    @abc.abstractmethod
    def response_for_user_is_not_admin_exception(self):
        pass

    @abc.abstractmethod
    def response_for_invalid_name_length_exception(self):
        pass

    @abc.abstractmethod
    def response_for_invalid_email_exception(self):
        pass

    @abc.abstractmethod
    def response_for_user_account_already_exists_exception(self):
        pass

    @abc.abstractmethod
    def response_for_name_contains_special_character_exception(self):
        pass

    @abc.abstractmethod
    def response_for_invalid_role_ids_exception(self):
        pass

    @abc.abstractmethod
    def response_for_invalid_company_ids_exception(self):
        pass

    @abc.abstractmethod
    def response_for_invalid_team_ids_exception(self):
        pass

    @abc.abstractmethod
    def response_for_add_user_response(self):
        pass
