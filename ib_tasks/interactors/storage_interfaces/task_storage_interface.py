"""
Created on: 15/07/20
Author: Pavankumar Pamuru

"""

import abc
from typing import List, Optional

from ib_tasks.interactors.storage_interfaces.actions_dtos import \
    ActionWithStageIdDTO
from ib_tasks.interactors.storage_interfaces.get_task_dtos import \
    TemplateFieldsDTO
from ib_tasks.interactors.storage_interfaces.stage_dtos import \
    TaskIdWithStageValueDTO, StageIdWithTemplateIdDTO, TaskStageIdsDTO, \
    TaskStagesDTO, StageDTO
from ib_tasks.interactors.storage_interfaces.status_dtos import \
    TaskTemplateStatusDTO
from ib_tasks.interactors.storage_interfaces.task_dtos import TaskDisplayIdDTO
from ib_tasks.interactors.task_dtos import CreateTaskLogDTO, GetTaskDetailsDTO


class TaskStorageInterface(abc.ABC):

    @abc.abstractmethod
    def get_existing_field_ids(self, field_ids: List[str]) -> List[str]:
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
                                             update_stages_information:
                                             StageDTO):
        pass

    @abc.abstractmethod
    def validate_stages_related_task_template_ids(self,
                                                  task_stages_dto:
                                                  TaskStagesDTO) -> \
            Optional[List[TaskStagesDTO]]:
        pass

    @abc.abstractmethod
    def create_status_for_tasks(self,
                                create_status_for_tasks: List[
                                    TaskTemplateStatusDTO]):
        pass

    @abc.abstractmethod
    def get_valid_task_ids(self, task_ids: List[int]) -> Optional[List[int]]:
        pass

    @abc.abstractmethod
    def get_task_ids_for_the_stage_ids(
            self, stage_ids: List[str], task_ids: List[int]) -> List[
        TaskStageIdsDTO]:
        pass

    @abc.abstractmethod
    def get_field_ids_for_given_task_template_ids(self,
                                                  task_template_ids: List[
                                                      str]) -> \
            List[TemplateFieldsDTO]:
        pass

    @abc.abstractmethod
    def get_user_task_and_max_stage_value_dto_based_on_given_stage_ids(
            self, user_id: str, stage_ids: List[str], limit: int, offset: int
    ) -> List[TaskIdWithStageValueDTO]:
        pass

    @abc.abstractmethod
    def validate_task_related_stage_ids(self,
                                        task_dtos: List[GetTaskDetailsDTO]) \
            -> \
                    List[GetTaskDetailsDTO]:
        pass

    @abc.abstractmethod
    def get_initial_stage_ids_of_templates(self) -> List[int]:
        pass

    @abc.abstractmethod
    def get_initial_stage_id_with_template_id_dtos(
            self) -> List[StageIdWithTemplateIdDTO]:
        pass

    @abc.abstractmethod
    def get_actions_for_given_stage_ids_in_dtos(
            self, stage_ids: List[int]) -> List[ActionWithStageIdDTO]:
        pass

    @abc.abstractmethod
    def check_is_task_exists(self, task_id: int) -> bool:
        pass

    @abc.abstractmethod
    def create_task_log(self, create_task_log_dto: CreateTaskLogDTO):
        pass

    @abc.abstractmethod
    def get_user_task_ids_and_max_stage_value_dto_based_on_given_stage_ids(
            self, stage_ids: List[str], task_ids: List[int]
    ) -> List[TaskIdWithStageValueDTO]:
        pass

    @abc.abstractmethod
    def create_elastic_task(self, task_id: int, elastic_task_id: str):
        pass

    @abc.abstractmethod
    def check_is_valid_task_display_id(self, task_display_id: str) -> bool:
        pass

    @abc.abstractmethod
    def get_task_id_for_task_display_id(self, task_display_id: str) -> int:
        pass

    @abc.abstractmethod
    def get_task_display_ids_dtos(self, task_ids: List[int]) -> List[
        TaskDisplayIdDTO]:
        pass

    @abc.abstractmethod
    def get_project_id_of_task(self, task_id: int) -> str:
        pass

    @abc.abstractmethod
    def get_project_id_for_the_task_id(self, task_id) -> str:
        pass

    @abc.abstractmethod
    def get_user_team_id(self, user_id: str, task_id: int) -> str:
        pass
