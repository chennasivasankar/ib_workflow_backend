"""
Created on: 21/07/20
Author: Pavankumar Pamuru

"""
import pytest

from ib_boards.populate.populate_script_for_add_or_delete_columns_for_board import \
    InvalidDataFormat, InvalidJsonFormat
from ib_boards.populate.populate_script_to_create_boards_and_columns import \
    PopulateCreateBoardsAndColumns


class TestPopulateBoardsAndColumnsInteractor:

    def test_with_invalid_keys_in_dict_raise_exception(self):
        # Arrange
        from ib_boards.tests.common_fixtures.populate_data import\
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

    def test_with_invalid_json_in_task_summary_fields_dict_raise_exception(self):
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

    def test_with_valid_data_return_dtos(self):
        # Arrange
        from ib_boards.tests.common_fixtures.populate_data import \
            populate_dict_with_valid_data

        data_dict = populate_dict_with_valid_data()
        populate_script = PopulateCreateBoardsAndColumns()

        # Act
        with pytest.raises(InvalidJsonFormat) as error:
            board_dtos, column_dtos = populate_script.populate_create_boards_and_columns(
                boards_columns_dicts=data_dict
            )

        # Assert

