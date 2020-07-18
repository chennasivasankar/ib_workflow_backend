from typing import Optional, List

from ib_tasks.interactors.storage_interfaces.dtos import (
    StageInformationDTO, TaskStagesDTO, TaskStatusDTO)
from ib_tasks.interactors.storage_interfaces.storage_interface import \
    TaskStorageInterface
from ib_tasks.models import Stage


class StorageImplementation(TaskStorageInterface):
    def create_stages_with_given_information(self, stage_information: StageInformationDTO):
        pass

    def validate_stage_ids(self, stage_ids) -> Optional[List[str]]:
        valid_stage_ids = (Stage.objects.filter(stage_id__in=stage_ids)
                           .values_list('stage_id', flat=True))

        return list(valid_stage_ids)

    def update_stages_with_given_information(self,
                                             update_stages_information: StageInformationDTO):
        pass

    def validate_stages_related_task_template_ids(self,
                                                  task_stages_dto: TaskStagesDTO) -> \
            Optional[List[str]]:
        pass

    def get_task_template_ids(self) -> List[str]:
        pass

    def create_status_for_tasks(self, create_status_for_tasks: List[TaskStatusDTO]):
        pass
