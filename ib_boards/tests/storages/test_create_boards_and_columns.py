"""
Created on: 18/07/20
Author: Pavankumar Pamuru

"""
import pytest

from ib_boards.storages.storage_implementation import StorageImplementation


@pytest.mark.django_db
class TestCreateBoardsAndColumns:

    @pytest.fixture
    def storage(self):
        return StorageImplementation()

    def test_with_valid_data_crates_data(self, storage):
        # Arrange
        from ib_boards.tests.factories.interactor_dtos import \
            CreateBoardDTOFactory, ColumnDTOFactory
        board_dtos = CreateBoardDTOFactory.create_batch(1)
        column_dtos = ColumnDTOFactory.create_batch(board_id='BOARD_ID_1')

        # Act
        storage.create_boards_and_columns(
            board_dtos=board_dtos,
            column_dtos=column_dtos
        )

        # Assert
