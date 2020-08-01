from collections import defaultdict
from typing import List, Optional, Dict, Tuple

from django.db.models import Q

from ib_tasks.interactors.global_constants_dtos import GlobalConstantsDTO
from ib_tasks.interactors.gofs_dtos import GoFWithOrderAndAddAnotherDTO
from ib_tasks.interactors.storage_interfaces.actions_dtos import \
    ActionsOfTemplateDTO, ActionDTO
from ib_tasks.interactors.storage_interfaces.fields_dtos import FieldDTO, \
    FieldRoleDTO, FieldTypeDTO, UserFieldPermissionDTO, FieldDetailsDTO, FieldCompleteDetailsDTO
from ib_tasks.interactors.storage_interfaces.get_task_dtos import TemplateFieldsDTO

from ib_tasks.interactors.storage_interfaces.stage_dtos import \
    TaskIdWithStageValueDTO, \
    TaskIdWithStageDetailsDTO, StageValueWithTaskIdsDTO
from ib_tasks.interactors.storage_interfaces.gof_dtos import GoFDTO, \
    GoFRoleDTO, GoFToTaskTemplateDTO
from ib_tasks.interactors.storage_interfaces.stage_dtos import TaskStagesDTO, \
    StageDTO, GetTaskStageCompleteDetailsDTO, TaskStageIdsDTO

from ib_tasks.interactors.storage_interfaces.status_dtos import \
    TaskTemplateStatusDTO
from ib_tasks.interactors.storage_interfaces.stage_dtos import TaskStagesDTO, \
    StageDTO
from ib_tasks.interactors.storage_interfaces.status_dtos import \
    TaskTemplateStatusDTO
from ib_tasks.interactors.storage_interfaces.task_storage_interface import \
    TaskStorageInterface
from ib_tasks.interactors.storage_interfaces.task_templates_dtos import \
    TaskTemplateDTO
from ib_tasks.interactors.task_dtos import GetTaskDetailsDTO, CreateTaskLogDTO
from ib_tasks.models import GoFRole, GoF, TaskStage
from ib_tasks.models import Stage, StageAction
from ib_tasks.models import TaskTemplateStatusVariable
from ib_tasks.models.field import Field
from ib_tasks.models.field_role import FieldRole
from ib_tasks.models.task_template import TaskTemplate
from ib_tasks.models.stage_actions import StageAction
from ib_tasks.models.task_template_gofs import TaskTemplateGoFs
from ib_tasks.models.task import Task
from ib_tasks.models.task_gof_field import TaskGoFField


