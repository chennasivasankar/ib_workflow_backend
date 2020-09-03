import abc


class AddUserPresenterInterface(abc.ABC):
    @abc.abstractmethod
    def raise_user_is_not_admin_exception(self):
        pass

    @abc.abstractmethod
    def raise_invalid_name_length_exception_for_update_user_profile(self):
        pass

    @abc.abstractmethod
    def raise_invalid_email_exception(self):
        pass

    @abc.abstractmethod
    def raise_user_account_already_exist_with_this_email_exception(self):
        pass

    @abc.abstractmethod
    def raise_name_should_not_contain_special_characters_exception(self):
        pass

    @abc.abstractmethod
    def raise_role_ids_are_invalid(self):
        pass

    @abc.abstractmethod
    def raise_company_ids_is_invalid(self):
        pass

    @abc.abstractmethod
    def raise_team_ids_are_invalid(self):
        pass

    @abc.abstractmethod
    def user_created_response(self):
        pass
