from typing import List
from typing import Optional

from ib_tasks.interactors.stages_dtos import TemplateStageDTO
from ib_tasks.interactors.global_constants_dtos import GlobalConstantsDTO
from ib_tasks.interactors.stages_dtos import StageActionDTO
from ib_tasks.interactors.stages_dtos import StageDTO
from ib_tasks.interactors.storage_interfaces.actions_dtos import ActionDTO, \
    ActionRolesDTO
from ib_tasks.interactors.storage_interfaces.fields_dtos import FieldValueDTO
from ib_tasks.interactors.storage_interfaces.gof_dtos import \
    GOFMultipleEnableDTO
from ib_tasks.interactors.storage_interfaces.stage_dtos import TaskStagesDTO, TaskTemplateStageDTO
from ib_tasks.interactors.storage_interfaces.stage_dtos import TaskStagesDTO, StageValueDTO
from ib_tasks.interactors.storage_interfaces.stages_storage_interface import \
    StageStorageInterface
from ib_tasks.interactors.storage_interfaces.storage_interface \
    import (
        StorageInterface, GroupOfFieldsDTO,
        StatusVariableDTO, StageActionNamesDTO
)
from ib_tasks.models import *
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

    def get_existing_stage_ids(self, stage_ids: List[str]) -> Optional[
        List[str]]:
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
                                  ['task_template_id',
                                   'value', 'display_name', 'display_logic'])

    @staticmethod
    def _get_update_stage_object(stage, stage_object):
        # stage_object.stage_id = stage.stage_id
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
        return invalid_task_id_stages

    def create_initial_stage_to_task_template(self,
                                              task_template_stage_dtos: List[
                                                  TaskTemplateStageDTO]):
        stage_ids = [stage.stage_id for stage in task_template_stage_dtos]
        stages = Stage.objects.filter(stage_id__in=stage_ids).values(
            'stage_id',
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


class StorageImplementation(StorageInterface):

    def get_stage_action_names(
            self, stage_ids: List[str]) -> List[StageActionNamesDTO]:
        pass

    def get_valid_stage_ids(self,
                            stage_ids: List[str]) -> Optional[List[str]]:
        pass

    def create_stage_actions(self, stage_actions: List[StageActionDTO]):
        pass

    def update_stage_actions(self, stage_actions: List[StageActionDTO]):
        pass

    def delete_stage_actions(self,
                             stage_actions: List[StageActionNamesDTO]):
        pass

    def create_initial_stage_to_task_template(
            self, task_template_stage_dtos: List[TemplateStageDTO]):
        pass

    def get_valid_task_template_ids(self, task_template_ids: List[str]):
        pass

    def validate_task_id(self, task_id: int) -> bool:

        return Task.objects.filter(id=task_id).exists()

    def get_task_group_of_fields_dto(
            self, task_id: str) -> List[GroupOfFieldsDTO]:
        # GOF.objects.filter()
        pass

    def get_fields_to_group_of_field_ids(
            self, group_of_field_ids: List[str]) -> List[FieldValueDTO]:
        # Field.objects.filter(gof_id__in=group_of_field_ids)
        pass

    def get_status_variables_to_task(
            self, task_id: int) -> List[StatusVariableDTO]:

        status_variable_objs = TaskStatusVariable.objects \
            .filter(task_id=task_id)

        return [
            StatusVariableDTO(
                status_id=status_variable_obj.id,
                status_variable=status_variable_obj.variable,
                value=status_variable_obj.value
            ) for status_variable_obj in status_variable_objs
        ]

    def get_path_name_to_action(self, action_id: int) -> str:

        action_obj = StageAction.objects.get(id=action_id)
        return action_obj.py_function_import_path

    def update_status_variables_to_task(self, task_id: int,
                                        status_variables_dto):
        status_variable_objs = TaskStatusVariable.objects \
            .filter(task_id=task_id)
        status_variable_dict = \
            self._get_status_variable_dict(status_variable_objs)
        for status_variable_dto in status_variables_dto:
            status_obj = status_variable_dict[status_variable_dto.status_id]
            status_obj.variable = status_variable_dto.status_variable
            status_obj.value = status_variable_dto.value

    @staticmethod
    def _get_status_variable_dict(status_variable_objs):

        status_variable_dict = {}

        for status_variable_obj in status_variable_objs:
            status_id = status_variable_obj.id
            status_variable_dict[status_id] = status_variable_obj
        return status_variable_dict

    def get_action_roles_to_stages(
            self, stage_ids: List[str]) -> List[ActionRolesDTO]:
        action_role_objs = ActionPermittedRoles.objects.filter(
            action__in=StageAction.objects.filter(
                stage__stage_id__in=stage_ids
            )
        )
        from collections import defaultdict
        action_roles_dict = defaultdict(list)
        for action_role_obj in action_role_objs:
            action_id = action_role_obj.action_id
            role_id = action_role_obj.role_id
            action_roles_dict[action_id].append(role_id)

        return [
            ActionRolesDTO(
                action_id=key,
                roles=value
            )
            for key, value in action_roles_dict.items()
        ]

    def get_actions_dto(self, action_ids: List[int]) -> List[ActionDTO]:

        action_objs = StageAction.objects \
            .filter(id__in=action_ids) \
            .select_related('stage')

        return [
            ActionDTO(
                action_id=action_obj.id,
                name=action_obj.name,
                stage_id=action_obj.stage.stage_id,
                button_text=action_obj.button_text,
                button_color=action_obj.button_color
            )
            for action_obj in action_objs
        ]

    def get_action_roles(self, action_id: int) -> List[str]:

        action_permitted_role_objs = \
            ActionPermittedRoles.objects.filter(action_id=action_id)

        return [
            obj.role_id for obj in action_permitted_role_objs
        ]

    def validate_action(self, action_id: int) -> bool:

        return StageAction.objects.filter(id=action_id).exists()

    def get_enable_multiple_gofs_field_to_gof_ids(
            self, task_id: int, gof_ids: List[str]) -> List[GOFMultipleEnableDTO]:

        from ib_tasks.models import TaskTemplateGoFs
        task_obj = Task.objects.get(id=task_id)
        template_id = task_obj.template_id
        task_template_gofs = TaskTemplateGoFs.objects\
            .filter(gof_id__in=gof_ids, task_template_id=template_id)

        return [
            GOFMultipleEnableDTO(
                group_of_field_id=task_template_gof.gof_id,
                multiple_status=task_template_gof.enable_add_another_gof
            )
            for task_template_gof in task_template_gofs
        ]

    def get_global_constants_to_task(
            self, task_id: int) -> List[GlobalConstantsDTO]:

        from ib_tasks.models.task import Task
        task_obj = Task.objects.get(id=task_id)
        global_constant_objs = GlobalConstant.objects\
            .filter(task_template_id=task_obj.template_id)
        return [
            GlobalConstantsDTO(
                constant_name=global_constant_obj.name,
                value=global_constant_obj.value
            )
            for global_constant_obj in global_constant_objs
        ]

    def get_stage_dtos_to_task(self, task_id: int) -> List[StageValueDTO]:

        from ib_tasks.models.task import Task
        task_obj = Task.objects.get(id=task_id)
        stage_objs = Stage.objects.filter(task_template_id=task_obj.template_id)
        return [
            StageValueDTO(
                stage_id=stage_obj.stage_id,
                value=stage_obj.value
            )
            for stage_obj in stage_objs
        ]
