"""
Created on: 21/07/20
Author: Pavankumar Pamuru

"""
from typing import List, Dict

from ib_boards.interactors.dtos import BoardDTO, ColumnDTO


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
        board_dtos = [
            self._convert_board_dict_to_board_dto(board_dict=board_dict)
            for board_dict in boards_columns_dicts
            if board_dict['board_id'] not in board_ids
        ]
        column_dtos = populate_script.get_column_dtos_from_dict(
            boards_columns_dicts
        )
        from ib_boards.populate.populate_script_for_add_or_delete_columns_for_board import \
            StorageImplementation
        storage = StorageImplementation()
        from ib_boards.interactors.create_boards_and_columns_interactor \
            import CreateBoardsAndColumnsInteractor
        interactor = CreateBoardsAndColumnsInteractor(storage=storage)
        interactor.create_boards_and_columns(
            board_dtos=board_dtos, column_dtos=column_dtos
        )

    @staticmethod
    def _convert_board_dict_to_board_dto(board_dict: Dict) -> BoardDTO:
        return BoardDTO(
            board_id=board_dict['board_id'],
            display_name=board_dict['board_display_name']
        )
