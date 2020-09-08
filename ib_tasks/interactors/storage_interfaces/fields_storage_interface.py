import abc
from dataclasses import dataclass
from typing import List

from ib_tasks.constants.enum import ViewType, FieldTypes
from ib_tasks.interactors.storage_interfaces.fields_dtos import FieldDTO, \
    FieldCompleteDetailsDTO, UserFieldPermissionDTO, FieldIdWithGoFIdDTO, \
    FieldIdWithFieldDisplayNameDTO, \
    TaskTemplateStageFieldsDTO, StageTaskFieldsDTO, FieldDetailsDTOWithTaskId, \
    FieldNameDTO, FieldDisplayNameDTO
from ib_tasks.interactors.storage_interfaces.get_task_dtos import \
    TemplateFieldsDTO
from ib_tasks.interactors.storage_interfaces.stage_dtos import \
    TaskTemplateStageDTO, StageDetailsDTO
from ib_tasks.interactors.storage_interfaces.task_dtos import \
    TaskProjectRolesDTO


@dataclass
class FieldTypeDTO:
    field_id: str
    field_type: FieldTypes


class FieldsStorageInterface(abc.ABC):

    @abc.abstractmethod
    def get_fields_details(self, template_stage_dtos: List[StageTaskFieldsDTO]) -> \
            List[FieldDetailsDTOWithTaskId]:
        pass

    @abc.abstractmethod
    def get_field_ids(self, task_dto: List[TaskTemplateStageDTO],
                      view_type: ViewType) -> \
            List[TaskTemplateStageFieldsDTO]:
        pass

    @abc.abstractmethod
    def get_task_stages(self, task_id: int) -> List[str]:
        pass

    @abc.abstractmethod
    def get_stage_complete_details(self, stage_ids: List[str]) -> \
            List[StageDetailsDTO]:
        pass

    @abc.abstractmethod
    def get_fields_of_gofs_in_dtos(
            self, gof_ids: List[str]) -> List[FieldDTO]:
        pass

    @abc.abstractmethod
    def get_user_permitted_gof_field_dtos(
            self, user_roles: List[str], gof_ids: List[str]
    ) -> List[FieldNameDTO]:
        pass

    @abc.abstractmethod
    def get_field_details_for_given_field_ids(
            self, field_ids: List[str]
    ) -> List[FieldCompleteDetailsDTO]:
        pass

    @abc.abstractmethod
    def get_field_ids_for_given_task_template_ids(self,
                                                  task_template_ids: List[
                                                      str]) -> \
            List[TemplateFieldsDTO]:
        pass

    @abc.abstractmethod
    def get_field_ids_related_to_given_gof_ids(
            self, gof_ids: List[str]
    ) -> List[FieldIdWithGoFIdDTO]:
        pass

    @abc.abstractmethod
    def get_user_field_permission_dtos(
            self, roles: List[str],
            field_ids: List[str]) -> List[UserFieldPermissionDTO]:
        pass

    @abc.abstractmethod
    def get_field_ids_having_read_permission_for_user(
            self, user_roles: List[str], field_ids: List[str]) -> List[str]:
        pass

    @abc.abstractmethod
    def get_field_ids_having_write_permission_for_user(
            self, user_roles: List[str], field_ids: List[str]) -> List[str]:
        pass

    @abc.abstractmethod
    def get_field_ids_permissions_for_user_in_projects(
            self, task_project_roles: List[TaskProjectRolesDTO],
            field_ids: List[str]) -> List[str]:
        pass

    @abc.abstractmethod
    def check_is_user_has_read_permission_for_field(
            self, field_id: str, user_roles: List[str]) -> bool:
        pass

    @abc.abstractmethod
    def check_is_user_has_write_permission_for_field(
            self, field_id: str, user_roles: List[str]) -> bool:
        pass

    @abc.abstractmethod
    def get_field_type_dtos(self, field_ids: List[str]) -> List[FieldTypeDTO]:
        pass

    @abc.abstractmethod
    def get_field_ids_for_given_gofs(self, gof_ids: List[str]) -> List[str]:
        pass

    @abc.abstractmethod
    def get_field_dtos(self, field_ids: List[str]) -> List[FieldDTO]:
        pass

    @abc.abstractmethod
    def get_virtual_stage_ids_in_given_stage_ids(self, db_stage_ids):
        pass

    @abc.abstractmethod
    def get_gof_ids_for_given_field_ids(
            self, field_ids: List[str]) -> List[FieldIdWithGoFIdDTO]:
        pass

    @abc.abstractmethod
    def get_user_write_permitted_field_ids_for_given_gof_ids(
            self, user_roles, gof_ids: List[str]
    ) -> List[FieldIdWithFieldDisplayNameDTO]:
        pass

    @abc.abstractmethod
    def validate_user_roles_with_field_ids_roles(
            self, user_roles: List[str], field_ids: List[str]):
        pass

    @abc.abstractmethod
    def get_field_display_names(self, field_ids: List[str]) -> List[FieldDisplayNameDTO]:
        pass
