import factory
import pytest

from ib_tasks.tests.factories.models import FieldFactory
from ib_tasks.tests.factories.storage_dtos import \
    FieldCompleteDetailsDTOFactory


@pytest.mark.django_db
class TestGetFieldDetails:

    def test_get_field_details_for_given_field_ids(self, storage):
        # Arrange
        field_objects = FieldFactory.create_batch(size=2)
        field_ids_list = [field_object.field_id for field_object in
                          field_objects]
        field_types_list = [
            field_object.field_type for field_object in field_objects
        ]
        field_required_list = [
            field_object.required for field_object in field_objects
        ]
        field_values_list = [
            field_object.field_values for field_object in field_objects
        ]
        allowed_formats_list = [
            field_object.allowed_formats for field_object in field_objects
        ]
        validation_regex_list = [
            field_object.validation_regex for field_object in field_objects
        ]
        expected_field_type_dtos = FieldCompleteDetailsDTOFactory.create_batch(
            size=2, field_id=factory.Iterator(field_ids_list),
            field_type=factory.Iterator(field_types_list),
            required=factory.Iterator(field_required_list),
            field_values=factory.Iterator(field_values_list),
            allowed_formats=factory.Iterator(allowed_formats_list),
            validation_regex=factory.Iterator(validation_regex_list)
        )

        # Act
        actual_field_type_dtos = storage.get_field_details_for_given_field_ids(
            field_ids=field_ids_list)

        # Assert
        assert expected_field_type_dtos == actual_field_type_dtos
