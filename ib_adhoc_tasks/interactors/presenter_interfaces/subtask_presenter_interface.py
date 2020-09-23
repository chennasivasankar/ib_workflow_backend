import abc

from ib_adhoc_tasks.adapters.dtos import TasksCompleteDetailsDTO


class GetSubTasksPresenterInterface(abc.ABC):

    @abc.abstractmethod
    def get_response_for_get_subtasks_of_task(
            self, complete_subtasks_details_dto: TasksCompleteDetailsDTO
    ):
        pass
