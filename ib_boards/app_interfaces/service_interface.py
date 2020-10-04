from typing import List

from ib_boards.interactors.get_board_complete_details_interactor import \
    GetBoardDetailsInteractor
from ib_boards.interactors.storage_interfaces.dtos import ColumnStageIdsDTO
from ib_boards.storages.storage_implementation import StorageImplementation


class BoardServiceInterface:

    @staticmethod
    def get_board_details(board_id: str, stage_ids: List[str], user_id: str):
        storage = StorageImplementation()
        interactor = GetBoardDetailsInteractor(storage)
        board_details_dto = interactor.get_board_details(
            board_id=board_id, stage_ids=stage_ids, user_id=user_id)
        return board_details_dto

    @staticmethod
    def validate_given_board_id(board_id: str):
        storage = StorageImplementation()
        interactor = GetBoardDetailsInteractor(storage)
        return interactor.validate_board_id(board_id)

    @staticmethod
    def get_stage_ids_based_on_column(column_id: str) -> List[ColumnStageIdsDTO]:
        storage = StorageImplementation()
        from ib_boards.interactors.get_tasks_details_for_the_column_ids import \
            GetColumnsTasksDetailsInteractor
        interactor = GetColumnsTasksDetailsInteractor(
            storage=storage
        )
        column_stage_dtos = interactor.get_column_stage_dtos(
            column_ids=[column_id]
        )
        return column_stage_dtos
