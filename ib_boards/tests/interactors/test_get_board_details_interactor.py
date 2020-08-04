"""
Created on: 16/07/20
Author: Pavankumar Pamuru

"""
from unittest.mock import Mock

import pytest

from ib_boards.interactors.get_board_details_interactor import \
    GetBoardsDetailsInteractor
from ib_boards.tests.factories.storage_dtos import BoardDTOFactory


class TestGetBoardDetailsInteractor:

    @pytest.fixture
    def storage_mock(self):
        from ib_boards.interactors.storage_interfaces.storage_interface import \
            StorageInterface
        from unittest import mock
        storage = mock.create_autospec(StorageInterface)
        return storage

    def test_with_valid_details_return_board_details(
            self, storage_mock):
        # Arrange
        board_ids = ['BOARD_ID_1', 'BOARD_ID_2', 'BOARD_ID_3']
        board_dtos = BoardDTOFactory.create_batch(3)
        BoardDTOFactory.reset_sequence()

        interactor = GetBoardsDetailsInteractor(
            storage=storage_mock
        )
        expected_response = board_dtos
        storage_mock.get_valid_board_ids.return_value = board_ids
        storage_mock.get_board_details.return_value = board_dtos

        # Act
        actual_response = interactor.get_boards_details(
            board_ids=board_ids,
        )

        # Assert
        storage_mock.get_valid_board_ids.assert_called_once_with(
            board_ids=board_ids
        )
        storage_mock.get_board_details.assert_called_once_with(
            board_ids=board_ids
        )
        assert actual_response == expected_response

    def test_with_duplicate_board_details_return_board_details(
            self, storage_mock):
        # Arrange
        duplicate_board_ids = [
            'BOARD_ID_1', 'BOARD_ID_1', 'BOARD_ID_2', 'BOARD_ID_3'
        ]
        board_ids = ['BOARD_ID_1', 'BOARD_ID_2', 'BOARD_ID_3']
        board_dtos = BoardDTOFactory.create_batch(3)
        BoardDTOFactory.reset_sequence()

        interactor = GetBoardsDetailsInteractor(
            storage=storage_mock
        )
        expected_response = board_dtos
        storage_mock.get_valid_board_ids.return_value = board_ids
        storage_mock.get_board_details.return_value = board_dtos

        # Act
        actual_response = interactor.get_boards_details(
            board_ids=duplicate_board_ids,
        )

        # Assert
        storage_mock.get_valid_board_ids.assert_called_once_with(
            board_ids=board_ids
        )
        storage_mock.get_board_details.assert_called_once_with(
            board_ids=board_ids
        )
        assert actual_response == expected_response

    def test_with_invalid_details_return_error_message(
            self, storage_mock):
        # Arrange
        board_ids = ['BOARD_ID_1', 'BOARD_ID_2', 'BOARD_ID_3']
        valid_board_ids = ['BOARD_ID_1', 'BOARD_ID_2']
        invalid_board_ids = ['BOARD_ID_3']
        board_dtos = BoardDTOFactory.create_batch(3)
        BoardDTOFactory.reset_sequence()

        interactor = GetBoardsDetailsInteractor(
            storage=storage_mock
        )
        storage_mock.get_valid_board_ids.return_value = valid_board_ids

        # Act
        from ib_boards.exceptions.custom_exceptions import InvalidBoardIds
        with pytest.raises(InvalidBoardIds) as error:
            interactor.get_boards_details(
                board_ids=board_ids
            )

        # Assert
        storage_mock.get_valid_board_ids.assert_called_once_with(
            board_ids=board_ids
        )
        assert error.value.board_ids == invalid_board_ids
