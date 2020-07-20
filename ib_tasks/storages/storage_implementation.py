from typing import Optional, List

from ib_tasks.interactors.storage_interfaces.dtos import (
    StageDTO, TaskStagesDTO, TaskStatusDTO)
from ib_tasks.interactors.storage_interfaces.storage_interface import \
    TaskStorageInterface
from ib_tasks.models import Stage


class StorageImplementation(TaskStorageInterface):
    def create_stages_with_given_information(self, stage_information: StageDTO):
        list_of_stages = []
        for stage in stage_information:
            list_of_stages.append(Stage(stage_id=stage.stage_id,
                                        display_name=stage.stage_display_name,
                                        value=stage.value,
                                        display_logic=stage.stage_display_logic))
        Stage.objects.bulk_create(list_of_stages)

    def validate_stage_ids(self, stage_ids) -> Optional[List[str]]:
        valid_stage_ids = (Stage.objects.filter(stage_id__in=stage_ids)
                           .values_list('stage_id', flat=True))

        return list(valid_stage_ids)

    def update_stages_with_given_information(self,
                                             update_stages_information: StageDTO):
        list_of_stages = []
        for stage in update_stages_information:
            list_of_stages.append(Stage(stage_id=stage.stage_id,
                                        display_name=stage.stage_display_name,
                                        value=stage.value,
                                        display_logic=stage.stage_display_logic))
        Stage.objects.bulk_update(list_of_stages)

    def validate_stages_related_task_template_ids(self,
                                                  task_stages_dto: TaskStagesDTO) -> \
            Optional[List[str]]:
        pass

    def get_valid_template_ids_in_given_template_ids(self,
                                                     task_template_ids: List[str]) -> List[str]:
        pass

    def create_status_for_tasks(self, create_status_for_tasks: List[TaskStatusDTO]):
        pass
