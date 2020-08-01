from typing import List

from ib_boards.interactors.get_board_complete_details_interactor import GetBoardDetailsInteractor
from ib_boards.storages.storage_implementation import StorageImplementation


class ServiceInterface:
    def get_board_and_columns_details(self, board_id: str, user_id: str,
                                      stage_ids: List[str]):
        storage = StorageImplementation()
        interactor = GetBoardDetailsInteractor(storage)
        board_details = interactor.get_board_details(board_id=board_id,
                                                     )
