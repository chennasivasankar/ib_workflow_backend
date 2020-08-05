import factory
import pytest

from ib_tasks.tests.factories.models import FieldFactory
from ib_tasks.tests.factories.storage_dtos import \
    FieldCompleteDetailsDTOFactory


@pytest.mark.django_db
class TestFieldsStorageImplementation:

    @pytest.fixture
    def storage(self):
        from ib_tasks.storages.fields_storage_implementation import \
            FieldsStorageImplementation
        return FieldsStorageImplementation()

    def test_get_fields_of_gofs_in_dtos(self, storage):
        from ib_tasks.tests.factories.models import GoFFactory, FieldFactory
        from ib_tasks.interactors.storage_interfaces.fields_dtos \
            import FieldDTO
        from ib_tasks.constants.enum import FieldTypes
        expected_gof_ids = ['gof_1', 'gof_2']
        expected_field_dtos = [FieldDTO(gof_id='gof_1', field_id='FIELD_ID-0',
                                        field_display_name='DISPLAY_NAME-0',
                                        field_type=FieldTypes.PLAIN_TEXT.value,
                                        field_values=None, required=True,
                                        help_text=None, tooltip=None,
                                        placeholder_text=None,
                                        error_message=None,
                                        allowed_formats=None,
                                        validation_regex=None),
                               FieldDTO(gof_id='gof_2', field_id='FIELD_ID-1',
                                        field_display_name='DISPLAY_NAME-1',
                                        field_type=FieldTypes.PLAIN_TEXT.value,
                                        field_values=None, required=True,
                                        help_text=None, tooltip=None,
                                        placeholder_text=None,
                                        error_message=None,
                                        allowed_formats=None,
                                        validation_regex=None)]

        import factory
        gof_objs = GoFFactory.create_batch(
            size=2, gof_id=factory.Iterator(expected_gof_ids)
        )
        FieldFactory.create_batch(size=2,
                                  gof=factory.Iterator(gof_objs))

        # Act
        result = storage.get_fields_of_gofs_in_dtos(gof_ids=expected_gof_ids)

        # Assert
        assert result == expected_field_dtos

    def test_get_user_field_permission_dtos(self, storage):
        from ib_tasks.tests.factories.models import FieldFactory, \
            FieldRoleFactory
        from ib_tasks.interactors.storage_interfaces.fields_dtos \
            import UserFieldPermissionDTO
        from ib_tasks.constants.enum import PermissionTypes
        expected_field_ids = ['field_1', 'field_2']
        expected_user_field_permission_dtos = [
            UserFieldPermissionDTO(field_id='field_1',
                                   permission_type=PermissionTypes.READ.value)]

        import factory
        field_objs = FieldFactory.create_batch(size=2,
                                               field_id=factory.Iterator(
                                                   expected_field_ids))
        FieldRoleFactory.create_batch(size=2,
                                      field=factory.Iterator(field_objs))

        # Act
        result = storage.get_user_field_permission_dtos(
            field_ids=expected_field_ids, roles=['FIN_PAYMENT_REQUESTER'])

        # Assert
        assert result == expected_user_field_permission_dtos

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
            field_ids=field_ids_list
        )

        # Assert
        assert expected_field_type_dtos == actual_field_type_dtos

