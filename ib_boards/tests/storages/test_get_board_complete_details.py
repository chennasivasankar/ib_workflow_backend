import json

import pytest

from ib_boards.storages.storage_implementation import StorageImplementation
from ib_boards.tests.factories.models import BoardFactory, \
    ColumnPermissionFactory, ColumnFactory


@pytest.mark.django_db
class TestGetBoardDetails:

    @pytest.fixture()
    def create_columns(self):
        BoardFactory.reset_sequence()
        BoardFactory.create_batch(size=10)

        board = BoardFactory()
        ColumnFactory.reset_sequence()
        ColumnPermissionFactory.reset_sequence()
        column_1 = ColumnFactory(board=board,
                                 task_selection_config=json.dumps(
                                     {
                                         "FIN_PR": ["stage_id_1"]
                                     }
                                 ))
        column_2 = ColumnFactory(board=board,
                                 task_selection_config=json.dumps(
                                     {
                                         "FIN_PR": ["stage_id_2"]
                                     }
                                 ))
        column_3 = ColumnFactory(board=board,
                                 task_selection_config=json.dumps(
                                     {
                                         "FIN_PR": ["stage_id_3"]
                                     }
                                 ))
        column_4 = ColumnFactory(board=board,
                                 task_selection_config=json.dumps(
                                     {
                                         "FIN_PR": ["stage_id_1", "stage_id_2"]
                                     }
                                 ))
        ColumnPermissionFactory.create_batch(size=2, column=column_1)
        ColumnPermissionFactory.create_batch(size=2, column=column_2)
        ColumnPermissionFactory.create_batch(size=2, column=column_3)
        ColumnPermissionFactory.create_batch(size=2, column=column_4)

    def test_get_board_details_given_board_id_and_stages(self, snapshot,
                                                         create_columns):
        # Arrange
        board_id = "BOARD_ID_11"
        stages = ["stage_id_1", "stage_id_2"]
        storage = StorageImplementation()

        # Act
        response = storage.get_board_complete_details(board_id, stages)

        # Assert
        snapshot.assert_match(response, "response")
