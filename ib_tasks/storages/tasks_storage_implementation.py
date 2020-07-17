from typing import List

from ib_tasks.interactors.dtos import CreateTaskTemplateDTO, FieldDTO, \
    GlobalConstantsDTO
from ib_tasks.interactors.storage_interfaces.dtos import (
    GoFDTO, GoFRoleDTO, GoFFieldDTO
)
from ib_tasks.interactors.storage_interfaces.task_storage_interface import \
    TaskStorageInterface


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
        pass

    def get_existing_gof_ids_in_given_gof_ids(
            self, gof_ids: List[str]
    ) -> List[str]:
        from ib_tasks.models.gof import GoF
        existing_gof_ids = list(
            GoF.objects.filter(pk__in=gof_ids).values_list('gof_id', flat=True)
        )
        return existing_gof_ids

    def get_valid_field_ids_in_given_field_ids(
            self, field_ids: List[str]
    ) -> List[str]:
        from ib_tasks.models.field import Field
        valid_field_ids = list(
            Field.objects.filter(pk__in=field_ids)\
                         .values_list('field_id', flat=True)
        )
        return valid_field_ids

    def create_gofs(self, gof_dtos: List[GoFDTO]):
        from ib_tasks.models.gof import GoF
        gofs = [
            GoF(
                gof_id=gof_dto.gof_id,
                display_name=gof_dto.gof_display_name,
                task_template_id=gof_dto.task_template_id,
                order=gof_dto.order,
                max_columns=gof_dto.max_columns
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

    def create_gof_fields(self, gof_field_dtos: List[GoFFieldDTO]):
        from ib_tasks.models.field import Field
        field_ids = [
            gof_field_dto.field_id for gof_field_dto in gof_field_dtos
        ]
        fields = Field.objects.filter(field_id__in=field_ids)
        for field in fields:
            for gof_field_dto in gof_field_dtos:
                if field.field_id == gof_field_dto.field_id:
                    field.gof_id = gof_field_dto.gof_id
        Field.objects.bulk_update(fields, ['gof_id'])

    def check_is_template_exists(self, template_id: str) -> bool:
        pass

    def get_constant_names_of_existing_global_constants_of_template(
            self, template_id: str):
        pass

    def create_global_constants_to_template(
            self, template_id: str,
            global_constants_dtos: List[GlobalConstantsDTO]):
        pass
