from typing import Optional, List

from ib_tasks.interactors.storage_interfaces.dtos import (
    StageDTO, TaskStagesDTO, TaskStatusDTO, ValidStageDTO)
from ib_tasks.interactors.storage_interfaces.storage_interface import \
    TaskStorageInterface
from ib_tasks.models import Stage, TaskStatusVariable


class StorageImplementation(TaskStorageInterface):
    def create_stages(self, stage_information: StageDTO):
        list_of_stages = []
        for stage in stage_information:
            list_of_stages.append(self._get_stage_object(stage))
        Stage.objects.bulk_create(list_of_stages)

    @staticmethod
    def _get_stage_object(stage):
        return Stage(stage_id=stage.stage_id,
                     display_name=stage.stage_display_name,
                     task_template_id=stage.task_template_id,
                     value=stage.value,
                     display_logic=stage.stage_display_logic)

    def get_valid_stage_ids(self, stage_ids) -> Optional[List[str]]:
        valid_stage_ids = Stage.objects.filter(stage_id__in=stage_ids)

        valid_stages_dto = [ValidStageDTO(
            stage_id=stage.stage_id,
            id=stage.id
        ) for stage in valid_stage_ids]

        return list(valid_stages_dto)

    def update_stages(self,
                      update_stages_information: StageDTO):
        list_of_stages = []
        for stage in update_stages_information:
            list_of_stages.append(self._get_update_stage_object(stage))
        Stage.objects.bulk_update(list_of_stages,
                                  ['stage_id', 'task_template_id',
                                   'value', 'display_name', 'display_logic'])

    @staticmethod
    def _get_update_stage_object(stage):
        return Stage(stage_id=stage.stage_id,
                     display_name=stage.stage_display_name,
                     value=stage.value,
                     id=stage.id,
                     display_logic=stage.stage_display_logic)

    def validate_stages_related_task_template_ids(self,
                                                  task_stages_dto: TaskStagesDTO) -> \
            Optional[List[str]]:
        invalid_task_id_stages = []
        stage_ids = [stage.stage_id for stage in task_stages_dto]
        task_template_ids = [stage.task_template_id
                             for stage in task_stages_dto]

        stages = list(Stage.objects
                      .filter(stage_id__in=stage_ids,
                              task_template_id__in=task_template_ids)
                      .values_list('stage_id', flat=True))

        for stage in task_stages_dto:
            if stage.stage_id not in stages:
                invalid_task_id_stages.append(stage.stage_id)
        return invalid_task_id_stages

    def get_valid_template_ids_in_given_template_ids(self,
                                                     task_template_ids: List[str]) -> List[str]:
        pass

    def create_status_for_tasks(self, create_status_for_tasks: List[TaskStatusDTO]):
        list_of_status_tasks = [TaskStatusVariable(
            variable=status.status_variable_id,
            task_template_id=status.task_template_id
        ) for status in create_status_for_tasks]

        TaskStatusVariable.objects.bulk_create(list_of_status_tasks)
