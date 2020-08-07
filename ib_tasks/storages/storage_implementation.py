from typing import List
from typing import Optional

from ib_tasks.constants.enum import PermissionTypes
from ib_tasks.interactors.global_constants_dtos import GlobalConstantsDTO
from ib_tasks.interactors.stages_dtos import StageActionDTO, \
    TaskIdWithStageAssigneeDTO
from ib_tasks.interactors.stages_dtos import StageDTO
from ib_tasks.interactors.stages_dtos import TemplateStageDTO
from ib_tasks.interactors.storage_interfaces.actions_dtos import ActionDTO, \
    ActionRolesDTO
from ib_tasks.interactors.storage_interfaces.fields_dtos import FieldValueDTO, \
    FieldWritePermissionRolesDTO
from ib_tasks.interactors.storage_interfaces.gof_dtos import \
    GOFMultipleEnableDTO, GoFWritePermissionRolesDTO
from ib_tasks.interactors.storage_interfaces.stage_dtos import \
    StageRoleDTO, StageDisplayValueDTO, StageValueWithTaskIdsDTO, \
    TaskIdWithStageDetailsDTO
from ib_tasks.interactors.storage_interfaces.stage_dtos import TaskStagesDTO, \
    StageValueDTO
from ib_tasks.interactors.storage_interfaces.stage_dtos import \
    TaskTemplateStageDTO
from ib_tasks.interactors.storage_interfaces.stages_storage_interface import \
    StageStorageInterface
from ib_tasks.interactors.storage_interfaces.storage_interface import (
    StorageInterface, GroupOfFieldsDTO,
    StatusVariableDTO, StageActionNamesDTO
)
from ib_tasks.interactors.task_dtos import GetTaskDetailsDTO
from ib_tasks.models import GoFRole, TaskStatusVariable, Task, \
    ActionPermittedRoles, StageAction, TaskStage, FieldRole, GlobalConstant, \
    StagePermittedRoles
from ib_tasks.models import TaskTemplateInitialStage, Stage


