"""
Created on: 20/07/20
Author: Pavankumar Pamuru

"""
import pytest

from ib_boards.storages.storage_implementation import StorageImplementation


@pytest.mark.django_db
class TestColumnIdsWithBoardIds:

    @pytest.fixture
    def storage(self):
        return StorageImplementation()

    @pytest.fixture
    def reset_sequence(self):
        from ib_boards.tests.factories.models import BoardFactory, ColumnFactory
        from ib_boards.tests.factories.interactor_dtos import BoardDTOFactory
        from ib_boards.tests.factories.interactor_dtos import ColumnDTOFactory
        BoardDTOFactory.reset_sequence()
        ColumnDTOFactory.reset_sequence()
        BoardFactory.reset_sequence()
        ColumnFactory.reset_sequence()

    def test_with_valid_column_ids_return_boards_ids_with_columns_ids(
            self, storage, reset_sequence):
        # Arrange
        first_board_column_ids = [
            'COLUMN_ID_1', 'COLUMN_ID_2',
        ]
        second_board_column_ids = [
            'COLUMN_ID_3', 'COLUMN_ID_4'
        ]
        board_ids = ['BOARD_ID_1', 'BOARD_ID_2']
        from ib_boards.tests.factories.models import BoardFactory
        boards = BoardFactory.create_batch(2)
        from ib_boards.tests.factories.models import ColumnFactory
        columns = ColumnFactory.create_batch(
            2, board=boards[0]
        )
        columns_2 = ColumnFactory.create_batch(
            2, board=boards[1]
        )
        columns += columns_2

        # Arrange
        boards_columns_dtos = storage.get_boards_column_ids(
            board_ids=board_ids
        )

        # Assert
        assert boards_columns_dtos[0].board_id == board_ids[0]
        assert boards_columns_dtos[1].board_id == board_ids[1]
        assert boards_columns_dtos[0].column_ids == first_board_column_ids
        assert boards_columns_dtos[1].column_ids == second_board_column_ids






