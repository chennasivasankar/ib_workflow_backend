import abc


class EditUserPresenterInterface(abc.ABC):
    @abc.abstractmethod
    def edit_user_success_response(self):
        pass

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
    def response_for_name_contains_special_character_exception(self):
        pass

    @abc.abstractmethod
    def raise_role_ids_are_invalid(self):
        pass

    @abc.abstractmethod
    def response_for_invalid_company_ids_exception(self):
        pass

    @abc.abstractmethod
    def response_for_invalid_team_ids_exception(self):
        pass

    @abc.abstractmethod
    def raise_user_does_not_exist(self):
        pass
