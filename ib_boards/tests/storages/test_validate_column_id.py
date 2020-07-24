"""
Created on: 21/07/20
Author: Pavankumar Pamuru

"""
import pytest


@pytest.mark.django_db
class TestValidateColumnId:

    @pytest.fixture
    def storage(self):
        from ib_boards.storages.storage_implementation import \
            StorageImplementation
        return StorageImplementation()

    @pytest.fixture
    def reset_sequence(self):
        from ib_boards.tests.factories.models import BoardFactory, \
            ColumnFactory
        BoardFactory.reset_sequence()
        ColumnFactory.reset_sequence()
        from ib_boards.tests.factories.interactor_dtos import BoardDTOFactory
        BoardDTOFactory.reset_sequence()

    def test_with_invalid_column_id_raise_exception(
            self, storage, reset_sequence):
        # Arrange
        invalid_column_id = 'COLUMN_ID_100000'
        from ib_boards.tests.factories.models import BoardFactory, \
            ColumnFactory
        BoardFactory.create_batch(2)
        ColumnFactory.create_batch(3, board_id='BOARD_ID_1')

        # Act
        from ib_boards.exceptions.custom_exceptions import InvalidColumnId
        with pytest.raises(InvalidColumnId):
            storage.validate_column_id(
                column_id=invalid_column_id
            )

    def test_with_valid_column_id(
            self, storage, reset_sequence):
        # Arrange
        column_id = 'COLUMN_ID_1'
        from ib_boards.tests.factories.models import BoardFactory, \
            ColumnFactory
        BoardFactory.create_batch(2)
        ColumnFactory.create_batch(3, board_id='BOARD_ID_1')

        # Act
        storage.validate_column_id(column_id=column_id)
