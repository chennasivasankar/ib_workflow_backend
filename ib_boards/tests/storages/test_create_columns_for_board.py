"""
Created on: 18/07/20
Author: Pavankumar Pamuru

"""
from typing import List

import pytest

from ib_boards.interactors.dtos import ColumnDTO, BoardDTO, \
    TaskTemplateStagesDTO, TaskSummaryFieldsDTO
from ib_boards.models import Board, Column
from ib_boards.storages.storage_implementation import StorageImplementation


@pytest.mark.django_db
class TestAddColumnsForBoard:

    @pytest.fixture
    def storage(self):
        return StorageImplementation()

    @pytest.fixture
    def reset_sequence(self):
        from ib_boards.tests.factories.models import BoardFactory, ColumnFactory
        from ib_boards.tests.factories.interactor_dtos import BoardDTOFactory
        from ib_boards.tests.factories.interactor_dtos import ColumnDTOFactory
        BoardDTOFactory.reset_sequence()
        ColumnDTOFactory.reset_sequence()
        BoardFactory.reset_sequence()
        ColumnFactory.reset_sequence()

    def test_with_valid_data_crates_data_for_board(
            self, storage, reset_sequence):
        # Arrange
        from ib_boards.tests.factories.interactor_dtos import \
            ColumnDTOFactory
        from ib_boards.tests.factories.models import BoardFactory
        board_dtos = BoardFactory.create_batch(2)
        column_dtos = ColumnDTOFactory.create_batch(2, board_id=board_dtos[0].board_id)
        column_dtos += ColumnDTOFactory.create_batch(2, board_id=board_dtos[1].board_id)

        # Act
        storage.create_columns_for_board(
            column_dtos=column_dtos
        )

        # Assert
        self._check_given_columns_data_created_correctly(
            column_dtos=column_dtos
        )

    def _check_given_columns_data_created_correctly(
            self, column_dtos: List[ColumnDTO]):
        column_objects = Column.objects.filter(
            board_id__in=['BOARD_ID_1', 'BOARD_ID_2'],
            column_id__in=[
                'COLUMN_ID_1', 'COLUMN_ID_2',
                'COLUMN_ID_3', 'COLUMN_ID_4'
            ]
        )
        assert len(column_objects) == len(column_dtos)
        for column_object, column_dto in zip(column_objects, column_dtos):
            assert column_object.column_id == column_dto.column_id
            assert column_object.board_id == column_dto.board_id
            assert column_object.name == column_dto.name
            assert column_object.display_order == column_dto.display_order
            assert column_object.name == column_dto.name
            assert column_object.task_selection_config == \
                self._get_json_string_for_task_selection_config(
                    column_dto.task_template_stages
                )
            assert column_object.kanban_brief_view_config == \
                self._get_json_string_for_view_config(
                    column_dto.kanban_view_fields
                )
            assert column_object.list_brief_view_config == \
                self._get_json_string_for_view_config(
                    column_dto.list_view_fields
                )

    @staticmethod
    def _get_json_string_for_task_selection_config(
            task_template_stages: List[TaskTemplateStagesDTO]):
        task_template_stages_dict = {}
        for task_template_stage in task_template_stages:
            task_template_stages_dict.update(
                {
                    task_template_stage.task_template_id: task_template_stage.stages
                }
            )
        import json
        return json.dumps(task_template_stages_dict)

    @staticmethod
    def _get_json_string_for_view_config(
            task_summary_fields: List[TaskSummaryFieldsDTO]):
        task_summary_fields_dict = {}
        for task_summary_field in task_summary_fields:
            task_summary_fields_dict.update(
                {
                    task_summary_field.task_id: task_summary_field.summary_fields
                }
            )
        import json
        return json.dumps(task_summary_fields_dict)
