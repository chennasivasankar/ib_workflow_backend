from abc import ABC
from abc import abstractmethod
from typing import List
from ib_tasks.interactors.storage_interfaces.dtos import StageActionsDto
from ib_tasks.interactors.dtos import ActionDto, TaskDto


class StorageInterface(ABC):

    @abstractmethod
    def get_stage_action_names(
            self, stage_ids: List[str]) -> List[StageActionsDto]:
        pass

    @abstractmethod
    def get_db_stage_ids(self, stage_ids: List[str]):
        pass

    @abstractmethod
    def create_stage_actions(self, stage_actions: List[ActionDto]):
        pass

    @abstractmethod
    def update_stage_actions(self, stage_actions: List[ActionDto]):
        pass

    @abstractmethod
    def delete_stage_actions(self, stage_actions: List[StageActionsDto]):
        pass

    @abstractmethod
    def create_tasks(self, tasks_dto: List[TaskDto]):
        pass

    @abstractmethod
    def update_tasks(self, tasks_dto: List[TaskDto]):
        pass