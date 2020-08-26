from typing import List
from ib_tasks.interactors.storage_interfaces.field_config_storage_interface \
    import \
    FieldConfigStorageInterface
from ib_tasks.interactors.storage_interfaces.fields_dtos import FieldDTO, \
    FieldRoleDTO
from ib_tasks.models import FieldRole, Field


class FieldConfigStorageImplementation(FieldConfigStorageInterface):
    def create_fields(self, field_dtos: List[FieldDTO]):
        from ib_tasks.models.field import Field
        fields = self._get_fields(field_dtos)
        Field.objects.bulk_create(fields)

    def update_fields(self, field_dtos: List[FieldDTO]):
        list_of_fields = [
            'display_name', 'gof_id',
            'required', 'field_type',
            'field_values', 'allowed_formats',
            'help_text', 'tooltip',
            'placeholder_text', 'error_messages',
            'validation_regex', 'order'
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

    def delete_field_roles(self, field_ids: List[str]):
        FieldRole.objects.filter(field_id__in=field_ids).delete()

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
                gof_id=field_dto.gof_id,
                order=field_dto.order
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
