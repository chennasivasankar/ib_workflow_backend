"""
Created on: 20/07/20
Author: Pavankumar Pamuru

"""
import pytest

from ib_boards.storages.storage_implementation import StorageImplementation


class TestColumnIdsWithBoardIds:

    @pytest.fixture
    def storage(self):
        return StorageImplementation()

    def test_with_valid_column_ids_return_board_ids_with_column_ids(self):
        # Arrange
        column_ids = [
            'COLUMN_ID_1', 'COLUMN_ID_2',
            'COLUMN_ID_3', 'COLUMN_ID_4'
        ]
        pass
