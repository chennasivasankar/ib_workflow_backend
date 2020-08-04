"""
Created on: 16/07/20
Author: Pavankumar Pamuru

"""
from typing import List

from ib_boards.exceptions.custom_exceptions import InvalidBoardIds
from ib_boards.interactors.storage_interfaces.storage_interface import \
    StorageInterface


class GetBoardsDetailsInteractor:
    def __init__(self, storage: StorageInterface):
        self.storage = storage

    def get_boards_details(self, board_ids: List[str]):
        board_ids = self.get_unique_board_ids(board_ids=board_ids)
        self._validate_board_ids(board_ids=board_ids)
        board_details_dtos = self.storage.get_board_details(
            board_ids=board_ids
        )
        return board_details_dtos

    @staticmethod
    def get_unique_board_ids(board_ids):
        return sorted(list(set(board_ids)))

    def _validate_board_ids(self, board_ids):
        valid_board_ids = self.storage.get_valid_board_ids(board_ids=board_ids)
        invalid_board_ids = [
            board_id
            for board_id in board_ids
            if board_id not in valid_board_ids
        ]

        if invalid_board_ids:
            raise InvalidBoardIds(board_ids=invalid_board_ids)
