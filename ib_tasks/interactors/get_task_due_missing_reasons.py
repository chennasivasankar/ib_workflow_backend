from typing import List

from ib_tasks.adapters.service_adapter import get_service_adapter
from ib_tasks.exceptions.task_custom_exceptions import InvalidTaskIdException, \
    UserIsNotAssigneeToTask
from ib_tasks.interactors.presenter_interfaces.task_due_missing_details_presenter import \
    TaskDueDetailsPresenterInterface
from ib_tasks.interactors.storage_interfaces.storage_interface import StorageInterface
from ib_tasks.interactors.storage_interfaces.task_dtos import TaskDueMissingDTO, TaskDueDetailsDTO


class GetTaskDueMissingReasonsInteractor:
    def __init__(self, task_storage: StorageInterface):
        self.task_storage = task_storage

    def get_task_due_missing_reasons_wrapper(
            self,
            presenter: TaskDueDetailsPresenterInterface,
            task_id: int, user_id: str):
        try:
            task_dtos = self.get_task_due_missing_reasons(task_id, user_id)
        except InvalidTaskIdException as err:
            return presenter.response_for_invalid_task_id()
        except UserIsNotAssigneeToTask as err:
            return presenter.response_for_user_is_not_assignee_for_task()
        return presenter.get_response_for_get_task_due_details(task_dtos)

    def get_task_due_missing_reasons(self, task_id: int, user_id: str):
        self._validate_task_id(task_id)
        self._validate_if_task_is_assigned_to_user(task_id, user_id)
        task_dtos = self._get_task_reasons(task_id)
        return task_dtos

    def _validate_task_id(self, task_id):
        is_exists = self.task_storage.validate_task_id(task_id)
        does_not_exist = not is_exists
        if does_not_exist:
            raise InvalidTaskIdException(task_id)

    def _validate_if_task_is_assigned_to_user(self, task_id: int, user_id: str):
        is_assigned = self.task_storage.validate_if_task_is_assigned_to_user(
            task_id, user_id
        )
        is_not_assigned = not is_assigned
        if is_not_assigned:
            raise UserIsNotAssigneeToTask

    def _get_task_reasons(self, task_id: int):
        task_details = self.task_storage.get_task_due_missing_reasons_details(task_id)
        user_ids = [task.user_id for task in task_details]
        user_service = get_service_adapter().auth_service
        user_dtos = user_service.get_user_details(user_ids)
        users_dict = {}
        for user in user_dtos:
            users_dict[user.user_id] = user
        task_dtos = self._map_user_and_tasks(task_details, users_dict)
        return task_dtos

    @staticmethod
    def _map_user_and_tasks(task_details: List[TaskDueMissingDTO],
                            users_dict):
        tasks_dtos = []
        for task in task_details:
            tasks_dtos.append(
                TaskDueDetailsDTO(
                    task_id=task.task_id,
                    reason=task.reason,
                    due_date_time=task.due_date_time,
                    due_missed_count=task.due_missed_count,
                    user=users_dict[task.user_id]
                )
            )
        return tasks_dtos
