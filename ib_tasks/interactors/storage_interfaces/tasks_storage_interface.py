"""
Created on: 15/07/20
Author: Pavankumar Pamuru

"""

import abc
from typing import List

from ib_tasks.interactors.dtos import CreateTaskTemplateDTO, FieldDTO
from ib_tasks.interactors.storage_interfaces.dtos import (
    GoFDTO, GoFRoleDTO, GoFFieldDTO
)


class TaskStorageInterface(abc.ABC):

    @abc.abstractmethod
    def create_task_template(
            self, create_task_template_dto: CreateTaskTemplateDTO):
        pass

    @abc.abstractmethod
    def update_task_template(
            self, create_task_template_dto: CreateTaskTemplateDTO):
        pass

    @abc.abstractmethod
    def get_task_template_name_if_exists(self, template_id: str) -> str:
        pass

    @abc.abstractmethod
    def get_task_template_ids(self) -> List[str]:
        pass

    @abc.abstractmethod
    def create_fields(self, field_dtos: List[FieldDTO]):
        pass

    @abc.abstractmethod
    def get_existing_gof_of_template(self, template_id: str) -> List[str]:
        pass

    @abc.abstractmethod
    def get_existing_gof_ids_in_given_gof_ids(
            self, gof_ids: List[str]
    ) -> List[str]:
        pass

    @abc.abstractmethod
    def get_valid_field_ids_in_given_field_ids(
            self, field_ids: List[str]
    ) -> List[str]:
        pass

    @abc.abstractmethod
    def create_gofs(self, gof_dtos: List[GoFDTO]):
        pass

    @abc.abstractmethod
    def create_gof_roles(self, gof_role_dtos: List[GoFRoleDTO]):
        pass

    @abc.abstractmethod
    def create_gof_fields(self, gof_field_dtos: List[GoFFieldDTO]):
        pass
