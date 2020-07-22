"""
Created on: 15/07/20
Author: Pavankumar Pamuru

"""

import abc
from typing import List, Optional

from ib_tasks.interactors.storage_interfaces.dtos import (
    GoFRoleDTO, GoFDTO, FieldDTO, FieldRoleDTO, TaskStatusDTO, TaskStagesDTO,
    StageDTO, TaskTemplateDTO, ActionsOfTemplateDTO, UserFieldPermissionDTO,
    GoFToTaskTemplateDTO
)
from ib_tasks.interactors.dtos import GlobalConstantsDTO, \
    GoFWithOrderAndAddAnotherDTO


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
    def get_task_template_name(self, template_id: str):
        pass

    @abc.abstractmethod
    def create_global_constants_to_template(
            self, template_id: str,
            global_constants_dtos: List[GlobalConstantsDTO]):
        pass

    @abc.abstractmethod
    def update_fields(self, field_dtos: List[FieldDTO]):
        pass

    @abc.abstractmethod
    def update_fields_roles(self, field_roles_dto: List[FieldRoleDTO]):
        pass

    @abc.abstractmethod
    def create_fields_roles(self, field_roles_dto: List[FieldRoleDTO]):
        pass

    @abc.abstractmethod
    def get_existing_field_ids(self, field_ids: List[str]) -> List[str]:
        pass

    @abc.abstractmethod
    def get_existing_gof_ids(self, gof_ids: List[str]) -> List[str]:
        pass

    @abc.abstractmethod
    def update_task_template(self, template_id: str, template_name: str):
        pass

    @abc.abstractmethod
    def get_existing_gof_ids_of_template(
            self, template_id: str) -> List[str]:
        pass

    @abc.abstractmethod
    def add_gofs_to_template(
            self, template_id: str,
            gof_dtos: List[GoFWithOrderAndAddAnotherDTO]):
        pass

    @abc.abstractmethod
    def update_gofs_to_template(
            self, template_id: str,
            gof_dtos: List[GoFWithOrderAndAddAnotherDTO]):
        pass

    @abc.abstractmethod
    def get_valid_gof_ids_in_given_gof_ids(
            self, gof_ids: List[str]) -> List[str]:
        pass

    @abc.abstractmethod
    def create_status_for_tasks(self,
                                create_status_for_tasks: List[TaskStatusDTO]):
        pass

    @abc.abstractmethod
    def update_global_constants_to_template(
            self, template_id: str,
            global_constants_dtos: List[GlobalConstantsDTO]):
        pass

    @abc.abstractmethod
    def get_gof_dtos_for_given_gof_ids(
            self, gof_ids: List[str]
    ) -> List[GoFDTO]:
        pass

    @abc.abstractmethod
    def get_valid_template_ids_in_given_template_ids(
            self, template_ids: List[str]
    ) -> List[str]:
        pass

    @abc.abstractmethod
    def get_task_template_dtos(self) -> List[TaskTemplateDTO]:
        pass

    @abc.abstractmethod
    def get_user_actions_of_template_dtos(
            self, roles: List[str]) -> List[ActionsOfTemplateDTO]:
        pass

    @abc.abstractmethod
    def get_gofs_of_task_templates_dtos(self) -> List[GoFDTO]:
        pass

    @abc.abstractmethod
    def get_gofs_to_task_templates_dtos(self) -> List[GoFToTaskTemplateDTO]:
        pass

    @abc.abstractmethod
    def get_user_field_permission_dtos(
            self, roles: List[str]) -> List[UserFieldPermissionDTO]:
        pass

    @abc.abstractmethod
    def get_field_dtos(self) -> List[FieldDTO]:
        pass

