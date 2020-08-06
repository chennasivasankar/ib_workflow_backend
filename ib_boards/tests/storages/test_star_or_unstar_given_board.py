import pytest

from ib_boards.tests.factories.models import BoardFactory


class TestStarOrUnstarGivenBoard:


    @pytest.fixture()
    def populate_data(self):
        BoardFactory.reset_sequence()
        board = BoardFactory()


    def test_given_is_starred_true_and_board_is_not_starred_for_user(self):
        # Arrange
        # Act
        # Assert
