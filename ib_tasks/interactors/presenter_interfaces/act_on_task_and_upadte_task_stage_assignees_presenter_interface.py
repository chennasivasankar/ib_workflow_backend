import abc
from typing import List

from ib_tasks.exceptions.fields_custom_exceptions import \
    UserDidNotFillRequiredFields
from ib_tasks.exceptions.gofs_custom_exceptions import \
    UserDidNotFillRequiredGoFs
from ib_tasks.exceptions.stage_custom_exceptions import \
    StageIdsListEmptyException, InvalidStageIdsListException
from ib_tasks.exceptions.task_custom_exceptions import \
    TaskDelayReasonIsNotUpdated
from ib_tasks.interactors.presenter_interfaces.dtos import \
    TaskCompleteDetailsDTO, AllTasksOverviewDetailsDTO
from ib_tasks.interactors.task_dtos import TaskCurrentStageDetailsDTO


class ActOnTaskAndUpdateTaskStageAssigneesPresenterInterface(abc.ABC):

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
    def raise_duplicate_stage_ids_not_valid(self, duplicate_stage_ids):
        pass

    @abc.abstractmethod
    def raise_invalid_stage_ids_exception(self, invalid_stage_ids):
        pass

    @abc.abstractmethod
    def raise_stage_ids_with_invalid_permission_for_assignee_exception(
            self, invalid_stage_ids):
        pass

    @abc.abstractmethod
    def raise_invalid_task_display_id(self, err):
        pass

    @abc.abstractmethod
    def get_response_for_task_delay_reason_not_updated(
            self, err: TaskDelayReasonIsNotUpdated):
        pass


    @abc.abstractmethod
    def raise_user_did_not_fill_required_fields(
            self, err: UserDidNotFillRequiredFields):
        pass

    @abc.abstractmethod
    def raise_virtual_stage_ids_exception(self, virtual_stage_ids: List[int]):
        pass


