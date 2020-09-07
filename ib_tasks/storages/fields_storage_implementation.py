from collections import defaultdict
from typing import List, Dict

from django.db.models import F, Q

from ib_tasks.constants.constants import ALL_ROLES_ID
from ib_tasks.constants.enum import PermissionTypes, ViewType
from ib_tasks.interactors.storage_interfaces.fields_dtos import \
    FieldCompleteDetailsDTO, FieldDTO, UserFieldPermissionDTO, \
    FieldIdWithGoFIdDTO, StageTaskFieldsDTO, \
    TaskTemplateStageFieldsDTO, FieldDetailsDTOWithTaskId, FieldNameDTO, \
    FieldIdWithFieldDisplayNameDTO
from ib_tasks.interactors.storage_interfaces.fields_storage_interface import \
    FieldsStorageInterface, FieldTypeDTO
from ib_tasks.interactors.storage_interfaces.get_task_dtos import \
    TemplateFieldsDTO
from ib_tasks.interactors.storage_interfaces.stage_dtos import (
    TaskTemplateStageDTO, StageDetailsDTO)
from ib_tasks.interactors.storage_interfaces.task_dtos import \
    TaskProjectRolesDTO
from ib_tasks.models import CurrentTaskStage, Stage, TaskGoFField, FieldRole, \
    TaskTemplateGoFs, Field


