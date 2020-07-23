import abc
from ib_tasks.exceptions.task_custom_exceptions import InvalidTaskIdException


class GetTaskPresenterInterface(abc.ABC):

    @abc.abstractmethod
    def raise_exception_for_invalid_task_id(self, err: InvalidTaskIdException):
        pass

    @abc.abstractmethod
    def get_task_response(self, task_details_dto):
        pass