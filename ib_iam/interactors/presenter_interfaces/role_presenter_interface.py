import abc


class AddRolesPresenterInterface(abc.ABC):

    @abc.abstractmethod
    def response_for_user_is_not_admin_exception(self):
        pass

    @abc.abstractmethod
    def response_for_role_name_should_not_be_empty_exception(self):
        pass

    @abc.abstractmethod
    def response_for_role_description_should_not_be_empty_exception(self):
        pass

    @abc.abstractmethod
    def response_for_role_id_format_is_invalid_exception(self):
        pass

    @abc.abstractmethod
    def response_for_duplicate_role_ids_exception(self, err):
        pass
