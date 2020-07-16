import abc
from typing import List

from ib_boards.interactors.storage_interfaces.dtos import ColumnDetailsDTO


class StorageInterface(abc.ABC):

    @abc.abstractmethod
    def validate_board_id(self, board_id: str) -> bool:
        pass


    @abc.abstractmethod
    def get_columns_details(self, column_ids: List[str]) -> \
            List[ColumnDetailsDTO]:
        pass


    @abc.abstractmethod
    def get_column_ids_for_board(self, board_id: str, user_id: str) -> \
            List[str]:
        pass


    @abc.abstractmethod
    def check_if_user_has_permissions_for_board_id(self, board_id: str,
                                                   user_id: str) -> bool:
        pass