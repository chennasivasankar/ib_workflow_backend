import pytest

from ib_boards.storages.storage_implementation import StorageImplementation
from ib_boards.tests.factories.models import (
    BoardFactory, ColumnFactory, ColumnPermissionFactory)


@pytest.mark.django_db
class TestGetColumnStageIds:

    @pytest.fixture()
    def create_columns(self):
        BoardFactory.reset_sequence()
        board = BoardFactory()
        ColumnFactory.reset_sequence()
        ColumnFactory(board=board, display_order=4)
        ColumnFactory(board=board, display_order=1)
        ColumnFactory(board=board, display_order=2)
        ColumnFactory(board=board, display_order=3)

    def test_get_column_stages_in_display_order(self, snapshot,
                                                create_columns):
        # Arrange
        column_ids = ["COLUMN_ID_1", "COLUMN_ID_2", "COLUMN_ID_3",
                      "COLUMN_ID_4"]
        storage = StorageImplementation()

        # Act
        response = storage.get_columns_stage_ids(column_ids)

        # Assert
        snapshot.assert_match(response, "response")
