"""
Created on: 21/07/20
Author: Pavankumar Pamuru

"""
import pytest

from ib_boards.models import Board, Column, ColumnPermission
from ib_boards.populate.populate_script_for_add_or_delete_columns_for_board import \
    InvalidDataFormat, InvalidJsonFormat
from ib_boards.populate.populate_script_to_create_boards_and_columns import \
    PopulateCreateBoardsAndColumns


@pytest.mark.django_db
class TestPopulateBoardsAndColumnsInteractor:

    @pytest.fixture
    def sequence_reset(self):
        from ib_boards.tests.factories.interactor_dtos import \
            TaskTemplateStagesDTOFactory
        TaskTemplateStagesDTOFactory.reset_sequence()
        from ib_boards.tests.factories.interactor_dtos import \
            TaskSummaryFieldsDTOFactory
        TaskSummaryFieldsDTOFactory.reset_sequence()

    def test_with_invalid_keys_in_dict_raise_exception(self):
        # Arrange
        from ib_boards.tests.common_fixtures.populate_data import \
            populate_dict_with_invalid_keys

        data_dict = populate_dict_with_invalid_keys()
        populate_script = PopulateCreateBoardsAndColumns()

        # Act
        with pytest.raises(InvalidDataFormat) as error:
            populate_script.populate_create_boards_and_columns(
                boards_columns_dicts=data_dict
            )

        # Assert

    def test_with_invalid_json_in_template_stages_dict_raise_exception(self):
        # Arrange
        from ib_boards.tests.common_fixtures.populate_data import \
            populate_dict_with_invalid_json

        data_dict = populate_dict_with_invalid_json()
        populate_script = PopulateCreateBoardsAndColumns()

        # Act
        with pytest.raises(InvalidJsonFormat) as error:
            populate_script.populate_create_boards_and_columns(
                boards_columns_dicts=data_dict
            )

    def test_with_invalid_json_in_task_summary_fields_dict_raise_exception(
            self):
        # Arrange
        from ib_boards.tests.common_fixtures.populate_data import \
            populate_dict_with_invalid_json_for_summary_fields

        data_dict = populate_dict_with_invalid_json_for_summary_fields()
        populate_script = PopulateCreateBoardsAndColumns()

        # Act
        with pytest.raises(InvalidJsonFormat) as error:
            populate_script.populate_create_boards_and_columns(
                boards_columns_dicts=data_dict
            )

    def test_with_valid_data_return_dtos(self, snapshot, mocker,
                                         sequence_reset):
        # Arrange
        from ib_boards.tests.common_fixtures.populate_data import \
            populate_dict_with_valid_data

        data_dict = populate_dict_with_valid_data()
        populate_script = PopulateCreateBoardsAndColumns()
        user_roles = ["USER", 'ADMIN']
        from ib_boards.tests.common_fixtures.adapters.iam_service import \
            adapter_mock
        adapter_mock = adapter_mock(mocker=mocker,
                                    user_roles=user_roles)

        task_template_ids_for_stages = [
            'FIN_PR', 'FIN_IN',
        ]
        task_template_ids_list_view = [
            'FIN_PR', 'FIN_IN',
        ]
        task_template_ids_kanban_view = [
            'FIN_PR', 'FIN_IN',
        ]
        from ib_boards.tests.common_fixtures.adapters.task_service import \
            get_valid_task_ids_for_kanban_view_mock
        get_valid_task_ids_for_kanban_view_mock(
            mocker=mocker,
            task_template_ids_for_stages=task_template_ids_for_stages,
            task_template_ids_list_view=task_template_ids_list_view,
            task_ids=task_template_ids_kanban_view
        )

        # Act
        populate_script.populate_create_boards_and_columns(
            boards_columns_dicts=data_dict
        )

        # Assert

        boards = Board.objects.all()
        columns = Column.objects.all()
        column_permissions = ColumnPermission.objects.all()

        snapshot.assert_match(boards, "boards")
        snapshot.assert_match(columns, "columns")
        snapshot.assert_match(column_permissions, "column_permissions")
