import pytest

from ib_boards.interfaces.service_interface import BoardServiceInterface
from ib_boards.tests.common_fixtures.adapters.iam_service import adapter_mock_to_get_user_role
from ib_boards.tests.factories.models import ColumnPermissionFactory, \
    ColumnFactory, BoardFactory


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

    def test_get_board_details(self, mocker, snapshot, create_columns):
        # Arrange
        board_id = "BOARD_ID_1"
        stages = ["stage_id_1", "stage_id_2", "stage_id_3"]
        user_id = 1
        roles = ["FIN_PAYMENT_REQUESTER", "FIN_PAYMENT_POC", "FIN_PAYMENT_APPROVER",
                 "FIN_PAYMENTS_LEVEL1_VERIFIER", "FIN_PAYMENTS_LEVEL2_VERIFIER", "FIN_PAYMENTS_LEVEL3_VERIFIER"]
        user_roles = adapter_mock_to_get_user_role(mocker, "361362f1-a5e3-4822-a6ba-30019252e40d")
        user_roles.return_value = roles
        service = BoardServiceInterface()

        # Act
        result = service.get_board_details(board_id, stages, user_id)

        # Assert
        snapshot.assert_match(result, "result")
