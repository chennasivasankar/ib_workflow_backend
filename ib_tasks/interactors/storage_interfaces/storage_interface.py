import abc
from typing import List, Optional

from ib_tasks.interactors.global_constants_dtos import GlobalConstantsDTO
from ib_tasks.interactors.storage_interfaces.actions_dtos \
    import ActionRolesDTO, ActionDTO
from ib_tasks.interactors.storage_interfaces.fields_dtos import FieldValueDTO, \
    FieldWritePermissionRolesDTO
from ib_tasks.interactors.storage_interfaces.gof_dtos \
    import GroupOfFieldsDTO, GOFMultipleEnableDTO, GoFWritePermissionRolesDTO
from ib_tasks.interactors.storage_interfaces.stage_dtos import StageActionNamesDTO, StageValueDTO, StageDisplayValueDTO
from ib_tasks.interactors.stages_dtos import StageActionDTO
from ib_tasks.interactors.storage_interfaces.status_dtos import StatusVariableDTO
from ib_tasks.interactors.storage_interfaces.task_dtos import TaskDueMissingDTO


class StorageInterface(abc.ABC):

    @abc.abstractmethod
    def get_stage_action_names(
            self, stage_ids: List[str]) -> List[StageActionNamesDTO]:
        pass

    @abc.abstractmethod
    def get_valid_stage_ids(self, stage_ids: List[str]) -> Optional[List[str]]:
        pass

    @abc.abstractmethod
    def create_stage_actions(self, stage_actions: List[StageActionDTO]):
        pass

    @abc.abstractmethod
    def update_stage_actions(self, stage_actions: List[StageActionDTO]):
        pass

    @abc.abstractmethod
    def delete_stage_actions(self, stage_actions: List[StageActionNamesDTO]):
        pass

    @abc.abstractmethod
    def create_initial_stage_to_task_template(self, task_template_stage_dtos):
        pass

    @abc.abstractmethod
    def get_valid_task_template_ids(self, task_template_ids: List[str]):
        pass

    @abc.abstractmethod
    def validate_task_id(self, task_id: int) -> bool:
        pass

    @abc.abstractmethod
    def get_task_group_of_fields_dto(
            self, task_id: int) -> List[GroupOfFieldsDTO]:
        pass

    @abc.abstractmethod
    def get_fields_to_group_of_field_ids(
            self, group_of_field_ids: List[str]) -> List[FieldValueDTO]:
        pass

    @abc.abstractmethod
    def get_status_variables_to_task(
            self, task_id: int) -> List[StatusVariableDTO]:
        pass

    @abc.abstractmethod
    def get_enable_multiple_gofs_field_to_gof_ids(
            self, template_id: str, gof_ids: List[str]) -> List[GOFMultipleEnableDTO]:
        pass

    @abc.abstractmethod
    def get_path_name_to_action(self, action_id: int) -> str:
        pass

    @abc.abstractmethod
    def update_status_variables_to_task(self, task_id: int,
                                        status_variables_dto):
        pass

    @abc.abstractmethod
    def get_action_roles_to_stages(
            self, stage_ids: List[str]) -> List[ActionRolesDTO]:
        pass

    @abc.abstractmethod
    def get_actions_dto(self, action_ids: List[int]) -> List[ActionDTO]:
        pass

    @abc.abstractmethod
    def get_action_roles(self, action_id: int) -> List[str]:
        pass

    @abc.abstractmethod
    def validate_action(self, action_id: int) -> bool:
        pass

    @abc.abstractmethod
    def get_global_constants_to_task(
            self, task_id: int) -> List[GlobalConstantsDTO]:
        pass

    @abc.abstractmethod
    def get_stage_dtos_to_task(self, task_id: int) -> List[StageValueDTO]:
        pass

    @abc.abstractmethod
    def get_task_template_stage_logic_to_task(
            self, task_id: int) -> List[StageDisplayValueDTO]:
        pass

    @abc.abstractmethod
    def update_task_stages(self, task_id: int, stage_ids: List[str]):
        pass

    @abc.abstractmethod
    def get_write_permission_roles_for_given_gof_ids(
            self, gof_ids: List[str]) -> List[GoFWritePermissionRolesDTO]:
        pass

    @abc.abstractmethod
    def get_write_permission_roles_for_given_field_ids(
            self, field_ids: List[str]) -> List[FieldWritePermissionRolesDTO]:
        pass

    @abc.abstractmethod
    def get_task_present_stage_actions(self, task_id: int) -> List[int]:
        pass

    @abc.abstractmethod
    def validate_if_task_is_assigned_to_user(self,
                                             task_id: int, user_id: str) -> bool:
        pass

    @abc.abstractmethod
    def get_task_due_missing_reasons_details(self, task_id: int) -> \
            List[TaskDueMissingDTO]:
        pass
