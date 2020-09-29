import abc
from dataclasses import dataclass
from typing import List

from ib_adhoc_tasks.adapters.dtos import TasksCompleteDetailsDTO, \
    TaskIdWithSubTasksCountDTO, TaskIdWithCompletedSubTasksCountDTO
from ib_adhoc_tasks.interactors.storage_interfaces.dtos import GroupDetailsDTO, \
    GroupByResponseDTO


@dataclass
class TaskDetailsWithGroupInfoForListViewDTO:
    group_details_dtos: List[GroupDetailsDTO]
    task_details_dto: TasksCompleteDetailsDTO
    total_groups_count: int
    task_with_sub_tasks_count_dtos: List[TaskIdWithSubTasksCountDTO]
    task_completed_sub_tasks_count_dtos: \
        List[TaskIdWithCompletedSubTasksCountDTO]


class GetTasksForListViewPresenterInterface(abc.ABC):

    @abc.abstractmethod
    def raise_invalid_project_id(self):
        pass

    @abc.abstractmethod
    def get_task_details_group_by_info_response(
            self,
            task_details_with_group_info_list_view_dto:
            TaskDetailsWithGroupInfoForListViewDTO,
            group_by_response_dto: GroupByResponseDTO
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
