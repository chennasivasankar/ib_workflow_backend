import abc

from ib_tasks.exceptions.task_custom_exceptions import InvalidTaskIdException
from ib_tasks.interactors.stages_dtos import TaskStageCompleteDetailsDTO


class GetTaskStagePresenterInterface(abc.ABC):

    @abc.abstractmethod
    def raise_exception_for_invalid_task_id(
            self, err: InvalidTaskIdException):
        pass

    @abc.abstractmethod
    def get_task_stages_history_response(
            self, task_stages_details_dto: TaskStageCompleteDetailsDTO):
        pass