import abc
from dataclasses import dataclass
from typing import List
from ib_tasks.exceptions.task_custom_exceptions import InvalidTaskIdException

from ib_tasks.interactors.storage_interfaces.get_task_dtos \
    import TaskDetailsDTO
from ib_tasks.interactors.task_dtos import StageAndActionsDetailsDTO


@dataclass
class TaskCompleteDetailsDTO:
    task_id: int
    task_details_dto: TaskDetailsDTO
    stages_and_actions_details_dtos: List[StageAndActionsDetailsDTO]


class GetTaskPresenterInterface(abc.ABC):

    @abc.abstractmethod
    def raise_exception_for_invalid_task_id(self, err: InvalidTaskIdException):
        pass

    @abc.abstractmethod
    def get_task_response(self, task_complete_details_dto: TaskCompleteDetailsDTO):
        pass

    @abc.abstractmethod
    def response_for_invalid_task_id(self):
        pass

    @abc.abstractmethod
    def response_for_user_is_not_assignee_for_task(self):
        pass
