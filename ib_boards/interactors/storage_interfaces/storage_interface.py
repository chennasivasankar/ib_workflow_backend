import abc
from typing import List

from ib_boards.interactors.dtos import BoardDTO, ColumnDTO, BoardColumnDTO


class StorageInterface(abc.ABC):

    @abc.abstractmethod
    def validate_board_id(self, board_id):
        pass

    @abc.abstractmethod
    def populate_data(
            self, board_dtos: List[BoardDTO], column_dtos: List[ColumnDTO]):
        pass

    @abc.abstractmethod
    def check_for_column_ids_are_assigned_to_single_board(
            self, column_ids: List[str]):
        pass

    @abc.abstractmethod
    def get_board_ids_for_column_ids(self, column_ids: List[str]):
        pass

    @abc.abstractmethod
    def get_board_column_ids(self, board_ids: List[str]):
        pass

    @abc.abstractmethod
    def update_columns_for_board(self, column_dtos: List[ColumnDTO]):
        pass

    @abc.abstractmethod
    def create_columns_for_board(self, column_dtos):
        pass

    @abc.abstractmethod
    def delete_columns_which_are_not_in_configuration(
            self, column_for_delete_dtos: List[BoardColumnDTO]):
        pass
