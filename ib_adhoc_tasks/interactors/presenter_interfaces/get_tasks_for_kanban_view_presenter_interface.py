import abc
from typing import List
from dataclasses import dataclass

from ib_adhoc_tasks.adapters.dtos import TasksCompleteDetailsDTO
from ib_adhoc_tasks.interactors.storage_interfaces.dtos import GroupDetailsDTO, \
    ChildGroupCountDTO


@dataclass
class TaskDetailsWithGroupByInfoDTO:
    group_details_dtos: List[GroupDetailsDTO]
    total_groups_count: int
    child_group_count_dtos: List[ChildGroupCountDTO]
    task_details_dtos: TasksCompleteDetailsDTO


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

    @abc.abstractmethod
    def raise_invalid_offset_value(self):
        pass

    @abc.abstractmethod
    def raise_invalid_limit_value(self):
        pass

    @abc.abstractmethod
    def raise_invalid_user_id(self):
        pass

    @abc.abstractmethod
    def raise_invalid_user_for_project(self):
        pass


