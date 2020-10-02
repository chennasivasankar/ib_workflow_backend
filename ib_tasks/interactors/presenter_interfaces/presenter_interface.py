import abc

from ib_tasks.exceptions.fields_custom_exceptions import \
    UserDidNotFillRequiredFields
from ib_tasks.exceptions.gofs_custom_exceptions import \
    UserDidNotFillRequiredGoFs
from ib_tasks.exceptions.stage_custom_exceptions import \
    StageIdsListEmptyException, InvalidStageIdsListException
from ib_tasks.exceptions.task_custom_exceptions import \
    TaskDelayReasonIsNotUpdated, InvalidTaskJson
from ib_tasks.interactors.presenter_interfaces.dtos import \
    TaskCompleteDetailsDTO, AllTasksOverviewDetailsDTO
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
    def get_response_for_user_not_in_project(self):
        pass

    @abc.abstractmethod
    def get_response_for_user_action_on_task(
            self, task_complete_details_dto: TaskCompleteDetailsDTO,
            task_current_stage_details_dto: TaskCurrentStageDetailsDTO,
            all_tasks_overview_dto: AllTasksOverviewDetailsDTO
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

    @abc.abstractmethod
    def raise_stage_ids_list_empty_exception(
            self, err: StageIdsListEmptyException):
        pass

    @abc.abstractmethod
    def raise_invalid_stage_ids_list_exception(
            self, err: InvalidStageIdsListException):
        pass

    @abc.abstractmethod
    def get_response_for_task_delay_reason_not_updated(
            self, err: TaskDelayReasonIsNotUpdated):
        pass

    @abc.abstractmethod
    def raise_user_did_not_fill_required_gofs(self,
                                              err: UserDidNotFillRequiredGoFs):
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

    @abc.abstractmethod
    def raise_invalid_task_json(self, err: InvalidTaskJson):
        pass
