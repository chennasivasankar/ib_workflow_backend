import abc
from dataclasses import dataclass
from typing import List, Optional

from ib_tasks.interactors.stages_dtos import TaskStageHistoryDTO, \
    StageMinimalDTO
from ib_tasks.interactors.storage_interfaces.stage_dtos import \
    TaskStageAssigneeDTO, AssigneeCurrentTasksCountDTO, CurrentStageDetailsDTO
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
            task_ids: List[int]) -> List[
        AssigneeCurrentTasksCountDTO]:
        pass

    @abc.abstractmethod
    def get_task_stage_dtos(self, task_id: int) -> List[TaskStageHistoryDTO]:
        pass

    @abc.abstractmethod
    def get_stage_details(self, stage_ids: List[int]) -> List[StageMinimalDTO]:
        pass

    @abc.abstractmethod
    def get_stage_assignee_id_dtos(
            self, task_stage_dtos: List[GetTaskDetailsDTO]
    ) -> List[TaskStageAssigneeIdDTO]:
        pass

    @abc.abstractmethod
    def create_task_stage_history_records_for_virtual_stages(
            self, stage_ids: List[int], task_id: int):
        pass

    @abc.abstractmethod
    def get_latest_rp_id_if_exists(self, task_id: int,
                                   stage_id: int) -> Optional[str]:
        pass

    @abc.abstractmethod
    def get_rp_ids(self, task_id: int, stage_id: int) -> \
            List[str]:
        pass

    @abc.abstractmethod
    def add_superior_to_db(
            self, task_id: int, stage_id: int, superior_id: str):
        pass

    @abc.abstractmethod
    def get_latest_rp_added_datetime(self,
                                     task_id: int, stage_id: int
                                     ) -> Optional[str]:
        pass