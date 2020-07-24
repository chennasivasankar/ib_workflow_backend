"""
Created on: 18/07/20
Author: Pavankumar Pamuru

"""

import pytest

from ib_boards.interactors.dtos import BoardColumnsDTO
from ib_boards.models import Column
from ib_boards.storages.storage_implementation import StorageImplementation


@pytest.mark.django_db
class TestDeleteColumnsForBoard:

    @pytest.fixture
    def storage(self):
        return StorageImplementation()

    @pytest.fixture
    def reset_sequence(self):
        from ib_boards.tests.factories.models import BoardFactory, \
            ColumnFactory
        from ib_boards.tests.factories.interactor_dtos import BoardDTOFactory
        from ib_boards.tests.factories.interactor_dtos import ColumnDTOFactory
        BoardDTOFactory.reset_sequence()
        ColumnDTOFactory.reset_sequence()
        BoardFactory.reset_sequence()
        ColumnFactory.reset_sequence()

    def test_with_valid_data_delete_the_columns_for_board(self, storage):
        # Arrange
        from ib_boards.tests.factories.interactor_dtos import \
            BoardDTOFactory, ColumnDTOFactory
        board_dtos = BoardDTOFactory.create_batch(2)
        column_dtos = ColumnDTOFactory.create_batch(4, board_id='BOARD_ID_1')
        column_dtos += ColumnDTOFactory.create_batch(4, board_id='BOARD_ID_2')
        column_ids_for_first_board = ['COLUMN_ID_1', 'COLUMN_ID_2']
        column_ids_for_second_board = ['COLUMN_ID_7', 'COLUMN_ID_8']
        column_for_delete_dtos = [
            BoardColumnsDTO(
                board_id='BOARD_ID_1',
                column_ids=column_ids_for_first_board
            ),
            BoardColumnsDTO(
                board_id='BOARD_ID_2',
                column_ids=column_ids_for_second_board
            )
        ]

        # Act
        storage.delete_columns_which_are_not_in_configuration(
            column_for_delete_dtos=column_for_delete_dtos,
        )

        # Assert
        is_deleted = not Column.objects.filter(
            board_id__in=['BOARD_ID_1', 'BOARD_ID_2'],
            column_id__in=column_ids_for_first_board + column_ids_for_second_board
        )

        assert is_deleted is True
