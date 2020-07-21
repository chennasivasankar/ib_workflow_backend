from typing import List, Optional

from ib_tasks.interactors.dtos import CreateTaskTemplateDTO, \
    GlobalConstantsDTO
from ib_tasks.interactors.storage_interfaces.dtos import (
    GoFDTO, GoFRoleDTO, FieldDTO, FieldRoleDTO
)
from ib_tasks.interactors.storage_interfaces.task_storage_interface import \
    TaskStorageInterface
from ib_tasks.models.field import Field
from ib_tasks.models.field_role import FieldRole


class TasksStorageImplementation(TaskStorageInterface):

    def create_task_template(self, template_id: str, template_name: str):
        pass

    def update_task_template(
            self, create_task_template_dto: CreateTaskTemplateDTO):
        pass

    def get_task_template_name_if_exists(self, template_id: str) -> str:
        pass

    def get_task_template_ids(self) -> List[str]:
        pass

    def create_fields(self, field_dtos: List[FieldDTO]):
        from ib_tasks.models.field import Field
        fields = self._get_fields(field_dtos)
        Field.objects.bulk_create(fields)

    def get_existing_gof_ids_in_given_gof_ids(
            self, gof_ids: List[str]
    ) -> List[str]:
        from ib_tasks.models.gof import GoF
        existing_gof_ids = list(
            GoF.objects.filter(pk__in=gof_ids).values_list('gof_id', flat=True)
        )
        return existing_gof_ids

    def get_valid_template_ids_in_given_template_ids(
            self, template_ids: List[str]
    ) -> List[str]:
        from ib_tasks.models.task_template import TaskTemplate
        valid_template_ids = list(
            TaskTemplate.objects.filter(pk__in=template_ids). \
                values_list("template_id", flat=True)
        )
        return valid_template_ids

    def create_gofs(self, gof_dtos: List[GoFDTO]):
        from ib_tasks.models.gof import GoF
        gofs = [
            GoF(
                gof_id=gof_dto.gof_id,
                display_name=gof_dto.gof_display_name,
                task_template_id=gof_dto.task_template_id,
                order=gof_dto.order,
                max_columns=gof_dto.max_columns,
                enable_multiple_gofs=gof_dto.enable_multiple_gofs
            )
            for gof_dto in gof_dtos
        ]
        GoF.objects.bulk_create(gofs)

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
            gof.task_template_id = gof_dto.task_template_id
            gof.order = gof_dto.order
            gof.max_columns = gof_dto.max_columns
            gof.enable_multiple_gofs = gof_dto.enable_multiple_gofs
        GoF.objects.bulk_update(
            gofs, ['display_name', 'task_template_id', 'order', 'max_columns']
        )

    @staticmethod
    def _get_matching_gof_dto(
            gof_id: str, gof_dtos: List[GoFDTO]
    ) -> Optional[GoFDTO]:
        for gof_dto in gof_dtos:
            gof_id_matched = gof_id == gof_dto.gof_id
            if gof_id_matched:
                return gof_dto
        return

    def update_gof_roles(self, gof_role_dtos: List[GoFRoleDTO]):
        pass

    def check_is_template_exists(self, template_id: str) -> bool:
        pass

    def get_constant_names_of_existing_global_constants_of_template(
            self, template_id: str):
        pass

    def create_global_constants_to_template(
            self, template_id: str,
            global_constants_dtos: List[GlobalConstantsDTO]):
        pass

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

    def update_fields_roles(self, field_role_dtos: List[FieldRoleDTO]):
        list_of_fields = ["permission_type"]
        field_ids = [
            field_role_dto.field_id
            for field_role_dto in field_role_dtos
        ]

        field_role_objs = list(FieldRole.objects.filter(field_id__in=field_ids))
        for field_role_obj in field_role_objs:
            field_role_dto = self._get_matching_field_role_dto(
                field_role_obj, field_role_dtos
            )
            field_role_obj.permission_type = field_role_dto.permission_type

        FieldRole.objects.bulk_update(field_role_objs, list_of_fields)

    def create_fields_roles(self, field_role_dtos: List[FieldRoleDTO]):
        fields_roles = self._get_fields_roles(field_role_dtos)
        FieldRole.objects.bulk_create(fields_roles)

    def get_existing_field_ids(self, field_ids: List[str]) -> List[str]:
        from ib_tasks.models.field import Field
        existing_field_ids = list(
            Field.objects.filter(field_id__in=field_ids).values_list("field_id", flat=True)
        )
        return existing_field_ids

    def get_existing_gof_ids(self, gof_ids: List[str]) -> List[str]:
        from ib_tasks.models.gof import GoF
        existing_gof_ids = list(
            GoF.objects.filter(gof_id__in=gof_ids).values_list("gof_id", flat=True)
        )
        return existing_gof_ids

    def get_fields_role_dtos(self, field_ids: List[str]) -> List[str]:
        field_role_objs = FieldRole.objects.filter(field_id__in=field_ids)
        field_role_dtos = [
            FieldRoleDTO(
                field_id=field_role_obj.field_id,
                role=field_role_obj.role,
                permission_type=field_role_obj.permission_type
            )
            for field_role_obj in field_role_objs
        ]
        return field_role_dtos

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
    def _get_matching_field_role_dto(
            field_role_obj: FieldRole, field_role_dtos: List[FieldRoleDTO]
    ):
        old_field_id = field_role_obj.field_id
        old_role = field_role_obj.role
        for field_role_dto in field_role_dtos:
            new_field_id = field_role_dto.field_id
            new_role = field_role_dto.role
            if old_field_id == new_field_id and old_role == new_role:
                return field_role_dto

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
