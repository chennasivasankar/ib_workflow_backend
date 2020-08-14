from datetime import datetime

from ib_tasks.exceptions.custom_exceptions import InvalidDueDateTimeException
from ib_tasks.exceptions.task_custom_exceptions import InvalidTaskIdException, \
    UserIsNotAssigneeToTask, InvalidReasonIdException
from ib_tasks.interactors.presenter_interfaces.task_due_missing_details_presenter import \
    TaskDueDetailsPresenterInterface
from ib_tasks.interactors.storage_interfaces.storage_interface import StorageInterface
from ib_tasks.interactors.task_dtos import TaskDueParametersDTO


class AddTaskDueDetailsInteractor:
    def __init__(self,
                 storage: StorageInterface):
        self.storage = storage

    def add_task_due_details_wrapper(self,
                                     presenter: TaskDueDetailsPresenterInterface,
                                     due_details: TaskDueParametersDTO):
        try:
            self.add_task_due_details(due_details)
        except InvalidTaskIdException as err:
            return presenter.response_for_invalid_task_id(err)
        except InvalidDueDateTimeException:
            return presenter.response_for_invalid_due_datetime()
        except UserIsNotAssigneeToTask:
            return presenter.response_for_user_is_not_assignee_for_task()
        except InvalidReasonIdException:
            return presenter.response_for_invalid_reason_id()

    def add_task_due_details(self, due_details: TaskDueParametersDTO):
        task_id = due_details.task_id
        user_id = due_details.user_id
        reason_id = due_details.reason_id
        updated_due_datetime = due_details.due_date_time
        self._validate_task_id(task_id)
        self._validate_if_task_is_assigned_to_user(task_id=task_id, user_id=user_id)
        self._validate_updated_due_datetime(updated_due_datetime)
        self._validate_reason_id(reason_id)

        self._add_task_due_delay_details(due_details)

    def _add_task_due_delay_details(self, due_details):
        reason_id = due_details.reason_id
        from ib_tasks.constants.enum import DELAYREASONS
        for reason_dict in DELAYREASONS:
            if reason_dict['id'] == reason_id and reason_id != -1:
                due_details.reason = reason_dict['reason']

        self.storage.add_due_delay_details(due_details)

    @staticmethod
    def _validate_reason_id(reason_id):
        from ib_tasks.constants.enum import DELAYREASONS
        valid_reason_ids = [reason['id'] for reason in DELAYREASONS]
        if reason_id not in valid_reason_ids:
            raise InvalidReasonIdException

    @staticmethod
    def _validate_updated_due_datetime(updated_due_datetime):
        if updated_due_datetime < datetime.now():
            raise InvalidDueDateTimeException()

    def _validate_task_id(self, task_id):
        is_valid = self.storage.validate_task_id(task_id)
        is_invalid = not is_valid
        if is_invalid:
            raise InvalidTaskIdException(task_id)

    def _validate_if_task_is_assigned_to_user(self, task_id: int, user_id: str):
        is_assigned = self.storage.validate_if_task_is_assigned_to_user(
            task_id, user_id
        )
        is_not_assigned = not is_assigned
        if is_not_assigned:
            raise UserIsNotAssigneeToTask
