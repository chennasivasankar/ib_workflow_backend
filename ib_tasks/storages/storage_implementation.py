from typing import Optional, List

from ib_tasks.interactors.stages_dtos import StageDTO, TaskTemplateStageDTO
from ib_tasks.interactors.storage_interfaces.stage_dtos import TaskStagesDTO, \
    ValidStageDTO
from ib_tasks.interactors.storage_interfaces.stages_storage_interface import \
    StageStorageInterface
from ib_tasks.models import TaskTemplateInitialStage, Stage


class StagesStorageImplementation(StageStorageInterface):
    def create_stages(self, stage_information: List[StageDTO]):
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

    def get_existing_stage_ids(self, stage_ids: List[str]) -> Optional[List[str]]:
        valid_stage_ids = Stage.objects.filter(
            stage_id__in=stage_ids
        ).values_list('stage_id', flat=True)
        return list(valid_stage_ids)

    def update_stages(self,
                      update_stages_information: StageDTO):
        stage_ids = [
            update_stage_information.stage_id
            for update_stage_information in update_stages_information
        ]
        stage_objects = Stage.objects.filter(stage_id__in=stage_ids)
        stage_objects_dict = {}
        for stage_object in stage_objects:
            stage_objects_dict[stage_object.stage_id] = stage_object
        list_of_stages = []
        for stage in update_stages_information:
            list_of_stages.append(self._get_update_stage_object(
                stage, stage_object
            )
            )
        Stage.objects.bulk_update(list_of_stages,
                                  ['stage_id', 'task_template_id',
                                   'value', 'display_name', 'display_logic'])

    @staticmethod
    def _get_update_stage_object(stage, stage_object):
        stage_object.stage_id = stage.stage_id
        stage_object.display_name = stage.stage_display_name
        stage_object.value = stage.value
        stage_object.display_logic = stage.stage_display_logic
        return stage_object

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
        # TODO need to send invalid_task_id_stages
        return []

    def create_initial_stage_to_task_template(self,
                                              task_template_stage_dtos: List[
                                                  TaskTemplateStageDTO]):
        stage_ids = [stage.stage_id for stage in task_template_stage_dtos]
        stages = Stage.objects.filter(stage_id__in=stage_ids).values('stage_id',
                                                                     'id')

        list_of_stages = {}
        for item in stages:
            list_of_stages[item['stage_id']] = item['id']

        list_of_task_stages = []
        for task in list_of_task_stages:
            list_of_stages.append(TaskTemplateInitialStage(
                task_template_id=task.task_template_id,
                stage_id=list_of_stages[task.stage_id]
            ))
        TaskTemplateInitialStage.objects.bulk_create(list_of_task_stages)