class StagesStorageImplementation(StageStorageInterface):
    def create_stages(self, stage_information: List[StageDTO]):
        list_of_stages = []
        for stage in stage_information:
            list_of_stages.append(self._get_stage_object(stage))
        Stage.objects.bulk_create(list_of_stages)
        list_of_stage_ids = [stage.stage_id for stage in stage_information]
        stages = Stage.objects.filter(stage_id__in=list_of_stage_ids)
        list_of_permitted_roles = self._get_list_of_permitted_roles_objs(
            stages, stage_information)
        StagePermittedRoles.objects.bulk_create(list_of_permitted_roles)

    @staticmethod
    def _get_list_of_permitted_roles_objs(stage_objs,
                                          stage_dtos):
        stage_roles = {}
        for stage in stage_dtos:
            stage_roles[stage.stage_id] = stage.roles.split('\n')

        list_of_permitted_roles = []
        for stage_obj in stage_objs:
            roles = stage_roles[stage_obj.stage_id]
            for role in roles:
                list_of_permitted_roles.append(
                    StagePermittedRoles(stage=stage_obj,
                                        role_id=role))
        return list_of_permitted_roles

    def get_allowed_stage_ids_of_user(self) -> List[str]:
        stage_ids = list(
            Stage.objects.all().values_list('stage_id', flat=True))
        return stage_ids

    @staticmethod
    def _get_stage_object(stage):
        return Stage(stage_id=stage.stage_id,
                     display_name=stage.stage_display_name,
                     task_template_id=stage.task_template_id,
                     value=stage.value,
                     card_info_kanban=stage.card_info_kanban,
                     card_info_list=stage.card_info_list,
                     stage_color=stage.stage_color,
                     display_logic=stage.stage_display_logic)

    def get_existing_stage_ids(self, stage_ids: List[str]) -> Optional[
        List[str]]:
        valid_stage_ids = Stage.objects.filter(
            stage_id__in=stage_ids
        ).values_list('stage_id', flat=True)
        return list(valid_stage_ids)

    def get_valid_stage_ids_in_given_stage_ids(self, stage_ids: List[str]) -> \
            List[str]:

        stage_ids = list(
            Stage.objects.filter(stage_id__in=stage_ids).
                values_list('stage_id', flat=True))
        return stage_ids

    def get_valid_db_stage_ids_in_given_db_stage_ids(self,
                                                     stage_ids: List[int]) -> \
            List[int]:

        stage_ids = list(
            Stage.objects.filter(id__in=stage_ids).
                values_list('id', flat=True))
        return stage_ids

    def get_stage_details(self, task_dtos: List[GetTaskDetailsDTO]) -> \
            List[TaskTemplateStageDTO]:
        task_ids = [task.task_id for task in task_dtos]
        task_objs = Task.objects.filter(id__in=task_ids).values(
            'id', 'template_id')
        template_stage_ids_list = []
        task_stages_dict = {}
        for item in task_dtos:
            task_stages_dict[item.task_id] = item.stage_id
        for task in task_objs:
            template_stage_ids_list.append(
                TaskTemplateStageDTO(task_id=task['id'],
                                     task_template_id=task['template_id'],
                                     stage_id=task_stages_dict[task['id']]))
        return template_stage_ids_list

    def update_stages(self,
                      update_stages_information: List[StageDTO]):
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
                stage, stage_objects_dict[stage.stage_id]))

        Stage.objects.bulk_update(list_of_stages,
                                  ['task_template_id', 'stage_color',
                                   'value', 'display_name', 'display_logic'])

        list_of_stage_ids = [stage.stage_id
                             for stage in update_stages_information]
        stages = Stage.objects.filter(stage_id__in=list_of_stage_ids)
        list_of_permitted_roles = self._get_list_of_permitted_roles_objs(
            stages, update_stages_information)
        StagePermittedRoles.objects.bulk_create(list_of_permitted_roles)

    @staticmethod
    def _get_update_stage_object(stage, stage_object):
        stage_object.display_name = stage.stage_display_name
        stage_object.value = stage.value
        stage_object.card_info_kanban = stage.card_info_kanban
        stage_object.card_info_list = stage.card_info_list
        stage_object.display_logic = stage.stage_display_logic
        return stage_object

    def validate_stages_related_task_template_ids(self,
                                                  task_stages_dto:
                                                  List[TaskStagesDTO]) -> \
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

    def get_stage_role_dtos_given_db_stage_ids(self,
                                               db_stage_ids: List[int]) -> \
            List[StageRoleDTO]:
        stage_roles = list(
            StagePermittedRoles.objects.filter(
                stage_id__in=db_stage_ids).values(
                'stage_id', 'role_id'))
        stage_role_dtos = [
            StageRoleDTO(db_stage_id=each_stage_role['stage_id'],
                         role_id=each_stage_role['role_id']) for
            each_stage_role in stage_roles]
        return stage_role_dtos

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

    def get_task_id_with_stage_details_dtos_based_on_stage_value(
            self, stage_values: List[int],
            task_ids_group_by_stage_value_dtos: List[StageValueWithTaskIdsDTO],
            user_id: str) -> List[TaskIdWithStageDetailsDTO]:
        # ToDo: Need to optimize the storage calls which are in for loop
        all_task_id_with_stage_details_dtos = []
        for each_stage_value in stage_values:
            for each_task_ids_group_by_stage_value_dto in \
                    task_ids_group_by_stage_value_dtos:
                if each_task_ids_group_by_stage_value_dto.stage_value \
                        == each_stage_value:
                    task_id_with_stage_details = list(
                        TaskStage.objects.filter(
                            task__created_by=user_id,
                            stage__value=each_stage_value,
                            task_id__in=each_task_ids_group_by_stage_value_dto.
                                task_ids).values("task_id", "stage__stage_id",
                                                 "stage__display_name"))

                    task_id_with_stage_details_dtos = self. \
                        _get_task_id_with_stage_details_dtos(
                        task_id_with_stage_details)

                    all_task_id_with_stage_details_dtos.extend(
                        task_id_with_stage_details_dtos)
        return all_task_id_with_stage_details_dtos

    @staticmethod
    def _get_task_id_with_stage_details_dtos(
            task_id_with_stage_details: List[dict]
    ) -> List[TaskIdWithStageDetailsDTO]:
        task_id_with_stage_details_dtos = [
            TaskIdWithStageDetailsDTO(
                task_id=task_id_with_stage_detail["task_id"],
                stage_id=task_id_with_stage_detail["stage__stage_id"],
                stage_display_name=task_id_with_stage_detail[
                    "stage__display_name"])
            for task_id_with_stage_detail in task_id_with_stage_details
        ]
        return task_id_with_stage_details_dtos

    def create_task_stage_assignees(
            self, task_id_with_stage_assignee_dtos_for_creation: List[
                TaskIdWithStageAssigneeDTO]):
        task_stage_objs = [
            TaskStage(task_id=each_task_id_with_stage_assignee_dto.task_id,
                      stage_id=each_task_id_with_stage_assignee_dto.db_stage_id,
                      assignee_id=each_task_id_with_stage_assignee_dto.assignee_id)
            for each_task_id_with_stage_assignee_dto in
            task_id_with_stage_assignee_dtos_for_creation
        ]
        TaskStage.objects.bulk_create(task_stage_objs)
        return

    def update_task_stage_assignees(
            self, task_id_with_stage_assignee_dtos_for_updation: List[
                TaskIdWithStageAssigneeDTO]):
        for each_task_id_with_stage_assignee_dto in \
                task_id_with_stage_assignee_dtos_for_updation:
            task_id = each_task_id_with_stage_assignee_dto.task_id
        stage_ids = [each_task_id_with_stage_assignee_dto.db_stage_id
                     for each_task_id_with_stage_assignee_dto in
                     task_id_with_stage_assignee_dtos_for_updation]
        task_stage_objs = TaskStage.objects.filter(task_id=task_id,
                                                   stage_id__in=stage_ids)
        for each_task_stage_obj in task_stage_objs:
            task_stage_dto = self._get_matching_task_stage_dto(
                each_task_stage_obj.stage_id,
                task_id_with_stage_assignee_dtos_for_updation)
            each_task_stage_obj.assignee_id = task_stage_dto.assignee_id
        TaskStage.objects.bulk_update(
            task_stage_objs, ['assignee_id']
        )

    @staticmethod
    def _get_matching_task_stage_dto(
            stage_id: int, task_id_with_stage_assignee_dtos_for_updation):
        for each_task_id_with_stage_assignee_dto in \
                task_id_with_stage_assignee_dtos_for_updation:
            stage_id_matched = stage_id == each_task_id_with_stage_assignee_dto.db_stage_id
            if stage_id_matched:
                return each_task_id_with_stage_assignee_dto
        return

    def get_task_stage_ids_in_given_stage_ids(self, task_id: int,
                                              stage_ids: List[int]) -> \
            List[str]:
        task_stage_ids = \
            list(TaskStage.objects.filter(task_id=task_id,
                                          stage_id__in=stage_ids). \
                 values_list('stage_id', flat=True))
        return task_stage_ids


