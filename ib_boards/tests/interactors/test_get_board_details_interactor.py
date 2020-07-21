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

    @pytest.fixture
    def presenter_mock(self):
        from unittest import mock
        from ib_boards.interactors.presenter_interfaces.presenter_interface import \
            GetBoardsDetailsPresenterInterface
        presenter = mock.create_autospec(GetBoardsDetailsPresenterInterface)
        return presenter

    def test_with_valid_details_return_board_details(
            self, storage_mock, presenter_mock, mocker):
        # Arrange
        board_ids = ['BOARD_ID_1', 'BOARD_ID_2', 'BOARD_ID_3']
        board_dtos = BoardDTOFactory.create_batch(3)
        BoardDTOFactory.reset_sequence()

        interactor = GetBoardsDetailsInteractor(
            storage=storage_mock
        )
        expected_response = Mock()
        storage_mock.get_valid_board_ids.return_value = board_ids
        storage_mock.get_board_details.return_value = board_dtos
        presenter_mock.get_response_for_board_details. \
            return_value = expected_response
        # Act
        actual_response = interactor.get_boards_details_wrapper(
            board_ids=board_ids,
            presenter=presenter_mock
        )

        # Assert
        storage_mock.get_valid_board_ids.assert_called_once_with(
            board_ids=board_ids
        )
        storage_mock.get_board_details.assert_called_once_with(
            board_ids=board_ids
        )
        presenter_mock.get_response_for_board_details.assert_called_once_with(
            board_dtos=board_dtos
        )
        assert actual_response == expected_response

    def test_with_invalid_details_return_error_message(
            self, storage_mock, presenter_mock, mocker):
        # Arrange
        board_ids = ['BOARD_ID_1', 'BOARD_ID_2', 'BOARD_ID_3']
        valid_board_ids = ['BOARD_ID_1', 'BOARD_ID_2']
        invalid_board_ids = ['BOARD_ID_3']
        board_dtos = BoardDTOFactory.create_batch(3)
        BoardDTOFactory.reset_sequence()

        interactor = GetBoardsDetailsInteractor(
            storage=storage_mock
        )
        expected_response = Mock()
        storage_mock.get_valid_board_ids.return_value = valid_board_ids
        storage_mock.get_board_details.return_value = board_dtos
        presenter_mock.get_response_for_invalid_board_ids. \
            return_value = expected_response
        # Act
        actual_response = interactor.get_boards_details_wrapper(
            board_ids=board_ids,
            presenter=presenter_mock
        )

        # Assert
        storage_mock.get_valid_board_ids.assert_called_once_with(
            board_ids=board_ids
        )
        call_args = presenter_mock.get_response_for_invalid_board_ids.call_args
        assert call_args.kwargs['error'].board_ids == invalid_board_ids
        assert actual_response == expected_response
