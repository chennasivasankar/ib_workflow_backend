import pytest

from ib_boards.storages.storage_implementation import StorageImplementation
from ib_boards.tests.factories.models import ColumnFactory, \
    ColumnPermissionFactory, BoardFactory


@pytest.mark.django_db
class TestGetColumnIdsForBoard:

    @pytest.fixture()
    def create_columns(self):
        BoardFactory.reset_sequence()
        board = BoardFactory()
        ColumnFactory.reset_sequence()
        ColumnPermissionFactory.reset_sequence()
        columns = ColumnFactory.create_batch(size=4, board=board)
        ColumnPermissionFactory.create_batch(size=2, column=columns[0])
        ColumnPermissionFactory.create_batch(size=2, column=columns[1])
        ColumnPermissionFactory.create_batch(size=2, column=columns[2])
        ColumnPermissionFactory.create_batch(size=2, column=columns[3])

    def test_get_column_ids_for_board(self, create_columns):
        # Arrange
        board_id = "BOARD_ID_1"
        user_roles = ["Super User", "PR APPROVER"]
        expected_column_ids = ["COLUMN_ID_1", "COLUMN_ID_2", "COLUMN_ID_3",
                               "COLUMN_ID_4"]
        storage = StorageImplementation()

        # Act
        column_ids = storage.get_column_ids_for_board(board_id, user_roles)

        # Assert
        assert column_ids == expected_column_ids
