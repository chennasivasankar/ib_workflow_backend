from ib_tasks.exceptions.task_custom_exceptions import InvalidTaskIdException
from ib_tasks.interactors.presenter_interfaces.get_task_presenter_interface import \
    GetTaskPresenterInterface
from ib_tasks.interactors.storage_interfaces.task_storage_interface import TaskStorageInterface


class GetTaskDueMissingReasonsInteractor:
    def __init__(self, task_storage: TaskStorageInterface):
        self.task_storage = task_storage

    def get_task_due_missing_reasons_wrapper(self,
                                             presenter: GetTaskPresenterInterface,
                                             task_id: int, user_id: str):
        try:
            self.get_task_due_missing_reasons(task_id, user_id)
        except InvalidTaskIdException:
            return presenter.raise_exception_for_invalid_task_id()

    def get_task_due_missing_reasons(self, task_id: int, user_id: str):
        pass
