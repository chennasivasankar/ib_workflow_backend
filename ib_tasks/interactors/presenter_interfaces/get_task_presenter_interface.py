import abc
from dataclasses import dataclass
from typing import List

from ib_tasks.exceptions.task_custom_exceptions import InvalidTaskIdException, \
    InvalidStageIdsForTask, InvalidTaskDisplayId
from ib_tasks.interactors.stages_dtos import StageAssigneeDetailsDTO
from ib_tasks.interactors.storage_interfaces.get_task_dtos \
    import TaskDetailsDTO
from ib_tasks.interactors.task_dtos import StageAndActionsDetailsDTO


@dataclass
class TaskCompleteDetailsDTO:
    task_id: str
    task_details_dto: TaskDetailsDTO
    stages_and_actions_details_dtos: List[StageAndActionsDetailsDTO]
    stage_assignee_details_dtos: List[StageAssigneeDetailsDTO]


class GetTaskPresenterInterface(abc.ABC):

    @abc.abstractmethod
    def raise_exception_for_invalid_task_id(self, err: InvalidTaskIdException):
        pass

    @abc.abstractmethod
    def get_task_response(self,
                          task_complete_details_dto: TaskCompleteDetailsDTO):
        pass

    @abc.abstractmethod
    def raise_invalid_stage_ids_for_task(self, err: InvalidStageIdsForTask):
        pass

    @abc.abstractmethod
    def raise_invalid_task_display_id(self, err: InvalidTaskDisplayId):
        pass
