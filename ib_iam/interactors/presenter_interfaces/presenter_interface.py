from abc import abstractmethod, ABC

from ib_iam.interactors.presenter_interfaces.dtos \
    import CompleteUsersDetailsDTO


class PresenterInterface(ABC):

    @abstractmethod
    def raise_user_is_not_admin_exception(self):
        pass

    @abstractmethod
    def raise_invalid_offset_value_exception(self):
        pass

    @abstractmethod
    def raise_invalid_limit_value_exception(self):
        pass

    @abstractmethod
    def raise_offset_value_is_greater_than_limit_value_exception(self):
        pass

    @abstractmethod
    def response_for_get_users(
            self, complete_user_details_dtos: CompleteUsersDetailsDTO):
        pass

    @abstractmethod
    def raise_invalid_name_exception(cls):
        pass

    @abstractmethod
    def raise_invalid_email_exception(cls):
        pass

    @abstractmethod
    def raise_user_account_already_exist_with_this_email_exception(cls):
        pass

    @abstractmethod
    def raise_name_should_not_contain_special_characters_exception(self):
        pass

    @abstractmethod
    def get_user_options_details_response(self, configuration_details):
        pass

    @abstractmethod
    def raise_role_ids_are_invalid(self):
        pass

    @abstractmethod
    def raise_company_ids_is_invalid(self):
        pass

    @abstractmethod
    def raise_team_ids_are_invalid(self):
        pass

    @abstractmethod
    def raise_role_name_should_not_be_empty_exception(self):
        pass

    @abstractmethod
    def raise_role_description_should_not_be_empty_exception(self):
        pass

    @abstractmethod
    def raise_role_id_format_is_invalid_exception(self):
        pass

    @abstractmethod
    def raise_duplicate_role_ids_exception(self):
        pass
