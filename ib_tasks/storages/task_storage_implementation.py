from typing import List

from ib_tasks.interactors.storage_interfaces.dtos import (
    FieldDTO, FieldRolesDTO, GoFDTO, GoFRolesDTO, GoFFieldsDTO
)
from ib_tasks.interactors.dtos import GoFIdAndOrderDTO, GlobalConstantsDTO

from ib_tasks.interactors.storage_interfaces.task_storage_interface \
    import TaskStorageInterface

from ib_tasks.models.field import Field


class TaskStorageImplementation(TaskStorageInterface):

    def create_task_template(self, template_id: str, template_name: str):
        pass

    def add_gofs_to_task_template(
            self, template_id: str,
            gof_id_and_order_dtos: List[GoFIdAndOrderDTO]):
        pass

    def get_existing_gof_ids_of_template(self, template_id: str) -> List[str]:
        pass

    def create_gofs(self, gof_dtos: List[GoFDTO]):
        pass

    def create_gof_roles(self, gof_roles_dtos: List[GoFRolesDTO]):
        pass

    def create_gof_fields(self, gof_fields_dtos: List[GoFFieldsDTO]):
        pass

    def check_is_template_exists(self, template_id: str) -> bool:
        pass

    def get_task_template_ids(self) -> List[str]:
        pass

    def get_constant_names_of_existing_global_constants_of_template(
            self, template_id: str):
        pass

    def create_global_constants_to_template(
            self, template_id: str,
            global_constants_dtos: List[GlobalConstantsDTO]):
        pass

    def create_fields(self, field_dtos: List[FieldDTO]):
        from ib_tasks.models.field import Field
        fields = self._get_fields(field_dtos)
        Field.objects.bulk_create(fields)

    def update_fields(self, field_dtos: List[FieldDTO]):
        from ib_tasks.models.field import Field
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
                tooltip=field_dto.tool_tip,
                placeholder_text=field_dto.placeholder_text,
                error_messages=field_dto.error_message,
                validation_regex=field_dto.validation_regex,
                gof_id=field_dto.gof_id
            )
            for field_dto in field_dtos
        ]
        return fields

    def update_fields_roles(self, field_roles_dto: List[FieldRolesDTO]):
        pass

    def create_fields_roles(self, field_roles_dto: List[FieldRolesDTO]):
        pass

    def get_existing_field_ids(self, field_ids: List[str]) -> List[str]:
        from ib_tasks.models.field import Field
        existing_field_ids = list(
            Field.objects.filter(field_id__in=field_ids).values_list("field_id", flat=True)
        )
        return existing_field_ids
