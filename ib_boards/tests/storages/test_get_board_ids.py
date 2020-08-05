"""
Created on: 21/07/20
Author: Pavankumar Pamuru

"""
import pytest

from ib_boards.tests.factories.models import UserStarredBoardFactory


@pytest.mark.django_db
class TestGetBoardIds:

    @pytest.fixture
    def storage(self):
        from ib_boards.storages.storage_implementation import \
            StorageImplementation
        return StorageImplementation()

    @pytest.fixture
    def reset_sequence(self):
        from ib_boards.tests.factories.models import BoardFactory
        from ib_boards.tests.factories.models import UserStarredBoardFactory
        BoardFactory.reset_sequence()
        UserStarredBoardFactory.reset_sequence()

    def test_with_valid_user_role_return_board_ids(
            self, storage, reset_sequence):
        # Arrange
        user_id = 'user_id_1'
        expected_board_ids = ['BOARD_ID_3', 'BOARD_ID_4', 'BOARD_ID_5']
        expected_starred_board_ids = ['BOARD_ID_1', 'BOARD_ID_2']
        from ib_boards.tests.factories.models import BoardFactory
        boards = BoardFactory.create_batch(5)
        UserStarredBoardFactory(board=boards[0], user_id="user_id_1")
        UserStarredBoardFactory(board=boards[1], user_id="user_id_1")

        # Act
        other_board_ids, starred_board_ids = storage.get_board_ids(user_id=user_id)

        # Assert
        assert other_board_ids == expected_board_ids
        assert starred_board_ids == expected_starred_board_ids
