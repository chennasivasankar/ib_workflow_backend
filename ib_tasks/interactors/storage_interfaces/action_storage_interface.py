"""
Created on: 15/07/20
Author: Pavankumar Pamuru

"""
import abc
from typing import List, Optional

from ib_tasks.adapters.dtos import ProjectRolesDTO
from ib_tasks.constants.enum import ActionTypes
from ib_tasks.exceptions.action_custom_exceptions import InvalidActionException
from ib_tasks.exceptions.stage_custom_exceptions import InvalidStageId, \
    TransitionTemplateIsNotRelatedToGivenStageAction
from ib_tasks.interactors.stages_dtos import StageActionDTO
from ib_tasks.interactors.storage_interfaces.actions_dtos import \
    StageActionDetailsDTO
from ib_tasks.interactors.storage_interfaces.stage_dtos import \
    StageActionNamesDTO, StageActionIdDTO, StageIdActionNameDTO
from ib_tasks.interactors.storage_interfaces.task_dtos import TaskProjectRolesDTO


class ActionStorageInterface(abc.ABC):

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
    def get_actions_details(self,
                            action_ids: List[int]) -> \
            List[StageActionDetailsDTO]:
        pass

    @abc.abstractmethod
    def get_action_type_for_given_action_id(self,
                                            action_id: int) -> ActionTypes:
        pass

    @abc.abstractmethod
    def validate_action_id(self, action_id) -> Optional[
        InvalidActionException]:
        pass

    @abc.abstractmethod
    def validate_stage_id(self, stage_id) -> Optional[InvalidStageId]:
        pass

    @abc.abstractmethod
    def validate_transition_template_id_is_related_to_given_stage_action(
            self, transition_checklist_template_id, action_id, stage_id
    ) -> Optional[TransitionTemplateIsNotRelatedToGivenStageAction]:
        pass

    @abc.abstractmethod
    def validate_action(self, action_id: int) -> bool:
        pass

    @abc.abstractmethod
    def get_permitted_action_ids_given_stage_ids(self, user_roles: List[str],
                                                 stage_ids: List[str]) -> List[int]:
        pass

    @abc.abstractmethod
    def get_stage_ids_having_actions(self, db_stage_ids: List[int]) \
            -> List[int]:
        pass

    @abc.abstractmethod
    def get_permitted_action_ids_for_given_task_stages(
            self,
            user_project_roles: List[TaskProjectRolesDTO],
            stage_ids):
        pass

    @abc.abstractmethod
    def get_stage_id_for_given_action_id(self, action_id: int) -> int:
        pass

    @abc.abstractmethod
    def get_user_permitted_action_ids_given_stage_ids(
            self, user_roles: List[str],
            stage_ids: List[int]
    ) -> List[int]:
        pass

    @abc.abstractmethod
    def get_action_ids_given_stage_ids(
            self, stage_ids: List[int]) -> List[int]:
        pass
    @abc.abstractmethod
    def get_stage_action_name_dtos(
            self, stage_id_action_dtos: List[StageIdActionNameDTO]
    ) -> List[StageActionIdDTO]:
        pass