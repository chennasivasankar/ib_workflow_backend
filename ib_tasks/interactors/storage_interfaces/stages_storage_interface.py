import abc
from typing import Optional, List
from ib_tasks.interactors.storage_interfaces.dtos import (
    StageInformationDTO, TaskStagesDTO)


class StageStorageInterface(abc.ABC):
    @abc.abstractmethod
    def create_stages_with_given_information(
            self, stage_information: StageInformationDTO):
        pass

    @abc.abstractmethod
    def validate_stage_ids(self, stage_ids) -> Optional[List[str]]:
        pass

    @abc.abstractmethod
    def update_stages_with_given_information(
            self, update_stages_information: StageInformationDTO):
        pass

    @abc.abstractmethod
    def validate_stages_related_task_template_ids(
            self, task_stages_dto: TaskStagesDTO) -> Optional[List[TaskStagesDTO]]:
        pass




