"""
Created on: 14/07/20
Author: Pavankumar Pamuru

"""
from typing import List

from ib_boards.interactors.dtos import ColumnDTO, BoardColumnsDTO, \
    TaskSummaryFieldsDTO, TaskTemplateStagesDTO
from ib_boards.interactors.storage_interfaces.storage_interface import \
    StorageInterface


class AddOrDeleteColumnsForBoardInteractor:
    def __init__(self, storage: StorageInterface):
        self.storage = storage

    def add_or_delete_columns_for_board_wrapper(
            self, column_dtos: List[ColumnDTO]):
        self.add_or_delete_columns_for_board(
            column_dtos=column_dtos
        )

    def add_or_delete_columns_for_board(self, column_dtos: List[ColumnDTO]):

        self._validate_columns_data(column_dtos=column_dtos)
        board_ids = [column_dto.board_id for column_dto in column_dtos]
        board_ids = list(set(board_ids))
        present_column_ids = self.storage.get_boards_column_ids(
            board_ids=board_ids
        )
        from collections import defaultdict
        board_column_map = defaultdict(lambda: [])
        for column_dto in column_dtos:
            board_column_map[column_dto.board_id].append(
                column_dto.column_id
            )
        column_dtos_dict = {}
        for column_dto in column_dtos:
            column_dtos_dict[column_dto.column_id] = column_dto
        self._delete_columns_which_are_not_in_configuration(
            board_column_map=board_column_map
        )
        self._create_columns_for_board(
            present_column_ids=present_column_ids,
            column_dtos_dict=column_dtos_dict
        )
        self._update_columns_for_board(
            present_column_ids=present_column_ids,
            column_dtos_dict=column_dtos_dict
        )

    def _create_columns_for_board(
            self, present_column_ids, column_dtos_dict):
        columns_dtos_for_create = [
            column_dtos_dict[column_id]
            for column_id in column_dtos_dict.keys()
            if column_id not in present_column_ids
        ]
        self.storage.create_columns_for_board(
            column_dtos=columns_dtos_for_create
        )

    def _update_columns_for_board(
            self, present_column_ids, column_dtos_dict):
        column_dto_for_update = [
            column_dtos_dict[column_id]
            for column_id in present_column_ids
        ]
        self.storage.update_columns_for_board(
            column_dtos=column_dto_for_update
        )

    def _delete_columns_which_are_not_in_configuration(self, board_column_map):

        column_for_delete_dtos = [
            BoardColumnsDTO(
                board_id=key,
                column_ids=value
            )
            for key, value in board_column_map.items()
        ]
        self.storage.delete_columns_which_are_not_in_configuration(
            column_for_delete_dtos=column_for_delete_dtos
        )

    def _validate_columns_data(self, column_dtos: List[ColumnDTO]):

        from ib_boards.interactors.create_boards_and_columns_interactor import \
            CreateBoardsAndColumnsInteractor
        create_boards_and_columns_interactor = CreateBoardsAndColumnsInteractor(
            storage=self.storage
        )
        create_boards_and_columns_interactor.validate_columns_data(
            column_dtos=column_dtos
        )
        self._check_for_column_ids_are_assigned_to_single_board(
            column_dtos=column_dtos
        )

    def _check_for_column_ids_are_assigned_to_single_board(
            self, column_dtos: List[ColumnDTO]):
        from collections import defaultdict
        board_column_map = defaultdict(lambda: [])

        for column_dto in column_dtos:
            board_column_map[column_dto.board_id].append(
                column_dto.column_id
            )
        column_ids = [column_dto.column_id for column_dto in column_dtos]
        board_column_dtos = self.storage.get_board_ids_for_column_ids(
            column_ids=column_ids
        )
    #     self._check_for_column_ids_are_having_single_board_id(
    #         board_column_dtos=board_column_dtos,
    #         board_column_map=board_column_map
    #     )
    #
    # @staticmethod
    # def _check_for_column_ids_are_having_single_board_id(
    #         board_column_dtos: List[BoardColumnDTO], board_column_map):
    #     for board_column_dto in board_column_dtos:
    #         column_board_map[board_column_dto.column_id]
    #
    #
    #     is_having_multiple_boards = (
    #             len(board_ids) == 1 and key not in board_ids
    #             or len(board_ids) > 1
    #     )
    #     if is_having_multiple_boards:
    #         raise ColumnIdsAssignedToDifferentBoard(column_ids=value)
