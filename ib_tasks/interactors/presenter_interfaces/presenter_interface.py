import abc

from ib_tasks.interactors.presenter_interfaces.dtos import TaskCompleteDetailsDTO


class PresenterInterface(abc.ABC):

    @abc.abstractmethod
    def raise_exception_for_invalid_task(self, error_obj):
        pass

    @abc.abstractmethod
    def raise_exception_for_invalid_board(self, error_obj):
        pass

    @abc.abstractmethod
    def raise_exception_for_invalid_action(self, error_obj):
        pass

    @abc.abstractmethod
    def raise_exception_for_user_action_permission_denied(self, error_obj):
        pass

    @abc.abstractmethod
    def raise_exception_for_user_board_permission_denied(self, error_obj):
        pass

    @abc.abstractmethod
    def get_response_for_user_action_on_task(
            self, task_complete_details_dto: TaskCompleteDetailsDTO):
        pass

    @abc.abstractmethod
    def raise_exception_for_invalid_present_actions(self, error_obj):
        pass
