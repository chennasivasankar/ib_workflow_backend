"""
Created on: 21/07/20
Author: Pavankumar Pamuru

"""
import pytest


@pytest.mark.django_db
class TestGetBoardDetails:

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

    def test_with_valid_user_role_return_board_ids(
            self, storage, reset_sequence):
        # Arrange
        user_role = 'User'
        board_ids = ['BOARD_ID_1', 'BOARD_ID_2', 'BOARD_ID_3']
        from ib_boards.tests.factories.models import BoardFactory
        BoardFactory.create_batch(3)
        from ib_boards.tests.factories.interactor_dtos import BoardDTOFactory
        expected_board_dtos = BoardDTOFactory.create_batch(3)

        # Act
        actual_board_dtos = storage.get_board_details(
            board_ids=board_ids
        )

        # Assert
        assert actual_board_dtos[0] == expected_board_dtos[0]
        assert actual_board_dtos[1] == expected_board_dtos[1]
        assert actual_board_dtos[2] == expected_board_dtos[2]