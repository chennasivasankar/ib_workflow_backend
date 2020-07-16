from typing import List

from ib_tasks.interactors.dtos import CreateTaskTemplateDTO, FieldDTO
from ib_tasks.interactors.storage_interfaces.dtos import (
    GoFDTO, GoFFieldsDTO, GoFRoleDTO
)
from ib_tasks.interactors.storage_interfaces.tasks_storage_interface import \
    TaskStorageInterface


class TasksStorageImplementation(TaskStorageInterface):

    def create_task_template(
            self, create_task_template_dto: CreateTaskTemplateDTO):
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

    def get_existing_gof_of_template(self, template_id: str) -> List[str]:
        pass

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

    def create_gof_fields(self, gof_fields_dtos: List[GoFFieldsDTO]):
        from ib_tasks.models.field import Field
        fields =
