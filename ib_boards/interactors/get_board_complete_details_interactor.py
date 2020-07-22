from typing import List

from ib_boards.adapters.service_adapter import get_service_adapter
from ib_boards.exceptions.custom_exceptions import InvalidBoardId, InvalidStageIds


class GetBoardDetailsInteractor:
    def __init__(self, storage):
        self.storage = storage

    def get_board_details(self, board_id: str, stage_ids: List[str],
                          user_id: str):
        is_valid = self.storage.validate_board_id(board_id)
        if not is_valid:
            raise InvalidBoardId

        board_dto = self.storage.get_board_details(board_id)

        user_service = get_service_adapter().user_roles_service
        user_roles = user_service.get_user_roles(user_id)
        column_ids = self.storage.get_column_ids_for_board(board_id, user_roles)
        column_dtos, field_dtos, column_stages_dto = self.storage.get_columns_details(column_ids)


