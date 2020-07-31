"""
Created on: 21/07/20
Author: Pavankumar Pamuru

"""
from typing import List, Dict

from ib_boards.interactors.dtos import BoardDTO


class PopulateCreateBoardsAndColumns:

    def populate_create_boards_and_columns(self,
                                           boards_columns_dicts: List[Dict]):
        from ib_boards.populate.populate_script_for_add_or_delete_columns_for_board \
            import PopulateAddOrDeleteColumnsForBoard
        populate_script = PopulateAddOrDeleteColumnsForBoard()
        populate_script.validate_keys_in_given_dict(
            boards_columns_dicts=boards_columns_dicts
        )
        board_ids = []
        board_dtos = []

        for board_dict in boards_columns_dicts:
            if board_dict['board_id'] not in board_ids:
                board_ids.append(board_dict['board_id'])
                board_dto = self._convert_board_dict_to_board_dto(
                    board_dict=board_dict
                )
                board_dtos.append(board_dto)

        column_dtos = populate_script.get_column_dtos_from_dict(
            boards_columns_dicts
        )
        from ib_boards.storages.storage_implementation import \
            StorageImplementation
        storage = StorageImplementation()
        from ib_boards.interactors.create_boards_and_columns_interactor \
            import CreateBoardsAndColumnsInteractor
        interactor = CreateBoardsAndColumnsInteractor(storage=storage)
        interactor.create_boards_and_columns(
            board_dtos=board_dtos, column_dtos=column_dtos
        )
        return board_dtos, column_dtos

    @staticmethod
    def _convert_board_dict_to_board_dto(board_dict: Dict) -> BoardDTO:
        return BoardDTO(
            board_id=board_dict['board_id'],
            name=board_dict['board_display_name']
        )
