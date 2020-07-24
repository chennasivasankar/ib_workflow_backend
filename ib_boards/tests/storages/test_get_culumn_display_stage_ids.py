"""
Created on: 22/07/20
Author: Pavankumar Pamuru

"""
import pytest


@pytest.mark.django_db
class TestGetColumnDisplayStageIds:

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

    def test_with_valid_column_id_return_column_stage_ids(
            self, storage, reset_sequence):
        # Arrange
        expected_stage_ids = ['PR_PAYMENT_REQUEST_DRAFTS']
        column_id = 'COLUMN_ID_1'
        from ib_boards.tests.factories.models import BoardFactory
        BoardFactory.create_batch(2)
        from ib_boards.tests.factories.models import ColumnFactory
        ColumnFactory.create_batch(2, board_id='BOARD_ID_1')

        # Act
        actual_stage_ids = storage.get_column_display_stage_ids(
            column_id=column_id
        )

        # Assert
        assert actual_stage_ids == expected_stage_ids
