from typing import List

import json

from ib_tasks.interactors.storage_interfaces.dtos import (
    FieldDTO, FieldRolesDTO, GoFDTO, GoFRolesDTO, GoFFieldsDTO
)
from ib_tasks.interactors.dtos import GoFIdAndOrderDTO

from ib_tasks.interactors.storage_interfaces.task_storage_interface \
    import TaskStorageInterface


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

    def create_fields(self, field_dtos: List[FieldDTO]):
        pass

    def update_fields(self, field_dtos: List[FieldDTO]):
        pass

    def update_fields_roles(self, field_roles_dto: List[FieldRolesDTO]):
        pass

    def create_fields_roles(self, field_roles_dto: List[FieldRolesDTO]):
        pass

    def get_existing_field_ids(self, field_ids: List[str]) -> List[str]:
        pass
