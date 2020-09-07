import datetime
from typing import List, Optional

from django.db.models import Q

from ib_tasks.constants.constants import ALL_ROLES_ID
from ib_tasks.constants.enum import PermissionTypes
from ib_tasks.interactors.global_constants_dtos import GlobalConstantsDTO
from ib_tasks.interactors.stages_dtos import StageDTO, \
    TaskIdWithStageAssigneeDTO, StageAssigneeDTO
from ib_tasks.interactors.storage_interfaces.actions_dtos import ActionDTO, \
    ActionRolesDTO
from ib_tasks.interactors.storage_interfaces.fields_dtos import \
    FieldWritePermissionRolesDTO
from ib_tasks.interactors.storage_interfaces.gof_dtos import \
    GOFMultipleEnableDTO, GoFWritePermissionRolesDTO
from ib_tasks.interactors.storage_interfaces.stage_dtos import \
    StageDisplayValueDTO, StageValueWithTaskIdsDTO, \
    TaskIdWithStageDetailsDTO, \
    TaskStagesDTO, StageValueDTO, TaskTemplateStageDTO, StageRoleDTO, \
    StageDetailsDTO, TaskStageHavingAssigneeIdDTO, TaskWithDbStageIdDTO, \
    StageIdWithValueDTO
from ib_tasks.interactors.storage_interfaces.stages_storage_interface import \
    StageStorageInterface
from ib_tasks.interactors.storage_interfaces.storage_interface import (
    StorageInterface, StatusVariableDTO
)
from ib_tasks.interactors.storage_interfaces.task_dtos import TaskDueMissingDTO
from ib_tasks.interactors.task_dtos import GetTaskDetailsDTO, \
    TaskDelayParametersDTO
from ib_tasks.models import GoFRole, TaskStatusVariable, Task, \
    GlobalConstant, \
    StagePermittedRoles, TaskTemplateInitialStage, Stage, \
    TaskTemplateStatusVariable, ProjectTaskTemplate, ActionPermittedRoles, \
    StageAction, CurrentTaskStage, FieldRole, TaskStageHistory, TaskStageRp
from ib_tasks.models.user_task_delay_reason import UserTaskDelayReason


