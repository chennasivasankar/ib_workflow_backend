"""
Created on: 21/07/20
Author: Pavankumar Pamuru

"""
import pytest


@pytest.mark.django_db
class TestGetValidBoardIds:

    @pytest.fixture
    def storage(self):
        from ib_boards.storages.storage_implementation import \
            StorageImplementation
        return StorageImplementation()

    @pytest.fixture
    def reset_sequence(self):
        from ib_boards.tests.factories.models import BoardFactory
        BoardFactory.reset_sequence()
        from ib_boards.tests.factories.interactor_dtos import BoardDTOFactory
        BoardDTOFactory.reset_sequence()

    def test_with_one_invalid_board_ids_return_valid_board_ids(
            self, storage, reset_sequence):
        # Arrange
        user_role = 'User'
        board_ids = ['BOARD_ID_1', 'BOARD_ID_2', 'BOARD_ID_3']
        expected_valid_board_ids = ['BOARD_ID_1', 'BOARD_ID_2']
        from ib_boards.tests.factories.models import BoardFactory
        BoardFactory.create_batch(2)
        from ib_boards.tests.factories.interactor_dtos import BoardDTOFactory
        BoardDTOFactory.create_batch(3)

        # Act
        actual_board_ids = storage.get_valid_board_ids(
            board_ids=board_ids
        )

        # Assert
        assert actual_board_ids == expected_valid_board_ids


