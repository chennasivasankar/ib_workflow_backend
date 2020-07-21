import abc
from typing import Optional, List

from ib_tasks.interactors.dtos import StageDTO
from ib_tasks.interactors.storage_interfaces.dtos import (
    TaskStagesDTO, ValidStageDTO)


class StageStorageInterface(abc.ABC):
    @abc.abstractmethod
    def create_stages(
            self, stage_information: StageDTO):
        pass

    @abc.abstractmethod
    def get_valid_stage_ids(self, stage_ids) -> Optional[List[ValidStageDTO]]:
        pass

    @abc.abstractmethod
    def update_stages(
            self, update_stages_information: StageDTO):
        pass

    @abc.abstractmethod
    def validate_stages_related_task_template_ids(
            self, task_stages_dto: TaskStagesDTO) -> Optional[List[TaskStagesDTO]]:
        pass

    @abc.abstractmethod
    def create_initial_stage_to_task_template(self, task_template_stage_dtos):
        pass
