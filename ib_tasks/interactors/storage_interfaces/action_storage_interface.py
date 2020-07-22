"""
Created on: 15/07/20
Author: Pavankumar Pamuru

"""
from abc import ABC
from abc import abstractmethod
from typing import List
from ib_tasks.interactors.storage_interfaces.dtos import StageActionNamesDTO
from ib_tasks.interactors.dtos import StagesActionDTO


class ActionStorageInterface(ABC):

    @abstractmethod
    def get_stage_action_names(
            self, stage_ids: List[str]) -> List[StageActionNamesDTO]:
        pass

    @abstractmethod
    def create_stage_actions(self, stage_actions: List[StagesActionDTO]):
        pass

    @abstractmethod
    def update_stage_actions(self, stage_actions: List[StagesActionDTO]):
        pass

    @abstractmethod
    def delete_stage_actions(self, stage_actions: List[StageActionNamesDTO]):
        pass