class FieldsStorageImplementation(FieldsStorageInterface):

    def get_user_write_permitted_field_ids_for_given_gof_ids(
            self, user_roles, gof_ids: List[str]
    ) -> List[FieldIdWithFieldDisplayNameDTO]:
        field_dicts = FieldRole.objects.filter(
            Q(role__in=user_roles) | Q(role=ALL_ROLES_ID),
            field__gof_id__in=gof_ids,
            permission_type=PermissionTypes.WRITE.value
        ).values(
            "field_id", "field__gof__display_name", "field__display_name")
        field_id_with_display_name_dtos = [
            FieldIdWithFieldDisplayNameDTO(
                field_id=field_dict['field_id'],
                gof_display_name=field_dict['field__gof__display_name'],
                field_display_name=field_dict['field__display_name']
            ) for field_dict in field_dicts
        ]
        return field_id_with_display_name_dtos

    def get_gof_ids_for_given_field_ids(
            self, field_ids: List[str]) -> List[FieldIdWithGoFIdDTO]:
        field_gofs_dicts = Field.objects.filter(field_id__in=field_ids).values(
            "field_id", "gof_id")
        return self._prepare_field_id_with_gof_id_dto(field_gofs_dicts)

    @staticmethod
    def _prepare_field_id_with_gof_id_dto(
            field_gofs_dicts) -> List[FieldIdWithGoFIdDTO]:
        field_id_with_gof_id_dtos = [
            FieldIdWithGoFIdDTO(
                field_id=field_gof_dict['field_id'],
                gof_id=field_gof_dict['gof_id'])
            for field_gof_dict in field_gofs_dicts
        ]
        return field_id_with_gof_id_dtos

    def get_virtual_stage_ids_in_given_stage_ids(self, db_stage_ids):
        virtual_stage_ids = Stage.objects.filter(
            id__in=db_stage_ids, value=-1).values_list('id', flat=True)
        return virtual_stage_ids

    def get_field_ids_related_to_given_gof_ids(self, gof_ids: List[str]) -> \
            List[FieldIdWithGoFIdDTO]:
        field_objects = Field.objects.filter(gof_id__in=gof_ids)
        field_id_with_gof_id_dtos = \
            self._prepare_field_id_with_gof_id_dtos(field_objects)
        return field_id_with_gof_id_dtos

    @staticmethod
    def _prepare_field_id_with_gof_id_dtos(
            field_objects: List[Field]
    ) -> List[FieldIdWithGoFIdDTO]:
        field_id_with_gof_id_dtos = [
            FieldIdWithGoFIdDTO(
                field_id=field_obj.field_id,
                gof_id=field_obj.gof_id
            )
            for field_obj in field_objects
        ]
        return field_id_with_gof_id_dtos

    def get_fields_of_gofs_in_dtos(self, gof_ids: List[str]) -> List[FieldDTO]:
        field_objs = Field.objects.filter(gof_id__in=gof_ids)
        field_dtos = self._convert_field_objs_to_field_dtos(
            field_objs=field_objs)
        return field_dtos

    def get_user_permitted_gof_field_dtos(
            self, user_roles: List[str], gof_ids: List[str]
    ) -> List[FieldNameDTO]:

        field_ids = FieldRole.objects.filter(
            Q(field__gof_id__in=gof_ids),
            (Q(role__in=user_roles) | Q(role=ALL_ROLES_ID))
        ).values_list('field_id', flat=True)

        field_objs = Field.objects.filter(field_id__in=field_ids)

        return [
            FieldNameDTO(
                field_id=field_obj.field_id,
                gof_id=field_obj.gof_id,
                field_display_name=field_obj.display_name
            )
            for field_obj in field_objs
        ]

    def get_field_details_for_given_field_ids(self, field_ids: List[str]) -> \
            List[FieldCompleteDetailsDTO]:
        field_objects = list(
            Field.objects.filter(field_id__in=field_ids)
        )
        field_details_dtos = self._prepare_field_details_dtos(field_objects)
        return field_details_dtos

    def get_field_ids_for_given_task_template_ids(self,
                                                  task_template_ids: List[
                                                      str]) -> \
            List[TemplateFieldsDTO]:
        task_field_objs = TaskTemplateGoFs.objects.filter(
            task_template_id__in=task_template_ids).values('task_template_id',
                                                           'gof__field')
        task_fields_dtos = self._convert_task_template_fields_to_dtos(
            task_field_objs)
        return task_fields_dtos

    def get_fields_details(self,
                           task_fields_dtos: List[StageTaskFieldsDTO]) -> \
            List[FieldDetailsDTOWithTaskId]:
        q = None
        for counter, item in enumerate(task_fields_dtos):
            current_queue = Q(task_gof__task_id=item.task_id,
                              field_id__in=item.field_ids) | Q(
                task_gof__task_id=item.task_id,
                field_id__in=item.field_ids
            )
            if counter == 0:
                q = current_queue
            else:
                q = q | current_queue
        if q is None:
            return []
        field_objs = list(set(TaskGoFField.objects.filter(q).select_related(
            'field', 'task_gof'
        )))

        task_fields_dtos = self._convert_field_objs_to_dtos(field_objs)
        return task_fields_dtos

    @staticmethod
    def _convert_field_objs_to_dtos(field_objs):
        task_fields_dtos = []
        for field in field_objs:
            task_fields_dtos.append(
                FieldDetailsDTOWithTaskId(
                    task_id=field.task_gof.task_id,
                    field_id=field.field_id,
                    value=field.field_response,
                    key=field.field.display_name,
                    field_type=field.field.field_type
                )
            )
        return task_fields_dtos

    def get_field_ids(self, task_dtos: List[TaskTemplateStageDTO],
                      view_type: ViewType) -> \
            List[TaskTemplateStageFieldsDTO]:
        from collections import defaultdict
        task_stages_dict = defaultdict(list)
        for item in task_dtos:
            task_stages_dict[item.stage_id].append(item.task_id)
        q = None
        for counter, item in enumerate(task_dtos):
            current_queue = Q(stage_id=item.stage_id,
                              task_template_id=item.task_template_id)
            if counter == 0:
                q = current_queue
            else:
                q = q | current_queue
        if q is None:
            return []

        if view_type == ViewType.LIST.value:
            stage_objs = (Stage.objects.filter(q)
                          .annotate(view_type=F('card_info_list'))
                          .values('task_template_id', 'stage_id',
                                  'view_type', 'stage_color', 'id',
                                  'display_name'))
        else:
            stage_objs = (Stage.objects.filter(q)
                          .annotate(view_type=F('card_info_kanban'))
                          .values('task_template_id', 'stage_id',
                                  'view_type', 'stage_color', 'id',
                                  'display_name'))

        task_fields_dtos = self._convert_stage_objs_to_dtos(stage_objs,
                                                            task_stages_dict)

        return task_fields_dtos

    @staticmethod
    def _convert_stage_objs_to_dtos(stage_objs, task_stages_dict):
        task_fields_dtos = []
        import json
        for stage in stage_objs:
            fields = stage['view_type']
            if not fields:
                continue
            field_ids = json.loads(fields)
            for task_id in task_stages_dict[stage['stage_id']]:
                task_fields_dtos.append(
                    TaskTemplateStageFieldsDTO(
                        task_template_id=stage['task_template_id'],
                        task_id=task_id,
                        stage_color=stage['stage_color'],
                        stage_id=stage['stage_id'],
                        display_name=stage['display_name'],
                        db_stage_id=stage['id'],
                        field_ids=field_ids))
        return task_fields_dtos

    def get_task_stages(self, task_id: int) -> List[str]:
        stage_ids = CurrentTaskStage.objects.filter(
            task_id=task_id).values_list(
            'stage__stage_id', flat=True)
        return list(stage_ids)

    def get_stage_complete_details(self, stage_ids: List[str]) -> \
            List[StageDetailsDTO]:
        stage_objs = Stage.objects.filter(
            stage_id__in=stage_ids
        ).values(
            'id', 'stage_id', 'display_name',
            'stage_color'
        )
        stage_dtos = []
        for stage in stage_objs:
            stage_dtos.append(
                StageDetailsDTO(
                    stage_id=stage['stage_id'],
                    name=stage['display_name'],
                    db_stage_id=stage['id'],
                    color=stage['stage_color']
                )
            )
        return stage_dtos

    @staticmethod
    def _convert_field_objs_to_field_dtos(
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
                validation_regex=field_obj.validation_regex,
                order=field_obj.order
            )
            for field_obj in field_objs
        ]
        return field_dtos

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

    @staticmethod
    def _convert_task_template_fields_to_dtos(task_field_objs):
        task_fields_dict = defaultdict(list)
        for task in task_field_objs:
            task_fields_dict[task['task_template_id']].append(
                task['gof__field'])

        task_fields_dtos = []
        for template_id, field_ids in task_fields_dict.items():
            task_fields_dtos.append(
                TemplateFieldsDTO(
                    task_template_id=template_id,
                    field_ids=field_ids
                )
            )
        return task_fields_dtos

    def get_user_field_permission_dtos(
            self, roles: List[str],
            field_ids: List[str]) -> List[UserFieldPermissionDTO]:

        user_field_permission_details = FieldRole.objects.filter(
            Q(field_id__in=field_ids),
            (Q(role__in=roles) | Q(role=ALL_ROLES_ID))
        ).values('field_id', 'permission_type')
        user_field_permission_dtos = \
            self._convert_user_field_permission_details_to_dtos(
                user_field_permission_details=user_field_permission_details)
        return user_field_permission_dtos

    def get_field_ids_having_read_permission_for_user(
            self, user_roles: List[str], field_ids: List[str]) -> List[str]:

        field_ids_queryset = FieldRole.objects.filter(
            (
                    Q(permission_type=PermissionTypes.READ.value) |
                    Q(permission_type=PermissionTypes.WRITE.value)
            ),
            (
                    Q(role__in=user_roles) | Q(role=ALL_ROLES_ID)
            ),
            Q(field_id__in=field_ids)
        ).values_list('field_id', flat=True)

        field_ids_list = list(field_ids_queryset)
        return field_ids_list

    def get_field_ids_having_write_permission_for_user(
            self, user_roles: List[str], field_ids: List[str]) -> List[str]:

        field_ids_queryset = FieldRole.objects.filter(
            Q(permission_type=PermissionTypes.WRITE.value),
            (Q(role__in=user_roles) | Q(role=ALL_ROLES_ID)),
            Q(field_id__in=field_ids)
        ).values_list('field_id', flat=True)

        field_ids_list = list(field_ids_queryset)
        return field_ids_list

    def get_field_ids_permissions_for_user_in_projects(
            self, task_project_roles: List[TaskProjectRolesDTO],
            field_ids: List[str]) -> List[str]:
        q = None
        for counter, item in enumerate(task_project_roles):
            current_queue = Q(role__in=item.roles) | Q(role=ALL_ROLES_ID) & \
                            Q(
                                field__taskgoffield__task_gof__task_id=item.task_id)
            if counter == 0:
                q = current_queue
            else:
                q = q | current_queue
        if q is None:
            return []

        field_ids_queryset = (FieldRole.objects.filter(q)
                              .values_list('field_id', flat=True))
        field_ids_list = list(set(field_ids_queryset))
        return field_ids_list

    def check_is_user_has_read_permission_for_field(
            self, field_id: str, user_roles: List[str]) -> bool:

        is_user_has_read_permission = FieldRole.objects.filter(
            (
                    Q(permission_type=PermissionTypes.READ.value) |
                    Q(permission_type=PermissionTypes.WRITE.value)
            ),
            (Q(role__in=user_roles) | Q(role=ALL_ROLES_ID)),
            Q(field_id=field_id)).exists()

        return is_user_has_read_permission

    def check_is_user_has_write_permission_for_field(
            self, field_id: str, user_roles: List[str]) -> bool:

        is_user_has_write_permission = FieldRole.objects.filter(
            Q(permission_type=PermissionTypes.WRITE.value),
            (Q(role__in=user_roles) | Q(role=ALL_ROLES_ID)),
            Q(field_id=field_id)).exists()

        return is_user_has_write_permission

    def get_field_ids_for_given_gofs(self, gof_ids: List[str]) -> List[str]:
        field_ids_queryset = Field.objects.filter(
            gof_id__in=gof_ids).values_list('field_id', flat=True)
        field_ids_list = list(field_ids_queryset)
        return field_ids_list

    def get_field_dtos(self, field_ids: List[str]) -> List[FieldDTO]:
        field_objs = Field.objects.filter(field_id__in=field_ids)
        field_dtos = self._convert_field_objs_to_field_dtos(
            field_objs=field_objs)
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

    def get_field_type_dtos(self, field_ids: List[str]) -> List[FieldTypeDTO]:
        field_types = Field.objects.filter(
            field_id__in=field_ids
        ).values('field_id', 'field_type')

        return [
            FieldTypeDTO(
                field_id=field_type['field_id'],
                field_type=field_type['field_type']
            )
            for field_type in field_types
        ]
