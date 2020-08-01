from typing import List

from ib_boards.interactors.get_board_complete_details_interactor import \
    GetBoardDetailsInteractor
from ib_boards.storages.storage_implementation import StorageImplementation


class BoardServiceInterface:

    @staticmethod
    def get_board_details(board_id: str, stage_ids: List[str], user_id: str):
        storage = StorageImplementation()
        interactor = GetBoardDetailsInteractor(storage)
        board_details_dto = interactor.get_board_details(
            board_id=board_id, stage_ids=stage_ids, user_id=user_id)
        return board_details_dto