class StagesStorageImplementation(StageStorageInterface):

    def get_stage_display_name_for_stage_id(self, stage_id: int) -> str:
        stage_display_name = Stage.objects.get(id=stage_id).display_name
        return stage_display_name

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

    def get_existing_status_ids(self, status_ids: List[str]):
        status = TaskTemplateStatusVariable.objects.filter(
            variable__in=status_ids
        ).values_list('variable', flat=True)
        return list(status)

    def get_stage_detail_dtos_given_stage_ids(self, stage_ids: List[str]) -> \
            List[StageDetailsDTO]:
        stage_objs = Stage.objects.filter(stage_id__in=stage_ids).values(
            'id', 'stage_id', 'display_name', 'stage_color')
        stage_detail_dtos = [StageDetailsDTO(db_stage_id=stage_obj['id'],
                                             stage_id=stage_obj['stage_id'],
                                             name=stage_obj['display_name'],
                                             color=stage_obj['stage_color'])
                             for stage_obj in stage_objs]
        return stage_detail_dtos

    def get_stage_ids_excluding_virtual_stages(
            self, stage_ids: List[str]) -> List[str]:
        stage_ids = list(Stage.objects.filter(stage_id__in=stage_ids).exclude(
            value=-1).values_list('stage_id', flat=True))
        return stage_ids

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

    def get_permitted_stage_ids(
            self, user_role_ids: List[str], project_id: Optional[str]
    ) -> List[str]:

        project_template_ids = ProjectTaskTemplate.objects.filter(
            project_id=project_id, task_template__is_transition_template=False
        ).values_list('task_template_id', flat=True)
        stage_ids = StagePermittedRoles.objects.filter(
            (Q(role_id__in=user_role_ids) | Q(role_id=ALL_ROLES_ID)) &
            Q(stage__task_template_id__in=project_template_ids)
        ).values_list('stage__stage_id', flat=True)

        return list(stage_ids)

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

    def get_valid_db_stage_ids_with_stage_value(
            self, stage_ids: List[int]) -> List[StageIdWithValueDTO]:

        stage_objs = list(
            Stage.objects.filter(id__in=stage_ids).
                values('id', 'value'))
        stage_dtos = [StageIdWithValueDTO(db_stage_id=stage_obj['id'],
                                          stage_value=stage_obj['value']) for
                      stage_obj in stage_objs]
        return stage_dtos

    def get_stage_details(self, task_dtos: List[GetTaskDetailsDTO]) -> \
            List[TaskTemplateStageDTO]:
        task_ids = [task.task_id for task in task_dtos]
        task_objs = Task.objects.filter(id__in=task_ids).values(
            'id', 'template_id')
        template_stage_ids_list = []
        task_template_dict = {}
        for item in task_objs:
            task_template_dict[item['id']] = item['template_id']
        for task in task_dtos:
            template_stage_ids_list.append(
                TaskTemplateStageDTO(task_id=task.task_id,
                                     task_template_id=task_template_dict[
                                         task.task_id],
                                     stage_id=task.stage_id))
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
            task_ids_group_by_stage_value_dtos: List[
                StageValueWithTaskIdsDTO]
    ) -> List[TaskIdWithStageDetailsDTO]:

        query = None
        for item in task_ids_group_by_stage_value_dtos:
            current_queue = Q(stage__value=item.stage_value,
                              task_id__in=item.task_ids)
            if query is None:
                query = current_queue
            else:
                query = query | current_queue
        if query is None:
            return []
        current_stage_objects = CurrentTaskStage.objects.filter(
            query
        ).values(
            "task_id", "task__task_display_id",
            "stage__stage_id", "stage__display_name",
            "stage__stage_color", "stage__id"
        )
        all_task_id_with_stage_details_dtos = [
            self._get_task_id_with_stage_details_dtos(
                task_id_with_stage_details=current_stage_object
            )
            for current_stage_object in current_stage_objects
        ]
        return all_task_id_with_stage_details_dtos

    @staticmethod
    def _get_task_id_with_stage_details_dtos(
            task_id_with_stage_details: dict
    ) -> TaskIdWithStageDetailsDTO:
        task_id_with_stage_details_dtos = TaskIdWithStageDetailsDTO(
            task_id=task_id_with_stage_details["task_id"],
            task_display_id=task_id_with_stage_details[
                "task__task_display_id"],
            stage_id=task_id_with_stage_details["stage__stage_id"],
            stage_display_name=task_id_with_stage_details[
                "stage__display_name"],
            stage_color=task_id_with_stage_details["stage__stage_color"],
            db_stage_id=task_id_with_stage_details["stage__id"]
        )
        return task_id_with_stage_details_dtos

    def create_task_stage_assignees(
            self, task_id_with_stage_assignee_dtos: List[
                TaskIdWithStageAssigneeDTO]):
        task_stage_objs = [
            TaskStageHistory(
                task_id=each_task_id_with_stage_assignee_dto.task_id,
                stage_id=each_task_id_with_stage_assignee_dto.db_stage_id,
                assignee_id=each_task_id_with_stage_assignee_dto.assignee_id,
                team_id=each_task_id_with_stage_assignee_dto.team_id)
            for each_task_id_with_stage_assignee_dto in
            task_id_with_stage_assignee_dtos
        ]
        TaskStageHistory.objects.bulk_create(task_stage_objs)
        return

    @staticmethod
    def _get_matching_task_stage_dto(
            stage_id: int, task_id_with_stage_assignee_dtos_for_updation):
        for each_task_id_with_stage_assignee_dto in \
                task_id_with_stage_assignee_dtos_for_updation:
            stage_id_matched = stage_id == \
                               each_task_id_with_stage_assignee_dto.db_stage_id
            if stage_id_matched:
                return each_task_id_with_stage_assignee_dto
        return

    def get_task_stage_ids_in_given_stage_ids(self, task_id: int,
                                              stage_ids: List[int]) -> \
            List[str]:
        task_stage_ids = \
            list(CurrentTaskStage.objects.filter(task_id=task_id,
                                                 stage_id__in=stage_ids). \
                 values_list('stage_id', flat=True))
        return task_stage_ids

    def get_stage_details_having_assignees_in_given_stage_ids(
            self, task_id: int, db_stage_ids: List[int]) -> List[
        TaskStageHavingAssigneeIdDTO]:

        task_stage_objs = list(TaskStageHistory.objects.filter(task_id=task_id,
                                                               stage_id__in=db_stage_ids). \
                               values('stage_id', 'assignee_id',
                                      'stage__display_name'))
        stages_having_assignee_dtos = [TaskStageHavingAssigneeIdDTO(
            assignee_id=task_stage_obj['assignee_id'],
            db_stage_id=task_stage_obj['stage_id'],
            stage_display_name=task_stage_obj['stage__display_name']) for
            task_stage_obj in task_stage_objs]
        return stages_having_assignee_dtos

    def update_task_stages_other_than_matched_stages_with_left_at_status(
            self, task_id: int, db_stage_ids: List[int]):
        task_stage_objs = TaskStageHistory.objects \
            .filter(task_id=task_id, left_at__isnull=True) \
            .exclude(stage_id__in=db_stage_ids)
        for each_task_stage_obj in task_stage_objs:
            each_task_stage_obj.left_at = datetime.datetime.now()
        TaskStageHistory.objects.bulk_update(
            task_stage_objs, ['left_at']
        )

    def get_task_stages_assignees_without_having_left_at_status(
            self, task_id: int, db_stage_ids: List[int]) -> List[
        StageAssigneeDTO]:
        task_stage_objs = list(TaskStageHistory.objects.filter(
            task_id=task_id,
            stage_id__in=db_stage_ids, left_at__isnull=True)
                               .values('stage_id', 'assignee_id', 'team_id'))
        stages_having_assignee_dtos = [StageAssigneeDTO(
            assignee_id=task_stage_obj['assignee_id'],
            db_stage_id=task_stage_obj['stage_id'],
            team_id=task_stage_obj['team_id']) for
            task_stage_obj in task_stage_objs]
        return stages_having_assignee_dtos

    def get_valid_template_ids(self, template_ids: List[str]) -> List[str]:
        from ib_tasks.models import TaskTemplate
        valid_template_ids = TaskTemplate.objects.filter(
            template_id__in=template_ids
        ).values_list('template_id', flat=True)
        return valid_template_ids

    def get_db_stage_ids_for_given_stage_ids(
            self, stage_ids: List[str]) -> List[int]:
        db_stage_ids = list(
            Stage.objects.filter(stage_id__in=stage_ids).values_list('id',
                                                                     flat=True))
        return db_stage_ids

    def get_virtual_stages_already_having_in_task(
            self, task_id: int, stage_ids_having_virtual_stages: List[str]) \
            -> \
                    List[str]:
        virtual_stages_already_having_task = list(
            TaskStageHistory.objects.filter(task_id=task_id,
                                            stage__stage_id__in=stage_ids_having_virtual_stages,
                                            left_at__isnull=True)
                .values_list('stage__stage_id', flat=True))
        return virtual_stages_already_having_task

    def get_current_stages_of_all_tasks(self) -> List[TaskWithDbStageIdDTO]:
        task_stage_objs = list(
            CurrentTaskStage.objects.all().values('task_id', 'stage_id'))
        task_with_stage_id_dtos = [
            TaskWithDbStageIdDTO(task_id=task_stage_obj['task_id'],
                                 db_stage_id=task_stage_obj['stage_id']) for
            task_stage_obj in task_stage_objs]
        return task_with_stage_id_dtos

    def check_is_stage_exists(self, stage_id: int) -> bool:
        is_valid_stage_id = Stage.objects.filter(id=stage_id).exists()
        return is_valid_stage_id

    def get_stage_permitted_user_roles(self, stage_id: int) -> List[str]:
        permitted_user_role_ids_queryset = StagePermittedRoles.objects.filter(
            stage_id=stage_id).values_list('role_id', flat=True)

        permitted_user_role_ids_list = list(permitted_user_role_ids_queryset)
        return permitted_user_role_ids_list

    def get_stage_ids_having_actions(self, user_roles: List[str]) -> List[str]:
        stage_ids = ActionPermittedRoles.objects \
            .filter(
            Q(role_id__in=user_roles) | Q(role_id=ALL_ROLES_ID)
        ) \
            .values_list('action__stage_id', flat=True)
        stage_ids = StagePermittedRoles.objects.filter(
            stage_id__in=stage_ids) \
            .filter(
            Q(role_id__in=user_roles) | Q(role_id=ALL_ROLES_ID)
        ).values_list('stage__stage_id', flat=True)
        return sorted(list(set(stage_ids)))

    def get_task_current_stages(self, task_id: int) -> List[str]:
        return list(CurrentTaskStage.objects.filter(
            task_id=task_id
        ).values_list('stage__stage_id', flat=True))

    def get_current_stage_db_ids_of_task(self, task_id: int) -> List[int]:
        return list(CurrentTaskStage.objects.filter(
            task_id=task_id
        ).values_list('stage__id', flat=True))

    def get_current_stages_of_task_in_given_stages(
            self, task_id: int, stage_ids: List[str]) -> List[str]:
        return list(CurrentTaskStage.objects.filter(
            task_id=task_id, stage__stage_id__in=stage_ids
        ).values_list('stage__stage_id', flat=True))


