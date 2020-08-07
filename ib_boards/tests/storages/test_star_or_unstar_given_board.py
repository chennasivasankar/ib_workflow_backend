import pytest

from ib_boards.constants.enum import StartAction
from ib_boards.interactors.dtos import StarOrUnstarParametersDTO
from ib_boards.models import UserStarredBoard
from ib_boards.storages.storage_implementation import StorageImplementation
from ib_boards.tests.factories.models import UserStarredBoardFactory, BoardFactory


@pytest.mark.django_db
class TestStarOrUnstarGivenBoard:

    @pytest.fixture()
    def populate_data(self):
        BoardFactory.reset_sequence()
        UserStarredBoardFactory.reset_sequence()
        UserStarredBoardFactory.create_batch(size=2)

    @pytest.fixture()
    def is_starred_true_parameters(self):
        board_id = "BOARD_ID_1"
        action = StartAction.UNSTAR.value
        user_id = "user_id_0"
        paramters = StarOrUnstarParametersDTO(
            board_id=board_id,
            user_id=user_id,
            action=action
        )
        return paramters

    @pytest.fixture()
    def is_starred_false_parameters(self):
        board_id = "BOARD_ID_1"
        action = StartAction.STAR.value
        user_id = "user_id_0"
        paramters = StarOrUnstarParametersDTO(
            board_id=board_id,
            user_id=user_id,
            action=action
        )
        return paramters

    def test_given_is_starred_true_and_board_is_starred_for_user_unstars_board(
            self, populate_data, is_starred_true_parameters):
        # Arrange
        parameters = is_starred_true_parameters
        user_id = parameters.user_id
        board_id = parameters.board_id
        expected_output = False
        storage = StorageImplementation()

        # Act
        storage.unstar_given_board(parameters)

        # Assert
        starred_board = UserStarredBoard.objects.filter(
            board_id=board_id, user_id=user_id).exists()
        assert starred_board == expected_output

    def test_given_is_starred_true_and_board_is_not_starred_for_user_does_nothing(
            self, populate_data, is_starred_true_parameters):
        # Arrange
        paramters = is_starred_true_parameters
        user_id = paramters.user_id
        board_id = paramters.board_id
        expected_output = False
        storage = StorageImplementation()

        # Act
        storage.unstar_given_board(paramters)

        # Assert
        starred_board = UserStarredBoard.objects.filter(
            board_id=board_id, user_id=user_id).exists()
        assert starred_board == expected_output

    def test_given_is_starred_false_and_board_is_not_starred_for_user_creates_starred_board(
            self, is_starred_false_parameters):
        # Arrange
        BoardFactory.reset_sequence()
        BoardFactory()
        parameters = is_starred_false_parameters
        user_id = parameters.user_id
        board_id = parameters.board_id
        expected_output = True
        storage = StorageImplementation()

        # Act
        storage.star_given_board(parameters)

        # Assert
        starred_board = UserStarredBoard.objects.filter(
            board_id=board_id, user_id=user_id).exists()
        assert starred_board == expected_output

    def test_given_is_starred_false_and_board_is_starred_for_user(
            self, populate_data, is_starred_false_parameters):
        # Arrange
        parameters = is_starred_false_parameters
        user_id = parameters.user_id
        board_id = parameters.board_id
        expected_output = True
        storage = StorageImplementation()

        # Act
        storage.star_given_board(parameters)

        # Assert
        starred_board = UserStarredBoard.objects.filter(
            board_id=board_id, user_id=user_id).exists()
        assert starred_board == expected_output
