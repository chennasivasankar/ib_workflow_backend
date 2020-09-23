import abc
from typing import List

from ib_adhoc_tasks.adapters.dtos import TasksCompleteDetailsDTO


class GetSubTasksPresenterInterface(abc.ABC):

    @abc.abstractmethod
    def get_response_for_get_subtasks_of_task(
            self, subtask_ids: List[int],
            complete_subtasks_details_dto: TasksCompleteDetailsDTO
    ):
        pass