class TasksStorageImplementation(TaskStorageInterface):

    def get_field_details_for_given_field_ids(self, field_ids: List[str]) -> \
            List[FieldCompleteDetailsDTO]:
        field_objects = list(
            Field.objects.filter(field_id__in=field_ids)
        )
        field_details_dtos = self._prepare_field_details_dtos(field_objects)
        return field_details_dtos

    @staticmethod
    def _prepare_field_details_dtos(
            field_objects: List[Field]) -> List[FieldCompleteDetailsDTO]:
        field_details_dtos = [
            FieldCompleteDetailsDTO(
                field_id=field_object.field_id,
                field_type=field_object.field_type,
                required=field_object.required,
                field_values=field_object.field_values,
                allowed_formats=field_object.allowed_formats,
                validation_regex=field_object.validation_regex
            )
            for field_object in field_objects
        ]
        return field_details_dtos

    def get_field_types_for_given_field_ids(self, field_ids: List[str]) -> \
            List[FieldCompleteDetailsDTO]:
        field_type_dicts = list(
            Field.objects.filter(field_id__in=field_ids). \
                values('field_id', 'field_type')
        )
        field_type_dtos = self._prepare_field_type_dtos(field_type_dicts)
        return field_type_dtos

    @staticmethod
    def _prepare_field_type_dtos(field_type_dicts: List[Dict]):
        field_type_dtos = [
            FieldCompleteDetailsDTO(field_id=field_type_dict['field_id'],
                                    field_type=field_type_dict['field_type'])
            for field_type_dict in field_type_dicts
        ]
        return field_type_dtos

    def get_task_template_name_if_exists(self, template_id: str) -> str:
        pass

    def create_task_template(self, template_id: str, template_name: str):
        from ib_tasks.models.task_template import TaskTemplate
        TaskTemplate.objects.create(template_id=template_id,
                                    name=template_name)

    def update_task_template(self, template_id: str, template_name: str):
        from ib_tasks.models.task_template import TaskTemplate
        task_template = \
            TaskTemplate.objects.get(template_id=template_id)
        task_template.name = template_name
        task_template.save()

    def get_task_template_name(self, template_id: str) -> str:
        from ib_tasks.models.task_template import TaskTemplate
        template_name_query_set = \
            TaskTemplate.objects.filter(
                template_id=template_id
            ).values_list('name', flat=True)
        return template_name_query_set.first()

    def get_task_template_ids(self) -> List[str]:
        pass

    def create_fields(self, field_dtos: List[FieldDTO]):
        from ib_tasks.models.field import Field
        fields = self._get_fields(field_dtos)
        Field.objects.bulk_create(fields)

    def get_valid_template_ids_in_given_template_ids(
            self, template_ids: List[str]) -> List[str]:
        from ib_tasks.models.task_template import TaskTemplate
        valid_template_ids = list(
            TaskTemplate.objects.filter(pk__in=template_ids).values_list(
                "template_id", flat=True))
        return valid_template_ids

    def get_existing_gof_ids_in_given_gof_ids(self,
                                              gof_ids: List[str]) -> List[str]:
        from ib_tasks.models.gof import GoF
        existing_gof_ids = list(
            GoF.objects.filter(pk__in=gof_ids).values_list('gof_id',
                                                           flat=True))
        return existing_gof_ids

    def create_gofs(self, gof_dtos: List[GoFDTO]):
        from ib_tasks.models.gof import GoF
        gof_objects = [
            GoF(gof_id=gof_dto.gof_id,
                display_name=gof_dto.gof_display_name,
                max_columns=gof_dto.max_columns) for gof_dto in gof_dtos
        ]
        GoF.objects.bulk_create(gof_objects)

    def create_gof_roles(self, gof_role_dtos: List[GoFRoleDTO]):
        from ib_tasks.models.gof_role import GoFRole
        gof_roles = [
            GoFRole(
                gof_id=gof_role_dto.gof_id,
                role=gof_role_dto.role,
                permission_type=gof_role_dto.permission_type
            )
            for gof_role_dto in gof_role_dtos
        ]
        GoFRole.objects.bulk_create(gof_roles)

    def update_gofs(self, gof_dtos: List[GoFDTO]):
        from ib_tasks.models.gof import GoF
        gof_ids = [gof_dto.gof_id for gof_dto in gof_dtos]
        gofs = GoF.objects.filter(pk__in=gof_ids)
        for gof in gofs:
            gof_dto = self._get_matching_gof_dto(gof.gof_id, gof_dtos)
            gof.display_name = gof_dto.gof_display_name
            gof.max_columns = gof_dto.max_columns
        GoF.objects.bulk_update(
            gofs, ['display_name', 'max_columns']
        )

    @staticmethod
    def _get_matching_gof_dto(gof_id: str,
                              gof_dtos: List[GoFDTO]) -> Optional[GoFDTO]:
        for gof_dto in gof_dtos:
            gof_id_matched = gof_id == gof_dto.gof_id
            if gof_id_matched:
                return gof_dto
        return

    def delete_gof_roles(self, gof_ids: List[str]):
        GoFRole.objects.filter(gof_id__in=gof_ids).delete()

    def check_is_template_exists(self, template_id: str) -> bool:
        is_template_exists = \
            TaskTemplate.objects.filter(template_id=template_id).exists()
        return is_template_exists

    def get_constant_names_of_existing_global_constants_of_template(
            self, template_id: str):

        from ib_tasks.models.global_constant import GlobalConstant
        constant_names_of_template = GlobalConstant.objects.filter(
            task_template_id=template_id).values_list('name', flat=True)

        constant_names_of_template_list = list(constant_names_of_template)
        return constant_names_of_template_list

    def create_global_constants_to_template(
            self, template_id: str,
            global_constants_dtos: List[GlobalConstantsDTO]):
        from ib_tasks.models.global_constant import GlobalConstant
        global_constants_objs = [
            GlobalConstant(task_template_id=template_id,
                           name=global_constants_dto.constant_name,
                           value=global_constants_dto.value)
            for global_constants_dto in global_constants_dtos
        ]
        GlobalConstant.objects.bulk_create(global_constants_objs)

    def update_fields(self, field_dtos: List[FieldDTO]):
        list_of_fields = [
            'display_name', 'gof_id',
            'required', 'field_type',
            'field_values', 'allowed_formats',
            'help_text', 'tooltip',
            'placeholder_text', 'error_messages',
            'validation_regex'
        ]
        fields = self._get_fields(field_dtos)
        Field.objects.bulk_update(fields, list_of_fields)

    def create_fields_roles(self, field_role_dtos: List[FieldRoleDTO]):
        fields_roles = self._get_fields_roles(field_role_dtos)
        FieldRole.objects.bulk_create(fields_roles)

    def get_existing_field_ids(self, field_ids: List[str]) -> List[str]:
        from ib_tasks.models.field import Field
        existing_field_ids = list(
            Field.objects.filter(
                field_id__in=field_ids
            ).values_list("field_id", flat=True)
        )
        return existing_field_ids

    def get_existing_gof_ids(self, gof_ids: List[str]) -> List[str]:
        from ib_tasks.models.gof import GoF
        existing_gof_ids = list(
            GoF.objects.filter(gof_id__in=gof_ids).values_list("gof_id",
                                                               flat=True))
        return existing_gof_ids

    @staticmethod
    def _get_fields(field_dtos: List[FieldDTO]):
        fields = [
            Field(
                field_id=field_dto.field_id,
                display_name=field_dto.field_display_name,
                required=field_dto.required,
                field_type=field_dto.field_type,
                field_values=field_dto.field_values,
                allowed_formats=field_dto.allowed_formats,
                help_text=field_dto.help_text,
                tooltip=field_dto.tooltip,
                placeholder_text=field_dto.placeholder_text,
                error_messages=field_dto.error_message,
                validation_regex=field_dto.validation_regex,
                gof_id=field_dto.gof_id
            )
            for field_dto in field_dtos
        ]
        return fields

    @staticmethod
    def _get_fields_roles(field_role_dtos):
        fields_roles = [
            FieldRole(
                field_id=field_role_dto.field_id,
                role=field_role_dto.role,
                permission_type=field_role_dto.permission_type
            )
            for field_role_dto in field_role_dtos
        ]
        return fields_roles

    def get_existing_template_ids(self):
        pass

    def get_existing_gof_ids_of_template(
            self, template_id: str) -> List[str]:
        from ib_tasks.models.task_template_gofs import TaskTemplateGoFs

        gof_ids_of_template_queryset = TaskTemplateGoFs.objects.filter(
            task_template_id=template_id
        ).values_list('gof_id', flat=True)

        gof_ids_of_template_list = list(gof_ids_of_template_queryset)
        return gof_ids_of_template_list

    def add_gofs_to_template(
            self, template_id: str,
            gof_dtos: List[GoFWithOrderAndAddAnotherDTO]):
        from ib_tasks.models.task_template_gofs import TaskTemplateGoFs
        gofs_to_template_objs = [
            TaskTemplateGoFs(
                task_template_id=template_id,
                gof_id=gof_dto.gof_id, order=gof_dto.order,
                enable_add_another_gof=gof_dto.enable_add_another_gof
            )
            for gof_dto in gof_dtos
        ]

        TaskTemplateGoFs.objects.bulk_create(gofs_to_template_objs)

    def update_gofs_to_template(
            self, template_id: str,
            gof_dtos: List[GoFWithOrderAndAddAnotherDTO]):

        gof_ids = self._get_gof_ids(gof_dtos=gof_dtos)
        gofs_dict = self._make_gofs_dict(gof_dtos=gof_dtos)
        from ib_tasks.models.task_template_gofs import TaskTemplateGoFs

        gof_to_task_template_objs = TaskTemplateGoFs.objects.filter(
            gof_id__in=gof_ids, task_template_id=template_id)
        for gof_to_task_template_obj in gof_to_task_template_objs:
            gof_to_task_template_obj.order = \
                gofs_dict[gof_to_task_template_obj.gof_id].order
            gof_to_task_template_obj.enable_add_another_gof = \
                gofs_dict[
                    gof_to_task_template_obj.gof_id].enable_add_another_gof

        TaskTemplateGoFs.objects.bulk_update(
            gof_to_task_template_objs, ['order', 'enable_add_another_gof'])

    def get_valid_gof_ids_in_given_gof_ids(self,
                                           gof_ids: List[str]) -> List[str]:
        from ib_tasks.models.gof import GoF
        gof_ids_queryset = GoF.objects.filter(gof_id__in=gof_ids).values_list(
            'gof_id', flat=True)

        gof_ids_list = list(gof_ids_queryset)
        return gof_ids_list

    def get_gof_dtos_for_given_gof_ids(self,
                                       gof_ids: List[str]) -> List[GoFDTO]:
        gofs = GoF.objects.filter(pk__in=gof_ids)
        gof_dtos = self._prepare_gof_dtos(gofs)
        return gof_dtos

    @staticmethod
    def _prepare_gof_dtos(gofs: List[GoF]):
        gof_dtos = [
            GoFDTO(gof_id=gof.gof_id,
                   gof_display_name=gof.display_name,
                   max_columns=gof.max_columns) for gof in gofs
        ]
        return gof_dtos

    def create_status_for_tasks(
            self, create_status_for_tasks: List[TaskTemplateStatusDTO]):
        list_of_status_tasks = [
            TaskTemplateStatusVariable(
                variable=status.status_variable_id,
                task_template_id=status.task_template_id)
            for status in create_status_for_tasks
        ]

        TaskTemplateStatusVariable.objects.bulk_create(list_of_status_tasks)

    def update_global_constants_to_template(
            self, template_id: str,
            global_constants_dtos: List[GlobalConstantsDTO]):

        global_constants_names = self._get_global_constant_names(
            global_constants_dtos=global_constants_dtos)
        global_constants_dict = self._make_global_constants_dict(
            global_constants_dtos=global_constants_dtos)

        from ib_tasks.models.global_constant import GlobalConstant
        global_constants_objs = GlobalConstant.objects.filter(
            name__in=global_constants_names, task_template_id=template_id)
        for global_constant_obj in global_constants_objs:
            global_constant_obj.value = \
                global_constants_dict[global_constant_obj.name].value

        GlobalConstant.objects.bulk_update(global_constants_objs, ['value'])

    def get_task_templates_dtos(self) -> List[TaskTemplateDTO]:
        task_template_objs = TaskTemplate.objects.all()
        task_template_dtos = self._convert_task_templates_objs_to_dtos(
            task_template_objs=task_template_objs)
        return task_template_dtos

    def get_initial_stage_ids_of_templates(self) -> List[int]:
        from ib_tasks.models.task_template_initial_stages import \
            TaskTemplateInitialStage
        templates_initial_stage_ids_queryset = \
            TaskTemplateInitialStage.objects.all().\
            values_list('stage_id', flat=True)
        templates_initial_stage_ids = \
            list(templates_initial_stage_ids_queryset)
        return templates_initial_stage_ids

    def get_actions_for_given_stage_ids(
            self, stage_ids: List[int]) -> List[ActionsOfTemplateDTO]:
        stage_actions_details = StageAction.objects.filter(
            stage_id__in=stage_ids
        ).select_related('stage').values(
            'id', 'button_text', 'button_color', 'stage__task_template_id'
        )

        actions_of_templates_dtos = self._convert_stage_actions_details_to_dto(
            stage_actions_details=stage_actions_details)
        return actions_of_templates_dtos

    def get_gofs_details_dtos(self, gof_ids: List[str]) -> List[GoFDTO]:
        gof_details = GoF.objects.filter(gof_id__in=gof_ids).values(
            'gof_id', 'max_columns', 'display_name')
        gof_dtos = self._convert_gof_details_to_dtos(gof_details=gof_details)
        return gof_dtos

    def get_gofs_to_task_templates_from_permitted_gofs(
            self, gof_ids: List[str]) -> List[GoFToTaskTemplateDTO]:
        task_template_gofs = \
            TaskTemplateGoFs.objects.filter(gof_id__in=gof_ids)
        gof_to_task_template_dtos = self._convert_task_template_gofs_to_dtos(
            task_template_gofs=task_template_gofs)
        return gof_to_task_template_dtos

    def get_user_field_permission_dtos(
            self, roles: List[str],
            field_ids: List[str]) -> List[UserFieldPermissionDTO]:
        from django.db.models import Q
        from ib_tasks.constants.constants import ALL_ROLES_ID
        user_field_permission_details = FieldRole.objects.filter(
            Q(field_id__in=field_ids),
            (Q(role__in=roles) | Q(role=ALL_ROLES_ID))
        ).values('field_id', 'permission_type')
        user_field_permission_dtos = self._convert_user_field_permission_details_to_dtos(
            user_field_permission_details=user_field_permission_details)
        return user_field_permission_dtos

    def get_fields_of_gofs_in_dtos(
            self, gof_ids: List[str]) -> List[FieldDTO]:
        field_objs = Field.objects.filter(gof_id__in=gof_ids)
        field_dtos = self._convert_field_objs_to_dtos(field_objs=field_objs)
        return field_dtos

    def get_gof_ids_with_read_permission_for_user(
            self, roles: List[str]) -> List[str]:
        from django.db.models import Q
        from ib_tasks.constants.enum import PermissionTypes
        from ib_tasks.constants.constants import ALL_ROLES_ID
        gof_ids_queryset = GoFRole.objects.filter(
            Q(permission_type=PermissionTypes.READ.value),
            (Q(role__in=roles) | Q(role=ALL_ROLES_ID))
        ).values_list('gof_id', flat=True)

        gof_ids_list = list(gof_ids_queryset)
        return gof_ids_list

    def delete_field_roles(self, field_ids: List[str]):
        FieldRole.objects.filter(field_id__in=field_ids).delete()

    def create_stages_with_given_information(self,
                                             stage_information: StageDTO):
        pass

    def validate_stage_ids(self, stage_ids) -> Optional[List[str]]:
        pass

    def update_stages_with_given_information(self,
                                             update_stages_information: StageDTO):
        pass

    def validate_stages_related_task_template_ids(self,
                                                  task_stages_dto: TaskStagesDTO) -> \
            Optional[List[TaskStagesDTO]]:
        pass

    @staticmethod
    def _get_global_constant_names(
            global_constants_dtos: List[GlobalConstantsDTO]):
        global_constants_names = [
            global_constants_dto.constant_name
            for global_constants_dto in global_constants_dtos
        ]
        return global_constants_names

    @staticmethod
    def _make_global_constants_dict(
            global_constants_dtos: List[GlobalConstantsDTO]):
        global_constants_dict = {}
        for global_constants_dto in global_constants_dtos:
            global_constants_dict[global_constants_dto.constant_name] = \
                global_constants_dto
        return global_constants_dict

    @staticmethod
    def _get_gof_ids(gof_dtos: List[GoFWithOrderAndAddAnotherDTO]):
        gof_ids = [gof_dto.gof_id for gof_dto in gof_dtos]
        return gof_ids

    @staticmethod
    def _make_gofs_dict(gof_dtos: List[GoFWithOrderAndAddAnotherDTO]):
        gofs_dict = {}
        for gof_dto in gof_dtos:
            gofs_dict[gof_dto.gof_id] = gof_dto
        return gofs_dict

    def get_task_details(self, task_dtos: List[GetTaskDetailsDTO]) -> \
            GetTaskStageCompleteDetailsDTO:
        task_ids = [task.task_id for task in task_dtos]
        task_objs = Task.objects.filter(id__in=task_ids).values('id',
                                                                'template_id')

        task_template_and_stage_ids = self._get_task_tempalate_and_stage_ids(
            task_dtos, task_objs)
        q = None
        for counter, item in enumerate(task_template_and_stage_ids):
            current_queue = Q(task_template_id=item['template_id'],
                              stage_id=item['stage_id'])
            if counter == 0:
                q = current_queue
            else:
                q = q | current_queue

        stage_objs = Stage.objects.filter(q).values('field_display_config',
                                                    'stage_id')

        stage_actions = self._get_stage_action_objs(
            task_template_and_stage_ids)
        stage_fields_dtos = self._get_fields_details(stage_objs)
        stage_actions_dtos = self._convert_stage_actions_to_dtos(stage_actions)

        return GetTaskStageCompleteDetailsDTO(
            fields_dto=stage_fields_dtos,
            actions_dto=stage_actions_dtos
        )

    def get_task_ids_for_the_stage_ids(
            self, stage_ids: List[str],
            offset: int, limit: int) -> Tuple[List[TaskStageIdsDTO], int]:
        task_stage_ids = TaskStage.objects.filter(
            stage__stage_id__in=stage_ids
        ).values('task_id', 'stage__stage_id')
        total_count = len(task_stage_ids)
        task_stage_dtos = [
            TaskStageIdsDTO(
                task_id=task_stage_id['task_id'],
                stage_id=task_stage_id['stage__stage_id']
            )
            for task_stage_id in task_stage_ids[offset: offset + limit]
        ]
        return task_stage_dtos, total_count

    @staticmethod
    def _get_task_tempalate_and_stage_ids(task_dtos, task_objs):
        task_template_and_stage_ids = []
        for task in task_objs:
            for task_dto in task_dtos:
                if task['id'] == task_dto.task_id:
                    task_template_and_stage_ids.append(
                        {
                            "template_id": task['template_id'],
                            "stage_id": task_dto.stage_id
                        }
                    )
        return task_template_and_stage_ids

    @staticmethod
    def _get_stage_action_objs(task_template_and_stage_ids):
        q = None
        for counter, item in enumerate(task_template_and_stage_ids):
            current_queue = Q(stage__task_template_id=item['template_id'],
                              stage__stage_id=item['stage_id'])
            if counter == 0:
                q = current_queue
            else:
                q = q | current_queue
        stage_actions = StageAction.objects.filter(q).values(
            'id', 'stage__stage_id', 'name', 'button_text', 'button_color')

        return stage_actions

    def _get_fields_details(self, stage_objs):
        fields_ids = [stage['field_display_config'] for stage in stage_objs]
        field_objs = Field.objects.filter(field_id__in=fields_ids).values(
            'field_id', 'field_type')
        field_response_objs = TaskGoFField.objects.filter(
            field_id__in=fields_ids).values('field_id', 'field_response')
        field_values = {}
        for item in field_response_objs:
            field_values[item['field_id']] = item['field_response']
        fields_dtos = []
        for stage in stage_objs:
            for field in field_objs:
                if field['field_id'] in stage['field_display_config']:
                    field_id = field['field_id']
                    fields_dtos.append(
                        self.get_field_dto(field, field_id, field_values,
                                           stage)
                    )
        return fields_dtos

    @staticmethod
    def get_field_dto(field, field_id, field_values, stage):
        return FieldDetailsDTO(
            field_id=field_id,
            field_type=field['field_type'],
            key=field['display_name'],
            value=field_values[field_id]
        )

    @staticmethod
    def _convert_stage_actions_to_dtos(stage_actions):
        stage_actions_dtos = []
        for stage in stage_actions:
            stage_actions_dtos.append(
                ActionDTO(
                    action_id=stage['id'],
                    name=stage['name'],
                    stage_id=stage['stage__stage_id'],
                    button_color=stage['button_color'],
                    button_text=stage['button_text']
                )
            )
        return stage_actions_dtos

    def get_valid_task_ids(self, task_ids: List[str]) -> Optional[List[str]]:
        valid_task_ids = Task.objects.filter(id__in=task_ids)
        return valid_task_ids

    @staticmethod
    def _convert_task_templates_objs_to_dtos(
            task_template_objs: List[TaskTemplate]) -> List[TaskTemplateDTO]:
        task_template_dtos = [
            TaskTemplateDTO(
                template_id=task_template_obj.template_id,
                template_name=task_template_obj.name
            )
            for task_template_obj in task_template_objs
        ]
        return task_template_dtos

    @staticmethod
    def _convert_stage_actions_details_to_dto(
            stage_actions_details: List[Dict]) -> List[ActionsOfTemplateDTO]:
        actions_of_template_dtos = [
            ActionsOfTemplateDTO(
                action_id=stage_action['id'],
                template_id=stage_action['stage__task_template_id'],
                button_color=stage_action['button_color'],
                button_text=stage_action['button_text']
            )
            for stage_action in stage_actions_details
        ]
        return actions_of_template_dtos

    @staticmethod
    def _convert_task_template_gofs_to_dtos(
            task_template_gofs) -> List[GoFToTaskTemplateDTO]:
        task_template_gof_dtos = [
            GoFToTaskTemplateDTO(
                template_id=task_template_gof.task_template_id,
                gof_id=task_template_gof.gof_id,
                order=task_template_gof.order,
                enable_add_another=task_template_gof.enable_add_another_gof

            )
            for task_template_gof in task_template_gofs
        ]
        return task_template_gof_dtos

    @staticmethod
    def _convert_gof_details_to_dtos(gof_details: List[Dict]) -> List[GoFDTO]:
        gof_dtos = [
            GoFDTO(gof_id=gof['gof_id'],
                   gof_display_name=gof['display_name'],
                   max_columns=gof['max_columns']) for gof in gof_details
        ]
        return gof_dtos

    @staticmethod
    def _convert_field_objs_to_dtos(
            field_objs: List[Field]) -> List[FieldDTO]:
        field_dtos = [
            FieldDTO(
                gof_id=field_obj.gof_id,
                field_id=field_obj.field_id,
                field_display_name=field_obj.display_name,
                field_type=field_obj.field_type,
                field_values=field_obj.field_values,
                required=field_obj.required,
                help_text=field_obj.help_text,
                tooltip=field_obj.tooltip,
                placeholder_text=field_obj.placeholder_text,
                error_message=field_obj.error_messages,
                allowed_formats=field_obj.allowed_formats,
                validation_regex=field_obj.validation_regex
            )
            for field_obj in field_objs
        ]
        return field_dtos

    @staticmethod
    def _convert_user_field_permission_details_to_dtos(
            user_field_permission_details: List[Dict]
    ) -> List[UserFieldPermissionDTO]:
        user_field_permission_dtos = [
            UserFieldPermissionDTO(
                field_id=user_field_permission['field_id'],
                permission_type=user_field_permission['permission_type']
            )
            for user_field_permission in user_field_permission_details
        ]
        return user_field_permission_dtos

    def get_user_task_and_max_stage_value_dto_based_on_given_stage_ids(
            self, user_id: str, stage_ids: List[str], limit: int,
            offset: int) -> List[TaskIdWithStageValueDTO]:
        from django.db.models import Max
        task_objs_with_max_stage_value = list(
            TaskStage.objects.filter(
                task__created_by=user_id,
                stage__stage_id__in=stage_ids).values("task_id").annotate(
                stage_value=Max("stage__value"))[offset:limit])
        task_id_with_max_stage_value_dtos = []
        for task_with_stage_value_item in task_objs_with_max_stage_value:
            task_id_with_max_stage_value_dtos.append(
                TaskIdWithStageValueDTO(
                    task_id=task_with_stage_value_item['task_id'],
                    stage_value=task_with_stage_value_item['stage_value']))
        return task_id_with_max_stage_value_dtos

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


    def get_task_ids_for_the_stage_ids(
            self, stage_ids: List[str],
            offset: int, limit: int) -> Tuple[List[TaskStageIdsDTO], int]:
        pass

    def get_field_ids_for_given_task_template_ids(self,
                                                  task_template_ids: List[str]) -> List[TemplateFieldsDTO]:
        task_field_objs = TaskTemplateGoFs.objects.filter(
            task_template_id__in=task_template_ids).values('task_template_id', 'gof__field')
        task_fields_dtos = self._convert_task_template_fields_to_dtos(task_field_objs)
        return task_fields_dtos

    @staticmethod
    def _convert_task_template_fields_to_dtos(task_field_objs):
        task_fields_dict = defaultdict(list)
        for task in task_field_objs:
            task_fields_dict[task['task_template_id']].append(task['gof__field'])

        task_fields_dtos = []
        for template_id, field_ids in task_fields_dict.items():
            task_fields_dtos.append(
                TemplateFieldsDTO(
                    task_template_id=template_id,
                    field_ids=field_ids
                )
            )
        return task_fields_dtos

    def check_is_task_exists(self, task_id: int) -> bool:
        pass

    def create_task_log(self, create_task_log_dto: CreateTaskLogDTO):
        pass
