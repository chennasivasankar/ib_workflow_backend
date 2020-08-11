import abc
from typing import List

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
    def get_count_of_tasks_assigned_for_each_user(
            self, db_stage_ids: List[int],
            task_ids: List[int], permitted_user_ids: List[str]):
        pass
