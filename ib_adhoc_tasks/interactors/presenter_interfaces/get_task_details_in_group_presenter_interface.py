import abc

from ib_adhoc_tasks.adapters.dtos import TasksCompleteDetailsDTO
from ib_adhoc_tasks.interactors.dtos.dtos import TaskIdsAndCountDTO


class GetTaskDetailsInGroupPresenterInterface(abc.ABC):

    @abc.abstractmethod
    def get_task_details_in_group_response(
            self, tasks_complete_details_dto: TasksCompleteDetailsDTO,
            task_ids_and_count_dto: TaskIdsAndCountDTO
    ):
        pass
