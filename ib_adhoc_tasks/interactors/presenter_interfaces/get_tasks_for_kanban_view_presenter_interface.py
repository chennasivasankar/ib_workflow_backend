import abc
from typing import List

from ib_adhoc_tasks.adapters.dtos import TasksCompleteDetailsDTO
from ib_adhoc_tasks.interactors.storage_interfaces.dtos import GroupDetailsDTO, \
    ChildGroupCountDTO


class TaskDetailsWithGroupByInfoDTO:
    group_details_dtos: List[GroupDetailsDTO]
    total_groups_count: int
    child_group_count_dtos: List[ChildGroupCountDTO]
    task_details_dtos: List[TasksCompleteDetailsDTO]


class GetTasksForKanbanViewPresenterInterface(abc.ABC):

    @abc.abstractmethod
    def raise_invalid_project_id(self):
        pass

    @abc.abstractmethod
    def get_task_details_group_by_info_response(
            self,
            task_details_with_group_by_info_dto: TaskDetailsWithGroupByInfoDTO
    ):
        pass
