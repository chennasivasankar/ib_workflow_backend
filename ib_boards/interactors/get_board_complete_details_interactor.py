from typing import List

from ib_boards.adapters.service_adapter import get_service_adapter
from ib_boards.exceptions.custom_exceptions import InvalidBoardId, InvalidStageIds, UserDonotHaveAccess


class GetBoardDetailsInteractor:
    def __init__(self, storage):
        self.storage = storage

    def get_board_details(self, board_id: str, stage_ids: List[str],
                          user_id: str):
        is_valid = self.storage.validate_board_id(board_id)
        if not is_valid:
            raise InvalidBoardId

        user_service = get_service_adapter().iam_service
        user_roles = user_service.get_user_roles(user_id)
        self._validate_if_user_has_permissions_for_given_board_id(
            board_id=board_id, user_roles=user_roles)

        board_details = self.storage.get_board_complete_details(board_id, stage_ids)
        return board_details

    def _validate_if_user_has_permissions_for_given_board_id(self,
                                                             board_id: str,
                                                             user_roles: str):
        board_permitted_user_roles = self.storage. \
            get_permitted_user_roles_for_board(board_id=board_id)
        has_permission = False
        for board_permitted_user_role in board_permitted_user_roles:
            if board_permitted_user_role in user_roles:
                has_permission = True
                break

        if not has_permission:
            raise UserDonotHaveAccess
        return
