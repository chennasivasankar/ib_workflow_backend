from ib_tasks.interactors.presenter_interfaces.get_task_rps_presenter import GetTaskRpsPresenterInterface
from ib_tasks.interactors.storage_interfaces.storage_interface import StorageInterface
from ib_tasks.interactors.storage_interfaces.task_storage_interface import \
    TaskStorageInterface
from ib_tasks.interactors.task_dtos import GetTaskRPsParametersDTO


class GetTaskRPsInteractor:
    def __init__(self, storage: StorageInterface,
                 task_storage: TaskStorageInterface):
        self.storage = storage
        self.task_storage = task_storage

    def get_task_rps_wrapper(self, presenter: GetTaskRpsPresenterInterface,
                             parameters: GetTaskRPsParametersDTO):
        pass
