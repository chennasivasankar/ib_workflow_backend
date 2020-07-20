import abc
from typing import Optional, List
from ib_tasks.interactors.storage_interfaces.dtos import (
    StageDTO, TaskStagesDTO, TaskStatusDTO)

class TaskStorageInterface(abc.ABC):
    @abc.abstractmethod
    def create_stages_with_given_information(self,
                                             stage_information: StageDTO):
        pass

    @abc.abstractmethod
    def validate_stage_ids(self, stage_ids) -> Optional[List[str]]:
        pass

    @abc.abstractmethod
    def update_stages_with_given_information(self,
                                             update_stages_information: StageDTO):
        pass

    @abc.abstractmethod
    def validate_stages_related_task_template_ids(self,
                                                 task_stages_dto: TaskStagesDTO) -> \
            Optional[List[TaskStagesDTO]]:
        pass

    @abc.abstractmethod
    def get_valid_template_ids_in_given_template_ids(self, task_template_ids: List[str]) -> List[str]:
        pass

    @abc.abstractmethod
    def create_status_for_tasks(self, create_status_for_tasks: List[TaskStatusDTO]):
        pass
