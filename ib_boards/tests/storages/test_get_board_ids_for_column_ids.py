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
        BoardDTOFactory.reset_sequence()
        from ib_boards.tests.factories.interactor_dtos import ColumnDTOFactory
        ColumnDTOFactory.reset_sequence()
        BoardFactory.reset_sequence()
        ColumnFactory.reset_sequence()

    def test_with_valid_column_ids_return_board_ids_with_column_ids(
            self, storage, reset_sequence):
        # Arrange
        column_ids = [
            'COLUMN_ID_1', 'COLUMN_ID_2', 'COLUMN_ID_3', 'COLUMN_ID_4'
        ]
        board_ids = ['BOARD_ID_1', 'BOARD_ID_1', 'BOARD_ID_2', 'BOARD_ID_2']
        from ib_boards.tests.factories.models import BoardFactory
        boards = BoardFactory.create_batch(2)
        from ib_boards.tests.factories.models import ColumnFactory
        columns = ColumnFactory.create_batch(
            2, board=boards[0]
        )
        columns += ColumnFactory.create_batch(
            2, board=boards[1]
        )

        # Arrange
        board_column_dtos = storage.get_board_ids_for_column_ids(
            column_ids=column_ids
        )

        # Assert
        for board, column, board_column_dto in zip(
                board_ids, column_ids, board_column_dtos):
            assert board_column_dto.board_id == board
            assert board_column_dto.column_id == column






