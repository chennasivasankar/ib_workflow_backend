from ib_tasks.interactors.presenter_interfaces.get_task_presenter_interface import \
    GetTaskPresenterInterface
from ib_tasks.interactors.storage_interfaces.task_storage_interface import TaskStorageInterface


class GetTaskDueMissingReasons:
    def __init__(self, task_storage: TaskStorageInterface):
        self.task_storage = task_storage

    def get_task_due_missing_reasons_wrapper(self,
                                             presenter: GetTaskPresenterInterface,
                                             task_id: int):
        try:
            self.get_task_due_missing_reasons()
