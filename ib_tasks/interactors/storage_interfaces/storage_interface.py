import abc
from datetime import datetime
from typing import List, Optional
from ib_tasks.interactors.global_constants_dtos import GlobalConstantsDTO
from ib_tasks.interactors.storage_interfaces.actions_dtos \
    import ActionRolesDTO, ActionDTO
from ib_tasks.interactors.storage_interfaces.fields_dtos import FieldWritePermissionRolesDTO
from ib_tasks.interactors.storage_interfaces.gof_dtos \
    import GOFMultipleEnableDTO, GoFWritePermissionRolesDTO
from ib_tasks.interactors.storage_interfaces.stage_dtos import StageValueDTO, StageDisplayValueDTO
from ib_tasks.interactors.storage_interfaces.status_dtos import StatusVariableDTO
from ib_tasks.interactors.storage_interfaces.task_dtos import TaskDueMissingDTO
from ib_tasks.interactors.task_dtos import TaskDelayParametersDTO


class StorageInterface(abc.ABC):

    @abc.abstractmethod
    def validate_task_id(self, task_id: int) -> bool:
        pass

    @abc.abstractmethod
    def get_task_project_id(self, task_id: int) -> str:
        pass
    @abc.abstractmethod
    def get_status_variables_to_task(
            self, task_id: int) -> List[StatusVariableDTO]:
        pass

    @abc.abstractmethod
    def get_enable_multiple_gofs_field_to_gof_ids(
            self, template_id: str) -> List[GOFMultipleEnableDTO]:
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
    def get_write_permission_roles_for_given_field_ids(
            self, field_ids: List[str]) -> List[FieldWritePermissionRolesDTO]:
        pass

    @abc.abstractmethod
    def get_task_present_stage_actions(self, task_id: int) -> List[int]:
        pass

    @abc.abstractmethod
    def validate_if_task_is_assigned_to_user_in_given_stage(self,
                                                            task_id: int, user_id: str,
                                                            stage_id: int) -> bool:
        pass

    @abc.abstractmethod
    def get_task_due_details(self, task_id: int, stage_id: int) -> \
            List[TaskDueMissingDTO]:
        pass

    @abc.abstractmethod
    def add_due_delay_details(self, due_details: TaskDelayParametersDTO):
        pass

    @abc.abstractmethod
    def validate_stage_id(self, stage_id: int) -> bool:
        pass

    @abc.abstractmethod
    def get_due_missed_count(self, task_id: int, user_id: str,
                             stage_id: str) -> int:
        pass

    @abc.abstractmethod
    def get_latest_rp_id_if_exists(self, task_id: int,
                                   stage_id: int) -> Optional[str]:
        pass

    @abc.abstractmethod
    def get_rp_ids(self, task_id: int, stage_id: int) -> \
            List[str]:
        pass

    @abc.abstractmethod
    def add_superior_to_db(
            self, task_id: int, stage_id: int, superior_id: str):
        pass

    @abc.abstractmethod
    def get_latest_rp_added_datetime(self,
                                     task_id: int, stage_id: int) -> Optional[str]:
        pass

    @abc.abstractmethod
    def update_task_due_datetime(self, due_details: TaskDelayParametersDTO):
        pass
