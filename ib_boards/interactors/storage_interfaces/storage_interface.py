import abc
from typing import List

from ib_boards.interactors.dtos import BoardDTO, ColumnDTO


class StorageInterface(abc.ABC):

    @abc.abstractmethod
    def validate_board_id(self, board_id):
        pass

    @abc.abstractmethod
    def populate_data(
            self, board_dtos: List[BoardDTO], column_dtos: List[ColumnDTO]):
        pass
