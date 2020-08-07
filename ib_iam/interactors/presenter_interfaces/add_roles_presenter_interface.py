from abc import abstractmethod, ABC


class AddRolesPresenterInterface(ABC):

    @abstractmethod
    def raise_user_is_not_admin_exception(self):
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
    def raise_duplicate_role_ids_exception(self, err):
        pass
