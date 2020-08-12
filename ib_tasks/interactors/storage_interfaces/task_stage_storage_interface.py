import abc
from typing import List

from ib_tasks.interactors.stages_dtos import TaskStageHistoryDTO, StageMinimalDTO
from ib_tasks.interactors.storage_interfaces.stage_dtos import \
    TaskStageAssigneeDTO


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