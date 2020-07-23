import abc

from ib_tasks.interactors.dtos import StageActionDTO, TaskTemplateStageDTO
from ib_tasks.interactors.storage_interfaces.dtos import *


class StorageInterface(abc.ABC):

    @abc.abstractmethod
    def get_stage_action_names(
            self, stage_ids: List[str]) -> List[StageActionNamesDTO]:
        pass

    @abc.abstractmethod
    def get_valid_stage_ids(self,
                            stage_ids: List[str]) -> Optional[List[str]]:
        pass

    @abc.abstractmethod
    def create_stage_actions(self, stage_actions: List[StageActionDTO]):
        pass

    @abc.abstractmethod
    def update_stage_actions(self, stage_actions: List[StageActionDTO]):
        pass

    @abc.abstractmethod
    def delete_stage_actions(self,
                             stage_actions: List[StageActionNamesDTO]):
        pass

    @abc.abstractmethod
    def create_initial_stage_to_task_template(
            self, task_template_stage_dtos: List[TaskTemplateStageDTO]):
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
            self, gof_ids: List[str]) -> List[GOFMultipleEnableDTO]:
        pass

    @abc.abstractmethod
    def get_path_name_to_action(self, action_id: str) -> str:
        pass

    @abc.abstractmethod
    def update_status_variables_to_task(self, task_id: str,
                                        status_variables_dto):
        pass

    @abc.abstractmethod
    def get_action_roles_to_stages(
            self, stage_ids: List[str]) -> List[ActionRolesDTO]:
        pass

    @abc.abstractmethod
    def get_actions_dto(self, action_ids: List[str]) -> List[ActionDTO]:
        pass

    @abc.abstractmethod
    def get_action_roles(self, action_id: str) -> List[str]:
        pass

    @abc.abstractmethod
    def validate_action(self, action_id: str) -> bool:
        pass
