import abc
from dataclasses import dataclass
from typing import List, Optional

from django.http import response

from ib_boards.exceptions.custom_exceptions import InvalidBoardIds
from ib_boards.interactors.dtos import TaskStageIdDTO, ActionDTO, \
    TaskCompleteDetailsDTO, TaskDTO
from ib_boards.interactors.storage_interfaces.dtos import BoardDTO, \
    ColumnCompleteDetails


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
            self, board_dtos: List[BoardDTO],
            total_boards: int) -> response.HttpResponse:
        pass

    @abc.abstractmethod
    def get_response_for_offset_exceeds_total_tasks(self):
        pass


import abc
from typing import List

from ib_boards.interactors.dtos import ColumnTasksDTO
from ib_boards.interactors.storage_interfaces.dtos import (
    TaskFieldsDTO, TaskActionsDTO, ColumnDetailsDTO)


class PresenterInterface(abc.ABC):
    @abc.abstractmethod
    def get_response_for_task_details(self,
                                      task_fields_dto: List[TaskFieldsDTO],
                                      task_actions_dto: List[TaskActionsDTO],
                                      task_ids: List[str]):
        pass

    @abc.abstractmethod
    def response_for_invalid_board_id(self):
        pass

    @abc.abstractmethod
    def response_for_invalid_offset_value(self):
        pass

    @abc.abstractmethod
    def response_for_invalid_limit_value(self):
        pass

    @abc.abstractmethod
    def response_for_user_donot_have_access_for_board(self):
        pass

    @abc.abstractmethod
    def get_response_for_column_details(self,
                                        column_details: List[ColumnCompleteDetails],
                                        task_fields_dtos: List[TaskDTO],
                                        task_actions_dtos: List[ActionDTO],
                                        column_tasks: List[ColumnTasksDTO]
                                        ):
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
            self, task_complete_details_dto: List[TaskCompleteDetailsDTO],
            total_tasks: int) -> response.HttpResponse:
        pass

    @abc.abstractmethod
    def get_response_for_invalid_offset(self) -> response.HttpResponse:
        pass

    @abc.abstractmethod
    def get_response_for_invalid_limit(self) -> response.HttpResponse:
        pass

    @abc.abstractmethod
    def get_response_for_offset_exceeds_total_tasks(self) -> response.HttpResponse:
        pass

    @abc.abstractmethod
    def get_response_for_user_have_no_access_for_column(self) -> response.HttpResponse:
        pass

    @abc.abstractmethod
    def get_response_for_invalid_stage_ids(self, error) -> response.HttpResponse:
        pass

    @abc.abstractmethod
    def get_response_for_column_tasks(
            self, task_fields_dtos: List[TaskDTO],
            task_actions_dtos: List[ActionDTO],
            total_tasks: int,
            task_ids: List[int]):
        pass


class StageDisplayLogicPresenterInterface(abc.ABC):

    @abc.abstractmethod
    def get_response_for_invalid_stage_ids(self, error) -> response.HttpResponse:
        pass

    @abc.abstractmethod
    def get_response_for_stage_display_logic(self, task_status_dtos) -> response.HttpResponse:
        pass
