import abc
from typing import Optional, List

from ib_tasks.interactors.dtos import StageDTO
from ib_tasks.interactors.storage_interfaces.dtos import (
    TaskStagesDTO, ValidStageDTO)


class StageStorageInterface(abc.ABC):
    @abc.abstractmethod
    def create_stages(self, stage_details: List[StageDTO]):
        pass

    @abc.abstractmethod
    def update_stages(self, stage_details: List[StageDTO]):
        pass

    @abc.abstractmethod
    def get_existing_stage_ids(self, stage_ids) -> Optional[List[str]]:
        pass


    @abc.abstractmethod
    def validate_stages_related_task_template_ids(self,
        task_stages_dto: List[TaskStagesDTO]) -> Optional[List[TaskStagesDTO]]:
        pass
