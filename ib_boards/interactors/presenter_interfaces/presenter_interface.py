import abc
from typing import List

from django.http import response

from ib_boards.exceptions.custom_exceptions import InvalidBoardIds
from ib_boards.interactors.storage_interfaces.dtos import BoardDTO


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