"""
Created on: 07/09/20
Author: Pavankumar Pamuru

"""
import pytest


@pytest.mark.django_db
class TestCreateFieldOrderAndStatus:

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
            'field_id_0', 'field_id_1', 'field_id_2'
        ]


        # Act
        storage.create_field_ids_order_and_display_status(
            column_id=column_id,
            user_id=user_id,
            field_ids=field_ids
        )

        # Assert
        from ib_boards.models import FieldDisplayStatus
        display_objects = FieldDisplayStatus.objects.filter(
            column_id=column_id,
            user_id=user_id
        )

        from ib_boards.models import FieldOrder
        order_object = FieldOrder.objects.get(
            user_id=user_id,
            column_id=column_id
        )

        snapshot.assert_match(order_object.fields_order, 'field_ids')
        snapshot.assert_match(display_objects, 'display_objects')
