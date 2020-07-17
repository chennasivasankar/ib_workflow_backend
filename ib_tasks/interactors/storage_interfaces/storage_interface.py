import abc
from typing import List, Optional
from ib_tasks.interactors.dtos import (
    StageActionDTO, TaskTemplateStageActionDTO
)
from ib_tasks.interactors.storage_interfaces.dtos import *


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
    def create_task_template_stage_actions(
            self, tasks_dto: List[TaskTemplateStageActionDTO]):
        pass

    @abc.abstractmethod
    def update_task_template_stage_actions(
            self, tasks_dto: List[TaskTemplateStageActionDTO]):
        pass

    @abc.abstractmethod
    def validate_task_id(self, task_id: str) -> bool:
        pass

    @abc.abstractmethod
    def get_task_group_of_fields_dto(
            self, task_id: str) -> List[GroupOfFieldsDTO]:
        pass

    @abc.abstractmethod
    def get_fields_to_group_of_field_ids(
            self, group_of_field_ids: List[str]) -> List[FieldValueDTO]:
        pass

    @abc.abstractmethod
    def get_status_variables_to_task(
            self, task_id: str) -> List[StatusVariableDTO]:
        pass
