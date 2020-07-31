import pytest

from ib_boards.storages.storage_implementation import StorageImplementation
from ib_boards.tests.factories.models import BoardFactory


@pytest.mark.django_db
class TestValidateBoardId:

    @pytest.fixture()
    def create_boards(self):
        BoardFactory.reset_sequence()
        BoardFactory.create_batch(size=2)

    def test_validate_board_id_given_invalid_board_id(self):
        # Arrange
        board_id = "board_id_1"
        storage = StorageImplementation()
        expected = False

        # Act
        is_valid = storage.validate_board_id(board_id)

        # Assert
        assert is_valid == expected

    def test_validate_board_id_given_valid_board_id(self,
                                                    create_boards):
        # Arrange
        board_id = "BOARD_ID_1"
        storage = StorageImplementation()
        expected = True

        # Act
        is_valid = storage.validate_board_id(board_id)

        # Assert
        assert is_valid == expected
