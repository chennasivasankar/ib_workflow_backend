from abc import ABC, abstractmethod


class PresenterInterface(ABC):

    @abstractmethod
    def raise_role_id_should_not_be_empty_exception(self):
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
    def raise_invalid_role_id_execption(self):
        pass

    @abstractmethod
    def raise_duplicate_role_ids_exception(self):
        pass