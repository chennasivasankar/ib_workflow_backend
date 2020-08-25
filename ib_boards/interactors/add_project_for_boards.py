from typing import List

from ib_boards.exceptions.custom_exceptions import InvalidBoardIdsException
from ib_boards.interactors.dtos import ProjectBoardDTO
from ib_boards.interactors.mixins.validation_mixins import ValidationMixin
from ib_boards.interactors.storage_interfaces.storage_interface import StorageInterface


class AddProjectForBoardsInteractor(ValidationMixin):
    def __init__(self, storage: StorageInterface):
        self.storage = storage

    def add_project_for_boards(self,
                               project_boards_dtos: List[ProjectBoardDTO]):
        project_ids = self._get_project_ids(project_boards_dtos)
        self.validate_given_project_ids(project_ids=project_ids)
        board_ids = self._get_board_ids(project_boards_dtos)
        self._validate_board_ids(board_ids)
        self.storage.add_project_id_for_boards(project_boards_dtos)

    @staticmethod
    def _get_board_ids(project_boards_dtos: List[ProjectBoardDTO]):
        board_ids = [item.board_id for item in project_boards_dtos]
        return board_ids

    @staticmethod
    def _get_project_ids(project_boards_dtos: List[ProjectBoardDTO]):
        project_ids = [item.project_id for item in project_boards_dtos]
        return project_ids

    def _validate_board_ids(self, board_ids: List[str]):
        valid_board_ids = self.storage.get_valid_board_ids(board_ids)
        invalid_board_ids = [
            board_id for board_id in board_ids
            if board_id not in valid_board_ids
        ]
        if invalid_board_ids:
            raise InvalidBoardIdsException(invalid_board_ids)
