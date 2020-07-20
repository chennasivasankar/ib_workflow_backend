"""
Created on: 15/07/20
Author: Pavankumar Pamuru

"""

import abc
from typing import List

from ib_tasks.interactors.storage_interfaces.dtos import (
    GoFDTO, GoFRoleDTO
)
from ib_tasks.interactors.dtos import FieldDTO, GlobalConstantsDTO


class TaskStorageInterface(abc.ABC):

    @abc.abstractmethod
    def create_task_template(self, template_id: str, template_name: str):
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
    def get_existing_gof_ids_in_given_gof_ids(
            self, gof_ids: List[str]
    ) -> List[str]:
        pass

    @abc.abstractmethod
    def create_gofs(self, gof_dtos: List[GoFDTO]):
        pass

    @abc.abstractmethod
    def create_gof_roles(self, gof_role_dtos: List[GoFRoleDTO]):
        pass

    @abc.abstractmethod
    def update_gofs(self, gof_dtos: List[GoFDTO]):
        pass

    @abc.abstractmethod
    def delete_gof_roles(self, gof_ids: List[str]):
        pass

    @abc.abstractmethod
    def check_is_template_exists(self, template_id: str) -> bool:
        pass

    @abc.abstractmethod
    def get_constant_names_of_existing_global_constants_of_template(
            self, template_id: str):
        pass

    @abc.abstractmethod
    def create_global_constants_to_template(
            self, template_id: str,
            global_constants_dtos: List[GlobalConstantsDTO]):
        pass

    @abc.abstractmethod
    def get_gof_dtos_for_given_gof_ids(
            self, gof_ids: List[str]
    ) -> List[GoFDTO]:
        pass
