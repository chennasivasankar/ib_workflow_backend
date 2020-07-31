"""
Created on: 15/07/20
Author: Pavankumar Pamuru

"""

import abc
from typing import List, Optional, Tuple

from ib_tasks.interactors.storage_interfaces.status_dtos import \
    TaskTemplateStatusDTO
from ib_tasks.interactors.storage_interfaces.fields_dtos import FieldDTO, \
    FieldRoleDTO, FieldTypeDTO, UserFieldPermissionDTO
from ib_tasks.interactors.storage_interfaces.gof_dtos import GoFDTO, \
    GoFRoleDTO, GoFToTaskTemplateDTO
from ib_tasks.interactors.storage_interfaces.stage_dtos import TaskStagesDTO, \
    StageDTO, TaskStageIdsDTO
from ib_tasks.interactors.storage_interfaces.gof_dtos import GoFDTO, GoFRoleDTO
from ib_tasks.interactors.storage_interfaces.stage_dtos import TaskStagesDTO, \
    StageDTO, GetTaskStageCompleteDetailsDTO
from ib_tasks.interactors.global_constants_dtos import GlobalConstantsDTO
from ib_tasks.interactors.gofs_dtos import GoFWithOrderAndAddAnotherDTO
from ib_tasks.interactors.storage_interfaces.task_templates_dtos import \
    TaskTemplateDTO
from ib_tasks.interactors.storage_interfaces.actions_dtos import \
    ActionsOfTemplateDTO
from ib_tasks.interactors.task_dtos import GetTaskDetailsDTO


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
    def create_fields_roles(self, field_role_dtos: List[FieldRoleDTO]):
        pass

    @abc.abstractmethod
    def get_existing_field_ids(self, field_ids: List[str]) -> List[str]:
        pass

    @abc.abstractmethod
    def get_existing_gof_ids(self, gof_ids: List[str]) -> List[str]:
        pass

    @abc.abstractmethod
    def create_stages_with_given_information(self,
                                             stage_information: StageDTO):
        pass

    @abc.abstractmethod
    def validate_stage_ids(self, stage_ids) -> Optional[List[str]]:
        pass

    @abc.abstractmethod
    def update_stages_with_given_information(self,
                                             update_stages_information: StageDTO):
        pass

    @abc.abstractmethod
    def validate_stages_related_task_template_ids(self,
                                                  task_stages_dto: TaskStagesDTO) -> \
            Optional[List[TaskStagesDTO]]:
        pass

    @abc.abstractmethod
    def create_status_for_tasks(self,
                                create_status_for_tasks: List[
                                    TaskTemplateStatusDTO]):
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
    def get_task_templates_dtos(self) -> List[TaskTemplateDTO]:
        pass

    @abc.abstractmethod
    def get_actions_of_templates_dtos(self) -> List[ActionsOfTemplateDTO]:
        pass

    @abc.abstractmethod
    def get_gofs_details_dtos(
            self, gof_ids: List[str]) -> List[GoFDTO]:
        pass

    @abc.abstractmethod
    def get_gofs_to_task_templates_from_permitted_gofs(
            self, gof_ids: List[str]) -> List[GoFToTaskTemplateDTO]:
        pass

    @abc.abstractmethod
    def get_user_field_permission_dtos(
            self, roles: List[str],
            field_ids: List[str]) -> List[UserFieldPermissionDTO]:
        pass

    @abc.abstractmethod
    def get_fields_of_gofs_in_dtos(
            self, gof_ids: List[str]) -> List[FieldDTO]:
        pass

    @abc.abstractmethod
    def get_gof_ids_with_read_permission_for_user(self, roles: List[str]) -> \
    List[str]:
        pass

    @abc.abstractmethod
    def delete_field_roles(self, field_ids: List[str]):
        pass

    @abc.abstractmethod
    def get_existing_gof_ids_of_template(
            self, template_id: str) -> List[str]:
        pass

    @abc.abstractmethod
    def get_valid_gof_ids_in_given_gof_ids(
            self, gof_ids: List[str]) -> List[str]:
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
    def update_task_template(
            self, template_id: str, template_name: str):
        pass

    @abc.abstractmethod
    def get_field_types_for_given_field_ids(
            self, field_ids: List[str]
    ) -> List[FieldTypeDTO]:
        pass

    @abc.abstractmethod
    def get_valid_task_ids(self, task_ids: List[str]) -> Optional[List[str]]:
        pass

    @abc.abstractmethod
    def get_task_ids_for_the_stage_ids(
            self, stage_ids: List[str],
            offset: int, limit: int) -> Tuple[List[TaskStageIdsDTO], int]:
        pass