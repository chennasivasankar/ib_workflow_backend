"""
Created on: 15/07/20
Author: Pavankumar Pamuru

"""

import abc
from typing import List

from ib_tasks.interactors.dtos import CreateTaskTemplateDTO
from ib_tasks.interactors.storage_interfaces.dtos import (
    GoFDTO, GoFRolesDTO, GoFFieldsDTO, FieldDTO, FieldRolesDTO
)
from ib_tasks.interactors.dtos import GoFIdAndOrderDTO


class TaskStorageInterface(abc.ABC):

    @abc.abstractmethod
    def create_task_template(self, template_id: str, template_name: str):
        pass

    @abc.abstractmethod
    def add_gofs_to_task_template(
            self, template_id: str,
            gof_id_and_order_dtos: List[GoFIdAndOrderDTO]):
        pass

    @abc.abstractmethod
    def get_task_template_ids(self) -> List[str]:
        pass

    @abc.abstractmethod
    def create_fields(self, field_dtos: List[FieldDTO]):
        pass

    @abc.abstractmethod
    def get_existing_gof_ids_of_template(self, template_id: str) -> List[str]:
        pass

    @abc.abstractmethod
    def create_gofs(self, gof_dtos: List[GoFDTO]):
        pass

    @abc.abstractmethod
    def create_gof_roles(self, gof_roles_dtos: List[GoFRolesDTO]):
        pass

    @abc.abstractmethod
    def create_gof_fields(self, gof_fields_dtos: List[GoFFieldsDTO]):
        pass

    @abc.abstractmethod
    def check_is_template_exists(self, template_id: str) -> bool:
        pass

    @abc.abstractmethod
    def update_fields(self, field_dtos: List[FieldDTO]):
        pass

    @abc.abstractmethod
    def update_fields_roles(self, field_roles_dto: List[FieldRolesDTO]):
        pass
    @abc.abstractmethod
    def create_fields_roles(self, field_roles_dto: List[FieldRolesDTO]):
        pass

    @abc.abstractmethod
    def get_existing_field_ids(self, field_ids: List[str]) -> List[str]:
        pass
