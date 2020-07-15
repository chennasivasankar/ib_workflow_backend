from abc import abstractmethod, ABC


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
    def raise_offset_value_is_greater_than_limit_exception(self):
        pass