import abc
from typing import List

from ib_tasks.constants.enum import ViewType
from ib_tasks.interactors.storage_interfaces.fields_dtos import FieldDTO, \
    FieldCompleteDetailsDTO, UserFieldPermissionDTO, FieldIdWithGoFIdDTO, \
    TaskTemplateStageFieldsDTO, StageTaskFieldsDTO, FieldDetailsDTOWithTaskId
from ib_tasks.interactors.storage_interfaces.get_task_dtos import \
    TemplateFieldsDTO
from ib_tasks.interactors.storage_interfaces.stage_dtos import \
    TaskTemplateStageDTO, StageDetailsDTO


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
    def check_is_user_has_read_permission_for_field(
            self, field_id: str, user_roles: List[str]) -> bool:
        pass

    @abc.abstractmethod
    def check_is_user_has_write_permission_for_field(
            self, field_id: str, user_roles: List[str]) -> bool:
        pass

    @abc.abstractmethod
    def get_field_ids_for_given_gofs(self, gof_ids: List[str]) -> List[str]:
        pass

    @abc.abstractmethod
    def get_field_dtos(self, field_ids: List[str]) -> List[FieldDTO]:
        pass
