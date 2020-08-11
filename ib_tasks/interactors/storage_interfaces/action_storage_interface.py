"""
Created on: 15/07/20
Author: Pavankumar Pamuru

"""
import abc
from abc import ABC
from typing import List, Optional

from ib_tasks.constants.enum import ActionTypes
from ib_tasks.exceptions.action_custom_exceptions import InvalidActionException
from ib_tasks.exceptions.stage_custom_exceptions import InvalidStageId, \
    TransitionTemplateIsNotRelatedToGivenStageAction
from ib_tasks.interactors.stages_dtos import StageActionDTO
from ib_tasks.interactors.storage_interfaces.actions_dtos import \
    StageActionDetailsDTO
from ib_tasks.interactors.storage_interfaces.stage_dtos import \
    StageActionNamesDTO


class ActionStorageInterface(ABC):

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
                            stage_ids: List[str],
                            user_roles: List[str]) -> \
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
    def get_stage_ids_having_actions(self, db_stage_ids: List[int]) -> List[
        int]:
        pass
