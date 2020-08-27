import abc
from dataclasses import dataclass
from typing import List

from ib_tasks.adapters.auth_service import InvalidProjectIdsException, \
    TeamsNotExistForGivenProjectException, UsersNotExistsForGivenTeamsException
from ib_tasks.exceptions.task_custom_exceptions import \
    InvalidTaskIdException, \
    InvalidStageIdsForTask, InvalidTaskDisplayId
from ib_tasks.interactors.stages_dtos import StageAssigneeWithTeamDetailsDTO
from ib_tasks.interactors.storage_interfaces.get_task_dtos \
    import TaskDetailsDTO
from ib_tasks.interactors.task_dtos import StageAndActionsDetailsDTO


@dataclass
class TaskCompleteDetailsDTO:
    task_details_dto: TaskDetailsDTO
    stages_and_actions_details_dtos: List[StageAndActionsDetailsDTO]
    stage_assignee_with_team_details_dtos: List[
        StageAssigneeWithTeamDetailsDTO]


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

    @abc.abstractmethod
    def raise_user_permission_denied(self):
        pass

    @abc.abstractmethod
    def raise_invalid_searchable_records_found(self):
        pass

    @abc.abstractmethod
    def raise_invalid_project_id(self, err: InvalidProjectIdsException):
        pass

    @abc.abstractmethod
    def raise_teams_does_not_exists_for_project(
            self, err: TeamsNotExistForGivenProjectException
    ):
        pass

    @abc.abstractmethod
    def raise_users_not_exist_for_given_teams(
            self, err: UsersNotExistsForGivenTeamsException
    ):
        pass