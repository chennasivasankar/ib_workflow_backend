import pytest


@pytest.mark.django_db
class TestGetFieldsOfGoFs:

    def test_get_fields_of_gofs_in_dtos(self, storage):
        from ib_tasks.tests.factories.models import GoFFactory, FieldFactory
        from ib_tasks.interactors.storage_interfaces.fields_dtos \
            import FieldDTO
        from ib_tasks.constants.enum import FieldTypes
        expected_gof_ids = ['gof_1', 'gof_2']
        expected_field_dtos = [
            FieldDTO(
                gof_id='gof_1', field_id='FIELD_ID-1',
                field_display_name='DISPLAY_NAME-1',
                field_type=FieldTypes.PLAIN_TEXT.value,
                field_values=None, required=True, help_text=None, tooltip=None,
                placeholder_text=None, error_message=None,
                allowed_formats=None, validation_regex=None, order=1),
            FieldDTO(gof_id='gof_2', field_id='FIELD_ID-2',
                     field_display_name='DISPLAY_NAME-2',
                     field_type=FieldTypes.PLAIN_TEXT.value, field_values=None,
                     required=True, help_text=None, tooltip=None,
                     placeholder_text=None, error_message=None,
                     allowed_formats=None, validation_regex=None, order=2)
        ]

        import factory
        gof_objects = GoFFactory.create_batch(
            size=2, gof_id=factory.Iterator(expected_gof_ids)
        )
        FieldFactory.create_batch(size=2,
                                  gof=factory.Iterator(gof_objects))

        # Act
        result = storage.get_fields_of_gofs_in_dtos(gof_ids=expected_gof_ids)

        # Assert
        assert result == expected_field_dtos
