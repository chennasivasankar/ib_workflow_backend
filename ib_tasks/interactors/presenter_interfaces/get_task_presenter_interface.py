import abc
from dataclasses import dataclass
from ib_tasks.exceptions.task_custom_exceptions import InvalidTaskIdException


from ib_tasks.interactors.storage_interfaces.get_task_dtos \
    import TaskDetailsDTO


@dataclass
class TaskCompleteDetailsDTO:
    task_id: int
    task_details_dto: TaskDetailsDTO


class GetTaskPresenterInterface(abc.ABC):

    @abc.abstractmethod
    def raise_exception_for_invalid_task_id(self, err: InvalidTaskIdException):
        pass

    @abc.abstractmethod
    def get_task_response(self, task_complete_details_dto: TaskCompleteDetailsDTO):
        pass