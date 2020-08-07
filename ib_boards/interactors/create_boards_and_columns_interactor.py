"""
Created on: 13/07/20
Author: Pavankumar Pamuru

"""
from typing import List

from ib_boards.exceptions.custom_exceptions import \
    TaskSummaryFieldsNotBelongsToTaskTemplateId, \
    TaskListViewFieldsNotBelongsToTaskTemplateId, \
    EmptyValuesForTaskSummaryFields, EmptyValuesForTaskListViewFields, \
    InvalidTaskIdInListViewFields, InvalidTaskIdInSummaryFields, \
    InvalidTaskIdInKanbanViewFields, EmptyValuesForTaskKanbanViewFields, \
    InvalidUserRoles
from ib_boards.interactors.dtos import BoardDTO, ColumnDTO, \
    TaskTemplateStagesDTO, TaskSummaryFieldsDTO
from ib_boards.interactors.storage_interfaces.storage_interface import \
    StorageInterface


class CreateBoardsAndColumnsInteractor:
    def __init__(self, storage: StorageInterface):
        self.storage = storage

    def create_boards_and_columns(
            self, board_dtos: List[BoardDTO], column_dtos: List[ColumnDTO]):
        self._validate_board_display_name(board_dtos=board_dtos)
        self._validate_columns_data(column_dtos)
        board_dtos, column_dtos = self._get_boards_and_columns_need_to_create(
            board_dtos=board_dtos, column_dtos=column_dtos
        )
        print(board_dtos, column_dtos)
        boards_columns_to_create = board_dtos and column_dtos
        if boards_columns_to_create:
            self.storage.create_boards_and_columns(
                board_dtos=board_dtos,
                column_dtos=column_dtos
            )

    def _get_boards_and_columns_need_to_create(self, board_dtos, column_dtos):
        existing_board_ids = self.storage.get_existing_board_ids()
        from collections import defaultdict
        board_columns_dict = defaultdict(lambda: [])
        for column_dto in column_dtos:
            board_columns_dict[column_dto.board_id].append(
                column_dto
            )
        new_board_dtos = []
        new_column_dtos = []
        for board_dto in board_dtos:
            if board_dto.board_id not in existing_board_ids:
                new_board_dtos.append(board_dto)
                new_column_dtos += board_columns_dict[board_dto.board_id]

        return new_board_dtos, new_column_dtos

    @staticmethod
    def _validate_board_display_name(board_dtos: List[BoardDTO]):
        for board_dto in board_dtos:
            is_invalid_display_name = not board_dto.name
            if is_invalid_display_name:
                from ib_boards.exceptions.custom_exceptions import \
                    InvalidBoardDisplayName
                raise InvalidBoardDisplayName(board_id=board_dto.board_id)

    def _validate_columns_data(self, column_dtos: List[ColumnDTO]):

        from ib_boards.interactors.add_or_delete_columns_for_board_interactor import \
            AddOrDeleteColumnsForBoardInteractor
        create_boards_and_columns_interactor = AddOrDeleteColumnsForBoardInteractor(
            storage=self.storage
        )
        create_boards_and_columns_interactor.validate_columns_data(
            column_dtos=column_dtos
        )
