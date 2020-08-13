import abc

from ib_tasks.interactors.presenter_interfaces.dtos import \
    TaskCompleteDetailsDTO
from ib_tasks.interactors.task_dtos import TaskCurrentStageDetailsDTO


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
            self, task_complete_details_dto: TaskCompleteDetailsDTO,
            task_current_stage_details_dto: TaskCurrentStageDetailsDTO
    ):
        pass

    @abc.abstractmethod
    def raise_exception_for_invalid_present_actions(self, error_obj):
        pass

    @abc.abstractmethod
    def raise_invalid_key_error(self):
        pass

    @abc.abstractmethod
    def raise_invalid_custom_logic_function_exception(self):
        pass

    @abc.abstractmethod
    def raise_invalid_path_not_found_exception(self, path_name):
        pass

    @abc.abstractmethod
    def raise_invalid_method_not_found_exception(self, method_name):
        pass

    @abc.abstractmethod
    def raise_duplicate_stage_ids_not_valid(self, duplicate_stage_ids):
        pass

    @abc.abstractmethod
    def raise_invalid_stage_ids_exception(self, invalid_stage_ids):
        pass

    @abc.abstractmethod
    def raise_stage_ids_with_invalid_permission_for_assignee_exception(self,
                                                                       invalid_stage_ids):
        pass

    @abc.abstractmethod
    def raise_invalid_task_display_id(self, err):
        pass
