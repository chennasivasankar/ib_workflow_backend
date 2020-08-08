from ib_tasks.exceptions.task_custom_exceptions import InvalidTaskIdException, \
    UserIsNotAssigneeToTask
from ib_tasks.interactors.presenter_interfaces.get_task_presenter_interface import \
    GetTaskPresenterInterface
from ib_tasks.interactors.storage_interfaces.storage_interface import StorageInterface


class GetTaskDueMissingReasonsInteractor:
    def __init__(self, task_storage: StorageInterface):
        self.task_storage = task_storage

    def get_task_due_missing_reasons_wrapper(self,
                                             presenter: GetTaskPresenterInterface,
                                             task_id: int, user_id: str):
        try:
            self.get_task_due_missing_reasons(task_id, user_id)
        except InvalidTaskIdException as err:
            return presenter.response_for_invalid_task_id()
        except UserIsNotAssigneeToTask as err:
            return presenter.response_for_user_is_not_assignee_for_task()

    def get_task_due_missing_reasons(self, task_id: int, user_id: str):
        self._validate_task_id(task_id)
        self._validate_if_task_is_assigned_to_user(task_id, user_id)
        self._get_task_reasons(task_id)

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
        task_details = self.task_storage.get_task_due_missing_reasons(task_id)
