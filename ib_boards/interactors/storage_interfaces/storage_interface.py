import abc
from typing import List, Optional

from ib_boards.interactors.storage_interfaces.dtos import ColumnDetailsDTO, BoardDTO, BoardColumnDTO


class StorageInterface(abc.ABC):

    @abc.abstractmethod
    def validate_board_id(self, board_id: str) -> bool:
        pass

    @abc.abstractmethod
    def get_columns_details(self, column_ids: List[str]) -> \
            List[ColumnDetailsDTO]:
        pass

    @abc.abstractmethod
    def get_column_ids_for_board(self, board_id: str, user_roles: List[str]) \
            -> List[str]:
        pass

    @abc.abstractmethod
    def get_permitted_user_roles_for_board(self, board_id: str) -> List[str]:
        pass

    @abc.abstractmethod
    def get_board_details(self, board_id: str) -> BoardDTO:
        pass

    @abc.abstractmethod
    def get_column_details(self, board_id: str, user_roles: List[str]) \
            -> List[BoardColumnDTO]:
        pass
