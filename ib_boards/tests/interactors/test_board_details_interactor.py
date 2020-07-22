from unittest.mock import create_autospec

import pytest

from ib_boards.exceptions.custom_exceptions import InvalidBoardId, InvalidStageIds
from ib_boards.interactors.get_board_complete_details_interactor import GetBoardDetailsInteractor
from ib_boards.interactors.storage_interfaces.storage_interface import StorageInterface


class TestBoardDetailsInteractor:

    @pytest.fixture()
    def storage(self):
        storage = create_autospec(StorageInterface)
        return storage

    def test_validate_board_id_given_invalid_raises_exception(self, storage):
        # Arrange
        user_id = "user_id_1"
        board_id = "board_id"
        stages = ["stage_id_1", "stage_id_2", "stage_id_3"]

        interactor = GetBoardDetailsInteractor(storage=storage)

        storage.validate_board_id.return_value = False

        # Act
        with pytest.raises(InvalidBoardId):
            interactor.get_board_details(board_id=board_id, stage_ids=stages,
                                         user_id=user_id)

        # Assert
        storage.validate_board_id.assert_called_once_with(board_id)

    def test_get_columns_details_given_valid_board_id(self, storage):
        # Arrange
        interactor = GetBoardDetailsInteractor(storage=storage)
        # Act
        # Assert
