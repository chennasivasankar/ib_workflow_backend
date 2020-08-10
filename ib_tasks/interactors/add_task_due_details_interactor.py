from ib_tasks.exceptions.task_custom_exceptions import InvalidTaskIdException
from ib_tasks.interactors.presenter_interfaces.task_due_missing_details_presenter import \
    TaskDueDetailsPresenterInterface
from ib_tasks.interactors.storage_interfaces.task_storage_interface import TaskStorageInterface
from ib_tasks.interactors.task_dtos import TaskDueParametersDTO


class AddTaskDueDetailsInteractor:
    def __init__(self, storage: TaskStorageInterface):
        self.storage = storage

    def add_task_due_details_wrapper(self,
                                     presenter: TaskDueDetailsPresenterInterface,
                                     due_details: TaskDueParametersDTO):
        try:
            self.add_task_due_details(due_details)
        except InvalidTaskIdException as err:
            return presenter.response_for_invalid_task_id()

    def add_task_due_details(self, due_details: TaskDueParametersDTO):
        task_id = due_details.task_id

        is_valid = self.storage.validate_task_id(task_id)
        is_invalid = not is_valid
        if is_invalid:
            raise InvalidTaskIdException(task_id)

