import abc
from abc import ABC
from dataclasses import dataclass
from typing import List

from django.http import response

from ib_boards.adapters.iam_service import InvalidProjectIdsException
from ib_boards.interactors.dtos import ActionDTO, \
    TaskCompleteDetailsDTO, FieldDTO, StarredAndOtherBoardsDTO, TaskStageDTO, \
    StageAssigneesDTO, TaskBaseAndCompleteDetailsDTO, \
    TaskCompleteDetailsWithAllFieldsDTO
from ib_boards.interactors.storage_interfaces.dtos import ColumnCompleteDetails, \
    AllFieldsDTO

from ib_boards.interactors.dtos import ColumnTasksDTO
from ib_boards.interactors.storage_interfaces.dtos import (
    TaskFieldsDTO, TaskActionsDTO)


@dataclass
class TaskDisplayIdDTO:
    task_id: int
    display_id: str


@dataclass
class CompleteTasksDetailsDTO:
    task_fields_dtos: List[FieldDTO]
    task_actions_dtos: List[ActionDTO]
    total_tasks: int
    task_id_dtos: List[TaskDisplayIdDTO]
    task_stage_dtos: List[TaskStageDTO]
    assignees_dtos: List[StageAssigneesDTO]


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
            self, starred_and_other_boards_dto: StarredAndOtherBoardsDTO,
            total_boards: int) -> response.HttpResponse:
        pass

    @abc.abstractmethod
    def get_response_for_offset_exceeds_total_tasks(self):
        pass

    @abc.abstractmethod
    def get_response_for_invalid_project_id(self, error: InvalidProjectIdsException)\
            -> response.HttpResponse:
        pass

    @abc.abstractmethod
    def get_response_for_user_is_not_in_project(self) \
            -> response.HttpResponse:
        pass


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
    def get_response_for_column_details(
            self, column_details: List[ColumnCompleteDetails],
            column_tasks: List[ColumnTasksDTO],
            tasks_complete_details_dto: TaskBaseAndCompleteDetailsDTO):
        pass

    @abc.abstractmethod
    def get_response_for_offset_exceeds_total_tasks(self):
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
            self, task_complete_details_dto: TaskBaseAndCompleteDetailsDTO, total_tasks: int, task_ids: List[int]):
        pass


class GetColumnTasksListViewPresenterInterface(abc.ABC):

    @abc.abstractmethod
    def get_response_for_the_invalid_column_id(self):
        pass

    @abc.abstractmethod
    def get_response_for_invalid_offset(self) -> response.HttpResponse:
        pass

    @abc.abstractmethod
    def get_response_for_invalid_limit(self) -> response.HttpResponse:
        pass

    @abc.abstractmethod
    def get_response_for_offset_exceeds_total_tasks(
            self) -> response.HttpResponse:
        pass

    @abc.abstractmethod
    def get_response_for_user_have_no_access_for_column(
            self) -> response.HttpResponse:
        pass

    @abc.abstractmethod
    def get_response_for_invalid_stage_ids(self,
                                           error) -> response.HttpResponse:
        pass

    @abc.abstractmethod
    def get_response_for_column_tasks_in_list_view(
            self, task_complete_details: TaskCompleteDetailsWithAllFieldsDTO):
        pass


class FieldsDisplayStatusPresenterInterface(abc.ABC):

    @abc.abstractmethod
    def get_response_for_the_invalid_column_id(self):
        pass

    @abc.abstractmethod
    def get_response_for_user_have_no_access_for_column(self):
        pass

    @abc.abstractmethod
    def get_response_for_field_not_belongs_to_column(self):
        pass


class FieldsDisplayOrderPresenterInterface(abc.ABC):

    @abc.abstractmethod
    def get_response_for_the_invalid_column_id(self):
        pass

    @abc.abstractmethod
    def get_response_for_user_have_no_access_for_column(self):
        pass

    @abc.abstractmethod
    def get_response_for_field_not_belongs_to_column(self, error):
        pass

    @abc.abstractmethod
    def get_response_for_the_invalid_display_order(self):
        pass

    def get_response_for_field_order_in_column(
            self, all_fields: List[AllFieldsDTO]):
        pass

