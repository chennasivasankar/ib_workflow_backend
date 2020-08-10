import abc
from typing import List

from ib_tasks.exceptions.task_custom_exceptions import \
    InvalidTaskIdException
from ib_tasks.interactors.storage_interfaces.task_dtos import TaskDueDetailsDTO


class TaskDueDetailsPresenterInterface(abc.ABC):

    @abc.abstractmethod
    def response_for_invalid_task_id(self, err: InvalidTaskIdException):
        pass

    @abc.abstractmethod
    def response_for_user_is_not_assignee_for_task(self):
        pass

    @abc.abstractmethod
    def get_response_for_get_task_due_details(self, task_dtos: List[TaskDueDetailsDTO]):
        pass

