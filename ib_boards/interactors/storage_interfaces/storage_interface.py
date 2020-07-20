import abc
from typing import List

from ib_boards.interactors.dtos import BoardDTO, ColumnDTO, BoardColumnDTO


class StorageInterface(abc.ABC):

    @abc.abstractmethod
    def create_boards_and_columns(
            self, board_dtos: List[BoardDTO],
            column_dtos: List[ColumnDTO]) -> None:
        pass

    @abc.abstractmethod
    def get_board_ids_for_column_ids(self, column_ids: List[str]) -> List[str]:
        pass

    @abc.abstractmethod
    def get_boards_column_ids(self, board_ids: List[str]) -> List[str]:
        pass

    @abc.abstractmethod
    def update_columns_for_board(self, column_dtos: List[ColumnDTO]) -> None:
        pass

    @abc.abstractmethod
    def create_columns_for_board(self, column_dtos: List[ColumnDTO]) -> None:
        pass

    @abc.abstractmethod
    def delete_columns_which_are_not_in_configuration(
            self, column_for_delete_dtos: List[BoardColumnDTO]) -> None:
        pass
