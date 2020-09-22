import abc
from dataclasses import dataclass
from typing import List

from ib_adhoc_tasks.adapters.dtos import TasksCompleteDetailsDTO
from ib_adhoc_tasks.exceptions.custom_exceptions import InvalidProjectId
from ib_adhoc_tasks.interactors.storage_interfaces.dtos import GroupDetailsDTO


@dataclass
class TaskDetailsWithGroupByInfoDTO:
    group_details_dtos = List[GroupDetailsDTO]
    task_details_dtos = List[TasksCompleteDetailsDTO]


class GetTasksForKanbanViewPresenterInterface(abc.ABC):

    @abc.abstractmethod
    def raise_invalid_project_id(self, err: InvalidProjectId):
        pass

    @abc.abstractmethod
    def get_task_details_group_by_info_reponse(
            self,
            task_details_with_group_by_info_dto: TaskDetailsWithGroupByInfoDTO
    ):
        pass
