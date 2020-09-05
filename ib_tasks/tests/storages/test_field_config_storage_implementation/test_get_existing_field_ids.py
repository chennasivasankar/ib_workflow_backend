import pytest

from ib_tasks.tests.factories.models import FieldFactory


@pytest.mark.django_db
class TestGetExistingFieldIds:

    def test_get_existing_field_ids_in_given_field_ids(
            self, storage
    ):
        # Arrange
        field_ids = ["field0", "field1", "field2"]
        FieldFactory.create(field_id="field0")
        FieldFactory.create(field_id="field1")
        expected_existing_field_ids = ["field0", "field1"]

        # Act
        actual_existing_field_ids = storage.get_existing_field_ids(field_ids)
        # Assert

        assert expected_existing_field_ids == actual_existing_field_ids
