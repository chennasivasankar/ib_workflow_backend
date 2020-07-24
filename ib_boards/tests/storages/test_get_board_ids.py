"""
Created on: 21/07/20
Author: Pavankumar Pamuru

"""
import pytest


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
        BoardFactory.reset_sequence()

    def test_with_valid_user_role_return_board_ids(
            self, storage, reset_sequence):
        # Arrange
        user_role = 'User'
        expected_board_ids = ['BOARD_ID_1', 'BOARD_ID_2', 'BOARD_ID_3']
        from ib_boards.tests.factories.models import BoardFactory
        BoardFactory.create_batch(3)

        # Act
        actual_board_ids = storage.get_board_ids(
            user_role=user_role
        )

        # Assert
        assert expected_board_ids == actual_board_ids


