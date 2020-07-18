"""
Created on: 18/07/20
Author: Pavankumar Pamuru

"""
from typing import List

from ib_boards.interactors.dtos import CreateBoardDTO, ColumnDTO, BoardColumnDTO
from ib_boards.interactors.storage_interfaces.storage_interface import \
    StorageInterface
from ib_boards.models import Board


class StorageImplementation(StorageInterface):

    def validate_board_id(self, board_id):
        is_board_id_invalid = not Board.objects.filter(
            board_id=board_id
        ).exists()
        if is_board_id_invalid:
            from ib_boards.exceptions.custom_exceptions import InvalidBoardId
            raise InvalidBoardId

    def create_boards_and_columns(
            self, board_dtos: List[CreateBoardDTO], column_dtos: List[ColumnDTO]) -> None:
        pass

    def check_for_column_ids_are_assigned_to_single_board(
            self, column_ids: List[str]):
        pass

    def get_board_ids_for_column_ids(self, column_ids: List[str]) -> List[str]:
        pass

    def get_board_column_ids(
            self, board_ids: List[str]) -> List[BoardColumnDTO]:
        pass

    def update_columns_for_board(self, column_dtos: List[ColumnDTO]) -> None:
        pass

    def create_columns_for_board(self, column_dtos) -> None:
        pass

    def delete_columns_which_are_not_in_configuration(
            self, column_for_delete_dtos: List[BoardColumnDTO]) -> None:
        pass

    def validate_user_role_with_boards_roles(self, user_role: str):
        pass

    def get_board_ids(
            self, user_role: str,) -> List[str]:
        pass

    def get_board_details(self, board_ids: List[str]) -> List[CreateBoardDTO]:
        pass

    def get_valid_board_ids(self, board_ids: List[str]) -> List[str]:
        pass

    def validate_column_id(self, column_id: str) -> None:
        pass

    def get_column_display_stage_ids(self, column_id: str) -> List[str]:
        pass

    def validate_user_role_with_column_roles(self, user_role: str):
        pass
