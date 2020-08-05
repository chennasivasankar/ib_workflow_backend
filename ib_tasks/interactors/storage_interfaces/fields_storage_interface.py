import abc
from typing import List, Optional

from ib_tasks.interactors.storage_interfaces.actions_dtos import \
    ActionDetailsDTO
from ib_tasks.interactors.storage_interfaces.fields_dtos import \
    FieldDTO, \
    FieldCompleteDetailsDTO, UserFieldPermissionDTO
from ib_tasks.interactors.storage_interfaces.fields_dtos import \
    FieldIdWithGoFIdDTO
from ib_tasks.interactors.storage_interfaces.fields_dtos import \
    TaskTemplateStageFieldsDTO, StageTaskFieldsDTO, FieldDetailsDTOWithTaskId
from ib_tasks.interactors.storage_interfaces.get_task_dtos import \
    TemplateFieldsDTO
from ib_tasks.interactors.storage_interfaces.stage_dtos import \
    TaskTemplateStageDTO, StageDetailsDTO
from ib_tasks.interactors.task_dtos import GetTaskDetailsDTO


class FieldsStorageInterface(abc.ABC):

    @abc.abstractmethod
    def get_stage_details(self, task_dtos: List[GetTaskDetailsDTO]) -> \
            List[TaskTemplateStageDTO]:
        pass

    @abc.abstractmethod
    def get_actions_details(self,
                            stage_ids: List[str],
                            user_roles: List[str]) -> \
            List[ActionDetailsDTO]:
        pass

    @abc.abstractmethod
    def get_fields_details(self, template_stage_dtos: List[StageTaskFieldsDTO],
                           user_roles: List[str]) -> \
            List[FieldDetailsDTOWithTaskId]:
        pass

    @abc.abstractmethod
    def get_valid_task_ids(self, task_ids: List[int]) -> Optional[List[int]]:
        pass

    @abc.abstractmethod
    def get_field_ids(self, task_dto: List[TaskTemplateStageDTO]) -> \
            List[TaskTemplateStageFieldsDTO]:
        pass

    @abc.abstractmethod
    def validate_task_related_stage_ids(self,
                                        task_dtos: List[GetTaskDetailsDTO]) \
            -> \
            List[GetTaskDetailsDTO]:
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
