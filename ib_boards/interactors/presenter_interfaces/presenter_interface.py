import abc
from dataclasses import dataclass
from typing import List

from django.http import response

from ib_boards.exceptions.custom_exceptions import InvalidBoardIds
from ib_boards.interactors.dtos import TaskDTO, ActionDTO
from ib_boards.interactors.storage_interfaces.dtos import BoardDTO


@dataclass
class TaskCompleteDetailsDTO:
    total_tasks: int
    task_dtos: List[TaskDTO]
    action_dtos: List[ActionDTO]


class GetBoardsPresenterInterface(abc.ABC):

    @abc.abstractmethod
    def get_response_for_user_have_no_access_for_boards(
            self) -> response.HttpResponse:
        pass

    @abc.abstractmethod
    def get_response_for_invalid_offset(self) -> response.HttpResponse:
        pass

    @abc.abstractmethod
    def get_response_for_invalid_limit(self) -> response.HttpResponse:
        pass

    @abc.abstractmethod
    def get_response_for_get_boards(
            self, board_dtos: List[BoardDTO], total_boards: int) -> response.HttpResponse:
        pass

    @abc.abstractmethod
    def get_response_for_offset_exceeds_total_tasks(self):
        pass


class GetBoardsDetailsPresenterInterface(abc.ABC):

    @abc.abstractmethod
    def get_response_for_invalid_board_ids(
            self, error: InvalidBoardIds) -> response.HttpResponse:
        pass

    @abc.abstractmethod
    def get_response_for_board_details(
            self, board_dtos: List[BoardDTO]) -> response.HttpResponse:
        pass


class GetColumnTasksPresenterInterface(abc.ABC):

    @abc.abstractmethod
    def get_response_for_the_invalid_column_id(self):
        pass

    @abc.abstractmethod
    def get_response_column_tasks(
            self, task_complete_details_dto: TaskCompleteDetailsDTO):
        pass

    @abc.abstractmethod
    def get_response_for_invalid_offset(self):
        pass

    @abc.abstractmethod
    def get_response_for_invalid_limit(self):
        pass

    @abc.abstractmethod
    def get_response_for_offset_exceeds_total_tasks(self):
        pass

    @abc.abstractmethod
    def get_response_for_user_have_no_access_for_boards(self):
        pass


class StageDisplayLogicPresenterInterface(abc.ABC):

    @abc.abstractmethod
    def get_response_for_invalid_stage_ids(self, error):
        pass

    @abc.abstractmethod
    def get_response_for_stage_display_logic(self, task_status_dtos):
        pass