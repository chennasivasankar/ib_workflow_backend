import abc

from ib_tasks.exceptions.action_custom_exceptions import InvalidActionException
from ib_tasks.exceptions.fields_custom_exceptions import \
    UserDidNotFillRequiredFields


class ValidateTaskFieldsPresenterInterface(abc.ABC):

    @abc.abstractmethod
    def get_success_response(self):
        pass

    @abc.abstractmethod
    def raise_invalid_task_display_id(self, err):
        pass

    @abc.abstractmethod
    def raise_exception_for_invalid_action(self, err: InvalidActionException):
        pass

    @abc.abstractmethod
    def raise_exception_for_user_action_permission_denied(self, error_obj):
        pass

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
