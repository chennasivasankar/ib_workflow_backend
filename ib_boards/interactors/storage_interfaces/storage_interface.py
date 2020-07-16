import abc
from typing import List

from ib_boards.interactors.dtos import CreateBoardDTO, ColumnDTO, BoardColumnDTO


class StorageInterface(abc.ABC):

    @abc.abstractmethod
    def validate_board_id(self, board_id):
        pass

    @abc.abstractmethod
    def create_boards_and_columns(
            self, board_dtos: List[CreateBoardDTO], column_dtos: List[ColumnDTO]) -> None:
        pass

    @abc.abstractmethod
    def check_for_column_ids_are_assigned_to_single_board(
            self, column_ids: List[str]):
        pass

    @abc.abstractmethod
    def get_board_ids_for_column_ids(self, column_ids: List[str]) -> List[str]:
        pass

    @abc.abstractmethod
    def get_board_column_ids(
            self, board_ids: List[str]) -> List[BoardColumnDTO]:
        pass

    @abc.abstractmethod
    def update_columns_for_board(self, column_dtos: List[ColumnDTO]) -> None:
        pass

    @abc.abstractmethod
    def create_columns_for_board(self, column_dtos) -> None:
        pass

    @abc.abstractmethod
    def delete_columns_which_are_not_in_configuration(
            self, column_for_delete_dtos: List[BoardColumnDTO]) -> None:
        pass

    @abc.abstractmethod
    def validate_user_role_with_boards_roles(self, user_role: str):
        pass

    @abc.abstractmethod
    def get_board_ids(
            self, user_role: str,) -> List[str]:
        pass

    @abc.abstractmethod
    def get_board_details(self, board_ids: List[str]) -> List[CreateBoardDTO]:
        pass

    @abc.abstractmethod
    def get_valid_board_ids(self, board_ids: List[str]) -> List[str]:
        pass
