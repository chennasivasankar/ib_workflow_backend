import abc
from typing import List

from django.http import response

from ib_boards.interactors.dtos import ActionDTO, \
    TaskCompleteDetailsDTO, FieldDTO, StarredAndOtherBoardsDTO, TaskStageColorDTO
from ib_boards.interactors.storage_interfaces.dtos import ColumnCompleteDetails

from ib_boards.interactors.dtos import ColumnTasksDTO
from ib_boards.interactors.storage_interfaces.dtos import (
    TaskFieldsDTO, TaskActionsDTO)


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
                                        task_fields_dtos: List[FieldDTO],
                                        task_actions_dtos: List[ActionDTO],
                                        column_tasks: List[ColumnTasksDTO],
                                        task_stage_color_dtos: List[TaskStageColorDTO]
                                        ):
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
            self, task_fields_dtos: List[FieldDTO],
            task_actions_dtos: List[ActionDTO],
            total_tasks: int,
            task_ids: List[int],
            task_stage_color_dtos: List[TaskStageColorDTO]):
        pass