class StorageImplementation(StorageInterface):

    def get_write_permission_roles_for_given_gof_ids(
            self, gof_ids: List[str]
    ) -> List[GoFWritePermissionRolesDTO]:
        gof_role_objects = GoFRole.objects.filter(
            gof_id__in=gof_ids, permission_type=PermissionTypes.WRITE.value)
        gof_write_permission_roles_dtos = \
            self._prepare_gof_write_permission_roles_dtos(
                gof_role_objects, gof_ids)
        return gof_write_permission_roles_dtos

    def _prepare_gof_write_permission_roles_dtos(
            self, gof_role_objects: List[GoFRole], gof_ids: List[str]
    ) -> List[GoFWritePermissionRolesDTO]:
        gof_write_permission_roles_dtos = []
        for gof_id in gof_ids:
            gof_roles = self._get_matching_gof_role_object(
                gof_id, gof_role_objects)
            gof_roles_are_empty = not gof_roles
            if gof_roles_are_empty:
                gof_write_permission_roles_dtos.append(
                    GoFWritePermissionRolesDTO(gof_id=gof_id,
                                               write_permission_roles=[]))
            else:
                gof_write_permission_roles_dtos.append(
                    GoFWritePermissionRolesDTO(
                        gof_id=gof_id, write_permission_roles=gof_roles)
                )
        return gof_write_permission_roles_dtos

    @staticmethod
    def _get_matching_gof_role_object(
            gof_id, gof_role_objects) -> List[str]:
        gof_roles = []
        for gof_role_obj in gof_role_objects:
            gof_id_matched = gof_id == gof_role_obj.gof_id
            if gof_id_matched:
                gof_roles.append(gof_role_obj.role)
        return gof_roles

    def get_write_permission_roles_for_given_field_ids(
            self, field_ids: List[str]) -> List[FieldWritePermissionRolesDTO]:
        field_role_objects = FieldRole.objects.filter(
            field_id__in=field_ids, permission_type=PermissionTypes.WRITE.value
        )
        field_write_permission_roles_dtos = \
            self._prepare_field_write_permission_roles_dtos(
                field_role_objects, field_ids)
        return field_write_permission_roles_dtos

    def _prepare_field_write_permission_roles_dtos(
            self, field_role_objects: List[FieldRole], field_ids: List[str]
    ) -> List[FieldWritePermissionRolesDTO]:
        field_write_permission_roles_dtos = []
        for field_id in field_ids:
            field_roles = self._get_matching_field_role_object(
                field_id, field_role_objects)
            field_roles_are_empty = not field_roles
            if field_roles_are_empty:
                field_write_permission_roles_dtos.append(
                    FieldWritePermissionRolesDTO(field_id=field_id,
                                                 write_permission_roles=[]))
            else:
                field_write_permission_roles_dtos.append(
                    FieldWritePermissionRolesDTO(
                        field_id=field_id, write_permission_roles=field_roles)
                )
        return field_write_permission_roles_dtos

    @staticmethod
    def _get_matching_field_role_object(
            field_id, field_role_objects) -> List[str]:
        field_roles = []
        for field_role_obj in field_role_objects:
            field_id_matched = field_id == field_role_obj.field_id
            if field_id_matched:
                field_roles.append(field_role_obj.role)
        return field_roles

    def validate_task_id(self, task_id: int) -> bool:

        return Task.objects.filter(id=task_id).exists()

    def get_task_project_id(self, task_id: int) -> str:
        task = Task.objects.get(id=task_id)
        return task.project_id

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
                button_color=action_obj.button_color,
                action_type=action_obj.action_type,
                transition_template_id=action_obj.transition_template_id
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
            self, template_id: str) -> List[GOFMultipleEnableDTO]:

        from ib_tasks.models import TaskTemplateGoFs
        task_template_gofs = TaskTemplateGoFs.objects \
            .filter(task_template_id=template_id)
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

        CurrentTaskStage.objects.filter(task_id=task_id).delete()
        stage_dict = {
            obj.stage_id: obj
            for obj in Stage.objects.filter(stage_id__in=stage_ids)
        }

        task_stage_objs = [
            CurrentTaskStage(task_id=task_id, stage=stage_dict[stage_id])
            for stage_id in stage_ids
        ]
        CurrentTaskStage.objects.bulk_create(task_stage_objs)

    def get_task_present_stage_actions(self, task_id: int):

        task_stage_ids = CurrentTaskStage.objects.filter(task_id=task_id) \
            .values_list('stage_id', flat=True)
        action_ids = StageAction.objects.filter(stage_id__in=task_stage_ids) \
            .values_list('id', flat=True)
        return action_ids

    def validate_if_task_is_assigned_to_user_in_given_stage(self,
                                                            task_id: int,
                                                            user_id: str,
                                                            stage_id: int) \
            -> bool:
        is_assigned = TaskStageHistory.objects.filter(
            task_id=task_id, assignee_id=user_id, stage_id=stage_id
        ).exists()
        return is_assigned

    def get_task_due_details(self, task_id: int, stage_id: int) -> \
            List[TaskDueMissingDTO]:
        task_due_objects = (
            UserTaskDelayReason.objects.filter(
                task_id=task_id, stage_id=stage_id
            ).values('due_datetime', 'count', 'reason', 'user_id',
                     'task__task_display_id'))

        task_due_details_dtos = self._convert_task_due_details_objs_to_dtos(
            task_due_objects)
        return task_due_details_dtos

    @staticmethod
    def _convert_task_due_details_objs_to_dtos(task_due_objs):
        task_due_details_dtos = []
        for task in task_due_objs:
            task_due_details_dtos.append(
                TaskDueMissingDTO(
                    task_id=task['task__task_display_id'],
                    due_date_time=task['due_datetime'],
                    due_missed_count=task['count'],
                    reason=task['reason'],
                    user_id=task['user_id']
                )
            )
        return task_due_details_dtos

    def add_due_delay_details(self, due_details: TaskDelayParametersDTO):
        user_id = due_details.user_id
        task_id = due_details.task_id
        reason_id = due_details.reason_id
        stage_id = due_details.stage_id
        updated_due_datetime = due_details.due_date_time
        count = UserTaskDelayReason.objects.filter(
            task_id=task_id, user_id=user_id).count()

        UserTaskDelayReason.objects.create(user_id=user_id, task_id=task_id,
                                           due_datetime=updated_due_datetime,
                                           count=count + 1,
                                           reason_id=reason_id,
                                           stage_id=stage_id,
                                           reason=due_details.reason)

    def validate_stage_id(self, stage_id: int) -> bool:
        does_exists = Stage.objects.filter(id=stage_id).exists()
        return does_exists

    def get_due_missed_count(self, task_id: int, user_id: str,
                             stage_id: str) -> int:
        count = UserTaskDelayReason.objects.filter(
            task_id=task_id, stage__stage_id=stage_id, user_id=user_id
        ).count()
        return count

    def get_latest_rp_id_if_exists(self, task_id: int,
                                   stage_id: int) -> Optional[str]:
        rp_ids = TaskStageRp.objects.filter(
            task_id=task_id, stage_id=stage_id
        ).values_list('rp_id', flat=True).order_by('-id')
        if not rp_ids:
            return None
        return rp_ids[0]

    def get_rp_ids(self, task_id: int, stage_id: int) -> \
            List[str]:
        rp_ids = list(TaskStageRp.objects.filter(
            task_id=task_id, stage_id=stage_id
        ).values_list('rp_id', flat=True).order_by('id'))
        return rp_ids

    def add_superior_to_db(
            self, task_id: int, stage_id: int, superior_id: str):
        TaskStageRp.objects.get_or_create(
            task_id=task_id, stage_id=stage_id, rp_id=superior_id)

    def get_latest_rp_added_datetime(self,
                                     task_id: int, stage_id: int) -> Optional[
        str]:
        objs = TaskStageRp.objects.filter(
            task_id=task_id, stage_id=stage_id
        ).values_list('added_at', flat=True).order_by('-added_at')
        if objs:
            return objs[0]
        return None

    def update_task_due_datetime(self, due_details: TaskDelayParametersDTO):
        task_id = due_details.task_id
        updated_due_datetime = due_details.due_date_time

        Task.objects.filter(pk=task_id).update(due_date=updated_due_datetime)
