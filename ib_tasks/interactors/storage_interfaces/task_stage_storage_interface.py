import abc
from dataclasses import dataclass
from typing import List

from ib_tasks.interactors.stages_dtos import TaskStageHistoryDTO, StageMinimalDTO
from ib_tasks.interactors.storage_interfaces.stage_dtos import \
    TaskStageAssigneeDTO
from ib_tasks.interactors.task_dtos import GetTaskDetailsDTO


@dataclass
class TaskStageAssigneeIdDTO:
    task_id: int
    stage_id: str
    assignee_id: str


class TaskStageStorageInterface(abc.ABC):

    @abc.abstractmethod
    def get_valid_stage_ids_of_task(
            self, task_id: int, stage_ids: List[int]
    ) -> List[int]:
        pass

    @abc.abstractmethod
    def get_stage_assignee_dtos(
            self, task_id: int, stage_ids: List[int]
    ) -> List[TaskStageAssigneeDTO]:
        pass

    @abc.abstractmethod
    def get_task_stage_dtos(self, task_id: int) -> List[TaskStageHistoryDTO]:
        pass

    @abc.abstractmethod
    def get_stage_details(self, stage_ids: List[int]) -> List[StageMinimalDTO]:
        pass

    @abc.abstractmethod
    def get_stage_assignee_id_dtos(
            self, task_stage_dtos: List[GetTaskDetailsDTO]) -> List[TaskStageAssigneeIdDTO]:
        pass