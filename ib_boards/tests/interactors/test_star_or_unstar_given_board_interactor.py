from unittest.mock import create_autospec

import pytest

from ib_boards.constants.enum import StartAction
from ib_boards.interactors.dtos import StarOrUnstarParametersDTO
from ib_boards.interactors.presenter_interfaces.presenter_interface import \
    PresenterInterface
from ib_boards.interactors.star_or_unstar_given_board_interactor import \
    StarOrUnstarBoardInteractor
from ib_boards.interactors.storage_interfaces.storage_interface import \
    StorageInterface


class TestStarOrUnstar:

    @pytest.fixture()
    def paramters(self):
        board_id = "board_id_1"
        action = StartAction.UNSTAR.value
        user_id = "user_id_1"
        paramters = StarOrUnstarParametersDTO(
            board_id=board_id,
            user_id=user_id,
            action=action
        )
        return paramters

    def test_given_invalid_board_id_raises_exception(self, paramters):
        # Arrange
        paramters = paramters
        board_id = paramters.board_id
        storage = create_autospec(StorageInterface)
        presenter = create_autospec(PresenterInterface)
        interactor = StarOrUnstarBoardInteractor(
            storage=storage
        )
        storage.validate_board_id.return_value = False

        # Act
        interactor.star_or_unstar_board_wrapper(
            presenter=presenter, parameters=paramters)

        # Assert
        storage.validate_board_id.assert_called_once_with(board_id)
        presenter.response_for_invalid_board_id.assert_called_once()

    def test_given_is_starred_star_creates_starred_board(self):
        # Arrange
        board_id = "board_id_1"
        action = StartAction.STAR.value
        user_id = "user_id_1"
        paramters = StarOrUnstarParametersDTO(
            board_id=board_id,
            user_id=user_id,
            action=action
        )
        storage = create_autospec(StorageInterface)
        presenter = create_autospec(PresenterInterface)
        interactor = StarOrUnstarBoardInteractor(
            storage=storage
        )
        storage.validate_board_id.return_value = True

        # Act
        interactor.star_or_unstar_board_wrapper(
            presenter=presenter, parameters=paramters)

        # Assert
        storage.validate_board_id.assert_called_once_with(board_id)
        storage.star_given_board.assert_called_once_with(paramters)

    def test_given_is_starred_true_deletes_starred_board(self, paramters):
        # Arrange
        paramters = paramters
        board_id = paramters.board_id
        storage = create_autospec(StorageInterface)
        presenter = create_autospec(PresenterInterface)
        interactor = StarOrUnstarBoardInteractor(
            storage=storage
        )
        storage.validate_board_id.return_value = True

        # Act
        interactor.star_or_unstar_board_wrapper(
            presenter=presenter, parameters=paramters)

        # Assert
        storage.validate_board_id.assert_called_once_with(board_id)
        storage.unstar_given_board.assert_called_once_with(paramters)
