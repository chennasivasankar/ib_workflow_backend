import pytest

from ib_boards.storages.storage_implementation import StorageImplementation
from ib_boards.tests.factories.models import BoardFactory, ColumnPermissionFactory, ColumnFactory


@pytest.mark.django_db
class TestGetBoardDetails:

    @pytest.fixture()
    def create_columns(self):
        BoardFactory.reset_sequence()
        BoardFactory.create_batch(size=10)

        board = BoardFactory()
        ColumnFactory.reset_sequence()
        ColumnPermissionFactory.reset_sequence()
        columns = ColumnFactory.create_batch(size=4, board=board)
        ColumnPermissionFactory.create_batch(size=2, column=columns[0])
        ColumnPermissionFactory.create_batch(size=2, column=columns[1])
        ColumnPermissionFactory.create_batch(size=2, column=columns[2])
        ColumnPermissionFactory.create_batch(size=2, column=columns[3])

    def test_get_board_details_given_board_id_and_stages(self, snapshot,
                                                         create_columns):
        # Arrange
        board_id = "BOARD_ID_11"
        stages = ["stage_id_1", "stage_id_2", "stage_id_3"]
        storage = StorageImplementation()

        # Act
        response = storage.get_board_complete_details(board_id, stages)

        # Assert
        snapshot.assert_match(response, "response")
