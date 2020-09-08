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

    def test_fields_display_order_and_status_creates(self, storage):
        # Arrange
        import json
        column_id = 'COLUMN_ID_1'
        user_id = 'user_id_0'
        field_ids = [
            "field_id_0", "field_id_1", "field_id_2"
        ]
        FieldDisplayStatusFactory.create_batch(3)
        FieldOrderFactory()

        # Act
        present_field_ids = storage.get_field_ids_list_in_order(
            column_id=column_id,
            user_id=user_id,
        )

        # Assert
        assert present_field_ids == field_ids
