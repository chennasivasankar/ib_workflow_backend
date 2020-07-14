"""
Created on: 13/07/20
Author: Pavankumar Pamuru

"""
from typing import List

from ib_boards.interactors.dtos import BoardDTO, ColumnDTO
from ib_boards.interactors.storage_interfaces.storage_interface import \
    StorageInterface


class PopulateScriptInteractor:
    def __init__(self, storage: StorageInterface):
        self.storage = storage

    def populate_script_wrapper(
            self, board_dtos: List[BoardDTO], column_dtos: List[ColumnDTO]):
        self.populate_script(
            board_dtos=board_dtos,
            column_dtos=column_dtos
        )

    def populate_script(
            self, board_dtos: List[BoardDTO], column_dtos: List[ColumnDTO]):

        board_ids = [board_dto.board_id for board_dto in board_dtos]
        column_ids = [column_dto.column_id for column_dto in column_dtos]
        self._validate_board_ids(board_ids=board_ids)
        self._validate_board_display_name(board_dtos=board_dtos)
        self._validate_column_ids(column_ids=column_ids)
        self._validate_column_display_name(column_dtos=column_dtos)
        self._validate_task_template_stages_json(column_dtos=column_dtos)
        self._validate_task_template_ids_in_task_template_stage(
            column_dtos=column_dtos
        )
        self._validate_task_template_summary_fields_json(
            column_dtos=column_dtos
        )
        self._validate_task_template_ids_in_task_template_fields(
            column_dtos=column_dtos
        )

    @staticmethod
    def _validate_board_ids(board_ids: List[str]):
        import collections
        duplicate_board_ids = [
            board_id for board_id, count in
            collections.Counter(board_ids).items()
            if count > 1
        ]
        if duplicate_board_ids:
            from ib_boards.exceptions.custom_exceptions import DuplicateBoardIds
            raise DuplicateBoardIds(board_ids=duplicate_board_ids)

    @staticmethod
    def _validate_board_display_name(board_dtos: List[BoardDTO]):
        for board_dto in board_dtos:
            is_invalid_display_name = not board_dto.display_name
            if is_invalid_display_name:
                from ib_boards.exceptions.custom_exceptions import \
                    InvalidBoardDisplayName
                raise InvalidBoardDisplayName(board_id=board_dto.board_id)

    @staticmethod
    def _validate_column_ids(column_ids: List[str]):
        import collections
        duplicate_column_ids = [
            column_id for column_id, count in
            collections.Counter(column_ids).items()
            if count > 1
        ]
        if duplicate_column_ids:
            from ib_boards.exceptions.custom_exceptions import \
                DuplicateColumnIds
            raise DuplicateColumnIds(column_ids=duplicate_column_ids)

    @staticmethod
    def _validate_column_display_name(column_dtos: List[ColumnDTO]):
        for column_dto in column_dtos:
            is_invalid_display_name = not column_dto.display_name
            if is_invalid_display_name:
                from ib_boards.exceptions.custom_exceptions import \
                    InvalidColumnDisplayName
                raise InvalidColumnDisplayName(column_id=column_dto.column_id)

    @staticmethod
    def _validate_task_template_stages_json(column_dtos: List[ColumnDTO]):
        import json
        for column_dto in column_dtos:
            try:
                json.loads(column_dto.task_template_stages)
            except json.JSONDecodeError:
                from ib_boards.exceptions.custom_exceptions import \
                    InvalidJsonForTaskTemplateStages
                raise InvalidJsonForTaskTemplateStages

    @staticmethod
    def _validate_task_template_ids_in_task_template_stage(
            column_dtos: List[ColumnDTO]):
        import json
        task_template_ids = []
        for column_dto in column_dtos:
            task_template_stages = json.loads(column_dto.task_template_stages)
            task_template_ids += task_template_stages.keys()

        from ib_boards.adapters.service_adapter import  get_service_adapter

        service_adapter = get_service_adapter()

        service_adapter.task_service.validate_task_template_ids(
            task_template_ids=task_template_ids
        )

    @staticmethod
    def _validate_task_template_ids_in_task_template_fields(
            column_dtos: List[ColumnDTO]):
        import json
        task_template_ids = []
        for column_dto in column_dtos:
            task_summary_fields = json.loads(column_dto.task_summary_fields)
            task_template_ids += task_summary_fields.keys()

        from ib_boards.adapters.service_adapter import get_service_adapter

        service_adapter = get_service_adapter()

        service_adapter.task_service.validate_task_template_ids(
            task_template_ids=task_template_ids
        )

    @staticmethod
    def _validate_task_template_summary_fields_json(column_dtos: List[ColumnDTO]):
        import json
        for column_dto in column_dtos:
            try:
                json.loads(column_dto.task_summary_fields)
            except json.JSONDecodeError:
                from ib_boards.exceptions.custom_exceptions import \
                    InvalidJsonForTaskTemplateSummaryFields
                raise InvalidJsonForTaskTemplateSummaryFields

