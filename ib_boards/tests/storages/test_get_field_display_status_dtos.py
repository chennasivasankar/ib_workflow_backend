"""
Created on: 07/09/20
Author: Pavankumar Pamuru

"""
import pytest

from ib_boards.tests.factories.models import FieldDisplayStatusFactory, \
    FieldOrderFactory


@pytest.mark.django_db
class TestCreateFieldOrderAndStatus:

    @classmethod
    def setup(cls):
        FieldDisplayStatusFactory.reset_sequence()
        FieldOrderFactory.reset_sequence()

    @classmethod
    def teardown(cls):
        pass

    @pytest.fixture
    def storage(self):
        from ib_boards.storages.storage_implementation import \
            StorageImplementation
        return StorageImplementation()

    def test_fields_display_order_and_status_creates(self, storage, snapshot):
        # Arrange
        import json
        column_id = 'COLUMN_ID_1'
        user_id = 'user_id_0'
        field_ids = [
            'field_id_0'
        ]
        FieldDisplayStatusFactory.create_batch(3)
        FieldOrderFactory()

        # Act
        display_status_dtos = storage.get_field_display_status_dtos(
            column_id=column_id,
            user_id=user_id,
        )

        # Assert
        snapshot.assert_match(display_status_dtos, 'display_status_dtos')
