import abc
from typing import List

from ib_boards.interactors.storage_interfaces.dtos import BoardColumnDTO, \
    ColumnDetailsDTO
from ib_boards.interactors.dtos import BoardDTO, ColumnDTO, BoardColumnsDTO
from ib_boards.interactors.storage_interfaces.dtos import BoardColumnDTO


class StorageInterface(abc.ABC):

    @abc.abstractmethod
    def validate_board_id(self, board_id):
        pass

    @abc.abstractmethod
    def create_boards_and_columns(
            self, board_dtos: List[BoardDTO],
            column_dtos: List[ColumnDTO]) -> None:
        pass

    @abc.abstractmethod
    def get_board_ids_for_column_ids(self, column_ids: List[str]) -> List[str]:
        pass

    @abc.abstractmethod
    def get_boards_column_ids(
            self, board_ids: List[str]) -> List[BoardColumnDTO]:
        pass

    @abc.abstractmethod
    def update_columns_for_board(self, column_dtos: List[ColumnDTO]) -> None:
        pass

    @abc.abstractmethod
    def create_columns_for_board(self, column_dtos: List[ColumnDTO]) -> None:
        pass

    @abc.abstractmethod
    def delete_columns_which_are_not_in_configuration(
            self, column_for_delete_dtos: List[BoardColumnsDTO]) -> None:
        pass

    @abc.abstractmethod
    def validate_user_role_with_boards_roles(self, user_role: str):
        pass

    @abc.abstractmethod
    def get_board_ids(
            self, user_role: str,) -> List[str]:
        pass

    @abc.abstractmethod
    def get_board_details(self, board_ids: List[str]) -> List[BoardDTO]:
        pass

    @abc.abstractmethod
    def get_valid_board_ids(self, board_ids: List[str]) -> List[str]:
        pass

    @abc.abstractmethod
    def validate_column_id(self, column_id: str) -> None:
        pass

    @abc.abstractmethod
    def get_column_display_stage_ids(self, column_id: str) -> List[str]:
        pass

    @abc.abstractmethod
    def validate_user_role_with_column_roles(self, user_role: str):
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
