"""
Created on: 15/07/20
Author: Pavankumar Pamuru

"""

import abc
from typing import List, Optional, Tuple

from ib_tasks.interactors.storage_interfaces.actions_dtos import \
    ActionsOfTemplateDTO
from ib_tasks.interactors.storage_interfaces.get_task_dtos import \
    TemplateFieldsDTO
from ib_tasks.interactors.storage_interfaces.stage_dtos import \
    StageValueWithTaskIdsDTO, TaskIdWithStageDetailsDTO, \
    TaskIdWithStageValueDTO
from ib_tasks.interactors.storage_interfaces.stage_dtos import TaskStageIdsDTO
from ib_tasks.interactors.storage_interfaces.stage_dtos import TaskStagesDTO, \
    StageDTO
from ib_tasks.interactors.storage_interfaces.status_dtos import \
    TaskTemplateStatusDTO


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
    def get_actions_for_given_stage_ids(
            self, stage_ids: List[int]) -> List[ActionsOfTemplateDTO]:
        pass

    @abc.abstractmethod
    def get_valid_task_ids(self, task_ids: List[str]) -> Optional[List[str]]:
        pass

    @abc.abstractmethod
    def get_task_ids_for_the_stage_ids(
            self, stage_ids: List[str],
            offset: int, limit: int) -> Tuple[List[TaskStageIdsDTO], int]:
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
    def get_task_id_with_stage_details_dtos_based_on_stage_value(
            self, user_id: str, stage_values: List[int],
            task_ids_group_by_stage_value_dtos: List[
                StageValueWithTaskIdsDTO]) \
            -> [TaskIdWithStageDetailsDTO]:
        pass

    @abc.abstractmethod
    def get_initial_stage_ids_of_templates(self) -> List[int]:
        pass
