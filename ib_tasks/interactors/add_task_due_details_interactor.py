from datetime import datetime

from ib_tasks.exceptions.custom_exceptions import InvalidDueDateTimeException
from ib_tasks.exceptions.stage_custom_exceptions import InvalidStageIdException
from ib_tasks.exceptions.task_custom_exceptions import UserIsNotAssigneeToTask, \
    InvalidReasonIdException, InvalidTaskDisplayId
from ib_tasks.interactors.mixins.get_task_id_for_task_display_id_mixin import \
    GetTaskIdForTaskDisplayIdMixin
from ib_tasks.interactors.presenter_interfaces.task_due_missing_details_presenter import \
    TaskDueDetailsPresenterInterface
from ib_tasks.interactors.storage_interfaces.storage_interface import StorageInterface
from ib_tasks.interactors.storage_interfaces.task_storage_interface import TaskStorageInterface
from ib_tasks.interactors.task_dtos import TaskDueParametersDTO, TaskDelayParametersDTO


class AddTaskDueDetailsInteractor(GetTaskIdForTaskDisplayIdMixin):
    def __init__(self,
                 storage: StorageInterface,
                 task_storage: TaskStorageInterface):
        self.task_storage = task_storage
        self.storage = storage

    def add_task_due_details_wrapper(self,
                                     presenter: TaskDueDetailsPresenterInterface,
                                     due_details: TaskDueParametersDTO, task_display_id: str):

        try:
            self.add_task_due_details(due_details, task_display_id)
        except InvalidTaskDisplayId as err:
            return presenter.response_for_invalid_task_id(err)
        except InvalidDueDateTimeException:
            return presenter.response_for_invalid_due_datetime()
        except UserIsNotAssigneeToTask:
            return presenter.response_for_user_is_not_assignee_for_task()
        except InvalidReasonIdException:
            return presenter.response_for_invalid_reason_id()
        except InvalidStageIdException:
            return presenter.response_for_invalid_stage_id()

    def add_task_due_details(self, parameters: TaskDueParametersDTO,
                             task_display_id: str):
        task_id = self.get_task_id_for_task_display_id(task_display_id)
        due_details = self._get_parameters_dto(parameters, task_id)
        user_id = due_details.user_id
        reason_id = due_details.reason_id
        stage_id = due_details.stage_id
        updated_due_datetime = due_details.due_date_time
        task_id = due_details.task_id
        self._validate_stage_id(stage_id=stage_id)
        self._validate_if_task_is_assigned_to_user(task_id=task_id,
                                                   user_id=user_id, stage_id=stage_id)
        self._validate_updated_due_datetime(updated_due_datetime)
        self._validate_reason_id(reason_id)

        self._add_task_due_delay_details(due_details)

    @staticmethod
    def _get_parameters_dto(due_details: TaskDueParametersDTO,
                            task_id: int):
        return TaskDelayParametersDTO(
            task_id=task_id,
            user_id=due_details.user_id,
            reason=due_details.reason,
            stage_id=due_details.stage_id,
            reason_id=due_details.reason_id,
            due_date_time=due_details.due_date_time
        )

    def _add_task_due_delay_details(self, due_details: TaskDelayParametersDTO):
        reason_id = due_details.reason_id
        from ib_tasks.constants.enum import DELAY_REASONS
        for reason_dict in DELAY_REASONS:
            if reason_dict['id'] == reason_id and reason_id != -1:
                due_details.reason = reason_dict['reason']

        self.storage.add_due_delay_details(due_details)

    def _validate_stage_id(self, stage_id: str):
        is_valid = self.storage.validate_stage_id(stage_id)
        if not is_valid:
            raise InvalidStageIdException

    @staticmethod
    def _validate_reason_id(reason_id):
        from ib_tasks.constants.enum import DELAY_REASONS
        valid_reason_ids = [reason['id'] for reason in DELAY_REASONS]
        if reason_id not in valid_reason_ids:
            raise InvalidReasonIdException

    @staticmethod
    def _validate_updated_due_datetime(updated_due_datetime):
        if updated_due_datetime < datetime.now():
            raise InvalidDueDateTimeException()

    def _validate_if_task_is_assigned_to_user(self, task_id: int, user_id: str,
                                              stage_id: str):
        is_assigned = self.storage.validate_if_task_is_assigned_to_user_in_given_stage(
            task_id, user_id, stage_id
        )
        is_not_assigned = not is_assigned
        if is_not_assigned:
            raise UserIsNotAssigneeToTask
