import abc
from dataclasses import dataclass
from typing import List

from ib_tasks.exceptions.adapter_exceptions import InvalidProjectIdsException
from ib_tasks.exceptions.task_custom_exceptions import InvalidTaskTemplateDBId
from ib_tasks.interactors.stages_dtos import StageMinimalDTO
from ib_tasks.interactors.storage_interfaces.stage_dtos import StageFlowDTO


@dataclass()
class StageFlowCompleteDetailsDTO:
    stage_dtos: List[StageMinimalDTO]
    stage_flow_dtos: List[StageFlowDTO]


class GetTemplateStageFlowPresenterInterface(abc.ABC):

    @abc.abstractmethod
    def raise_invalid_task_template_id(self, err: InvalidTaskTemplateDBId):
        pass

    @abc.abstractmethod
    def get_response_for_invalid_project_id(
            self, err: InvalidProjectIdsException):
        pass

    @abc.abstractmethod
    def get_response_for_user_not_in_project(self):
        pass

    @abc.abstractmethod
    def get_response_for_template_stage_flow(
            self, stage_flow_complete_details_dto: StageFlowCompleteDetailsDTO
    ):
        pass