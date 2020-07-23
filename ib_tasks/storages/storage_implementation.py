from typing import Optional, List

from ib_tasks.interactors.dtos import StageDTO, StageActionDTO, TaskTemplateStageDTO
from ib_tasks.interactors.storage_interfaces.dtos import (TaskStagesDTO, ValidStageDTO)
from ib_tasks.interactors.storage_interfaces.stages_storage_interface import StageStorageInterface
from ib_tasks.models import Stage


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

    def get_existing_stage_ids(self, stage_ids) -> Optional[List[str]]:
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



from typing import List
from ib_tasks.interactors.storage_interfaces.dtos import (
    FieldValueDTO, GOFMultipleEnableDTO, ActionRolesDTO, ActionDTO
)
from ib_tasks.interactors.storage_interfaces.storage_interface \
    import StorageInterface, GroupOfFieldsDTO, StatusVariableDTO, StageActionNamesDTO
from ib_tasks.models import *


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
            self, task_template_stage_dtos: List[TaskTemplateStageDTO]):
        pass

    
    def get_valid_task_template_ids(self, task_template_ids: List[str]):
        pass

    def validate_task_id(self, task_id: str) -> bool:
        # return Task.objects.filter(id=task_id).exists()
        pass


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

        status_variable_objs = TaskStatusVariable.objects\
            .filter(task_id=task_id)

        return [
            StatusVariableDTO(
                status_id=status_variable_obj.id,
                status_variable=status_variable_obj.variable,
                value=status_variable_obj.value
            ) for status_variable_obj in status_variable_objs
        ]

    def get_path_name_to_action(self, action_id: str) -> str:

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

        action_objs = StageAction.objects\
            .filter(id__in=action_ids)\
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
        pass
    
    def validate_action(self, action_id: int) -> bool:
        pass

    def get_enable_multiple_gofs_field_to_gof_ids(
            self, gof_ids: List[str]) -> List[GOFMultipleEnableDTO]:
        pass
