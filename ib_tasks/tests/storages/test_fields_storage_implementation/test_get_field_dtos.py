import pytest

from ib_tasks.tests.factories.models import FieldFactory


@pytest.mark.django_db
class TestGetFieldDTOS:

    def test_get_field_dtos_when_exists_returns_field_dtos(self, storage):
        # Arrange
        from ib_tasks.interactors.storage_interfaces.fields_dtos import \
            FieldDTO
        from ib_tasks.constants.enum import FieldTypes
        fields = FieldFactory.create_batch(size=2)
        field_ids = [field.field_id for field in fields]
        expected_field_dtos = [
            FieldDTO(
                gof_id='gof_1', field_id='FIELD_ID-1',
                field_display_name='DISPLAY_NAME-1',
                field_type=FieldTypes.PLAIN_TEXT.value,
                field_values=None, required=True,
                help_text=None, tooltip=None, placeholder_text=None,
                error_message=None, allowed_formats=None,
                validation_regex=None, order=1
            ),
            FieldDTO(
                gof_id='gof_2', field_id='FIELD_ID-2',
                field_display_name='DISPLAY_NAME-2',
                field_type=FieldTypes.PLAIN_TEXT.value,
                field_values=None, required=True, help_text=None, tooltip=None,
                placeholder_text=None, error_message=None,
                allowed_formats=None, validation_regex=None, order=2
            )]

        # Act
        field_dtos = storage.get_field_dtos(field_ids=field_ids)

        # Assert
        assert field_dtos == expected_field_dtos

    def test_get_field_dtos_when_not_exists_returns_empty_list(self, storage):
        # Arrange
        field_ids = ["field_1"]
        expected_field_dtos = []

        # Act
        field_dtos = storage.get_field_dtos(field_ids=field_ids)

        # Assert
        assert field_dtos == expected_field_dtos