class StorageImplementation(StorageInterface):

    def get_write_permission_roles_for_given_gof_ids(self,
                                                     gof_ids: List[str]) -> \
            List[GoFWritePermissionRolesDTO]:
        gof_role_objects = GoFRole.objects.filter(
            gof_id__in=gof_ids, permission_type=PermissionTypes.WRITE.value)
        gof_write_permission_roles_dtos = \
            self._prepare_gof_write_permission_roles_dtos(gof_role_objects)
        return gof_write_permission_roles_dtos

    @staticmethod
    def _prepare_gof_write_permission_roles_dtos(
            gof_role_objects: List[GoFRole]) -> List[
        GoFWritePermissionRolesDTO]:
        from collections import defaultdict
        gof_roles_dict = defaultdict(list)
        for gof_role_obj in gof_role_objects:
            gof_roles_dict[gof_role_obj.gof_id].append(gof_role_obj.role)
        gof_write_permission_roles_dtos = [
            GoFWritePermissionRolesDTO(
                gof_id=gof_id, write_permission_roles=write_permission_roles
            )
            for gof_id, write_permission_roles in gof_roles_dict.items()
        ]
        return gof_write_permission_roles_dtos

    def get_write_permission_roles_for_given_field_ids(self,
                                                       field_ids: List[str]) -> \
            List[FieldWritePermissionRolesDTO]:
        field_role_objects = FieldRole.objects.filter(
            field_id__in=field_ids, permission_type=PermissionTypes.WRITE.value
        )
        field_write_permission_roles_dtos = \
            self._prepare_field_write_permission_roles_dtos(field_role_objects)
        return field_write_permission_roles_dtos

    @staticmethod
    def _prepare_field_write_permission_roles_dtos(
            field_role_objects: List[FieldRole]) -> List[
        FieldWritePermissionRolesDTO]:
        from collections import defaultdict
        field_roles_dict = defaultdict(list)
        for field_role_obj in field_role_objects:
            field_roles_dict[field_role_obj.field_id].append(
                field_role_obj.role)
        field_write_permission_roles_dtos = [
            FieldWritePermissionRolesDTO(
                field_id=field_id,
                write_permission_roles=write_permission_roles
            )
            for field_id, write_permission_roles in field_roles_dict.items()
        ]
        return field_write_permission_roles_dtos

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

    def update_status_variables_to_task(
            self, task_id: int, status_variables_dto: List[StatusVariableDTO]):

        status_variable_objs = TaskStatusVariable.objects \
            .filter(task_id=task_id)
        status_variable_dict = \
            self._get_status_variable_dict(status_variable_objs)
        for status_variable_dto in status_variables_dto:
            status_obj = \
                status_variable_dict[status_variable_dto.status_id]
            status_obj.variable = status_variable_dto.status_variable
            status_obj.value = status_variable_dto.value
            status_obj.save()

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
            self, template_id: str, gof_ids: List[str]) -> List[
        GOFMultipleEnableDTO]:

        from ib_tasks.models import TaskTemplateGoFs
        task_template_gofs = TaskTemplateGoFs.objects \
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
        global_constant_objs = GlobalConstant.objects \
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
        stage_objs = Stage.objects.filter(
            task_template_id=task_obj.template_id)
        return [
            StageValueDTO(
                stage_id=stage_obj.stage_id,
                value=stage_obj.value
            )
            for stage_obj in stage_objs
        ]

    def get_task_template_stage_logic_to_task(
            self, task_id: int) -> List[StageDisplayValueDTO]:

        from ib_tasks.models.task import Task
        task_obj = Task.objects.get(id=task_id)
        stage_objs = Stage.objects.filter(
            task_template_id=task_obj.template_id)

        return [
            StageDisplayValueDTO(
                stage_id=stage_obj.stage_id,
                display_logic=stage_obj.display_logic,
                value=stage_obj.value
            )
            for stage_obj in stage_objs
        ]

    def update_task_stages(self, task_id: int, stage_ids: List[str]):

        TaskStage.objects.filter(task_id=task_id).delete()
        stage_dict = {
            obj.stage_id: obj
            for obj in Stage.objects.filter(stage_id__in=stage_ids)
        }

        task_stage_objs = [
            TaskStage(task_id=task_id, stage=stage_dict[stage_id])
            for stage_id in stage_ids
        ]
        TaskStage.objects.bulk_create(task_stage_objs)

    def get_task_present_stage_actions(self, task_id: int):

        task_stage_ids = TaskStage.objects.filter(task_id=task_id) \
            .values_list('stage_id', flat=True)
        action_ids = StageAction.objects.filter(stage_id__in=task_stage_ids) \
            .values_list('id', flat=True)
        return action_ids
