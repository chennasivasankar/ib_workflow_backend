import abc
from typing import List

from ib_tasks.interactors.stages_dtos import TaskStageHistoryDTO, StageMinimalDTO
from ib_tasks.interactors.storage_interfaces.stage_dtos import \
    TaskStageAssigneeDTO, CurrentStageDetailsDTO, AssigneeCurrentTasksCountDTO


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
    def validate_task_id(self, task_id: int) -> str:
        pass

    @abc.abstractmethod
    def get_task_current_stage_ids(self, task_id: int) -> List[int]:
        pass

    @abc.abstractmethod
    def get_stage_details_dtos(
            self, stage_ids: List[int]
    ) -> List[CurrentStageDetailsDTO]:
        pass

    @abc.abstractmethod
    def is_user_has_permission_for_at_least_one_stage(
            self, stage_ids: List[int], user_roles: List[str]
    ) -> bool:
        pass




    @abc.abstractmethod
    def get_count_of_tasks_assigned_for_each_user(
            self, db_stage_ids: List[int],
            task_ids: List[int])-> List[
        AssigneeCurrentTasksCountDTO]:
        pass

    @abc.abstractmethod
    def get_task_stage_dtos(self, task_id: int) -> List[TaskStageHistoryDTO]:
        pass

    @abc.abstractmethod
    def get_stage_details(self, stage_ids: List[int]) -> List[StageMinimalDTO]:
        pass