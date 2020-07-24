import pytest

from ib_boards.interfaces.service_interface import BoardServiceInterface
from ib_boards.tests.factories.models import ColumnPermissionFactory, ColumnFactory, BoardFactory


@pytest.mark.django_db
class TestServiceInterface:

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

    def test_get_board_details(self, snapshot, create_columns):
        # Arrange
        board_id = "BOARD_ID_1"
        stages = ["stage_id_1", "stage_id_2", "stage_id_3"]
        user_id = 1
        service = BoardServiceInterface()

        # Act
        result = service.get_board_details(board_id, stages, user_id)

        # Assert
        snapshot.assert_match(result, "result")
