import pytest

from ib_tasks.tests.factories.models import FieldFactory


@pytest.mark.django_db
class TestGetFieldIdsForGivenGoFs:

    def test_get_field_ids_for_given_gofs_when_exists_return_field_ids(
            self, storage):
        # Arrange
        fields = FieldFactory.create_batch(size=2)
        expected_field_ids = [field.field_id for field in fields]
        gof_ids = [field.gof_id for field in fields]

        # Act
        field_ids = storage.get_field_ids_for_given_gofs(gof_ids=gof_ids)

        # Assert
        assert field_ids == expected_field_ids

    def test_get_field_ids_for_given_gofs_when_not_exists_return_empty_list(
            self, storage):
        # Arrange
        expected_field_ids = []
        gof_ids = ["gof_1"]

        # Act
        field_ids = storage.get_field_ids_for_given_gofs(gof_ids=gof_ids)

        # Assert
        assert field_ids == expected_field_ids
