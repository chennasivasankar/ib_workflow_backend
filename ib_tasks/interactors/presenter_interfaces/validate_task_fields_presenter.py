import abc

from ib_tasks.exceptions.fields_custom_exceptions import \
    UserDidNotFillRequiredFields


class ValidateTaskFieldsPresenterInterface(abc.ABC):

    @abc.abstractmethod
    def raise_user_did_not_fill_required_fields(
            self, err: UserDidNotFillRequiredFields):
        pass

    @abc.abstractmethod
    def start_date_is_required(self):
        pass

    @abc.abstractmethod
    def due_date_is_required(self):
        pass

    @abc.abstractmethod
    def priority_is_required(self):
        pass
