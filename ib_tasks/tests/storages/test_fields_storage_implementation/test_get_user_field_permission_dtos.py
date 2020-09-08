import pytest


@pytest.mark.django_db
class TestGetUserFieldPermissionDTOS:

    def test_get_user_field_permission_dtos(self, storage):
        from ib_tasks.tests.factories.models import FieldFactory, \
            FieldRoleFactory
        from ib_tasks.interactors.storage_interfaces.fields_dtos \
            import UserFieldPermissionDTO
        from ib_tasks.constants.enum import PermissionTypes
        expected_field_ids = ['field_1', 'field_2']
        expected_user_field_permission_dtos = [
            UserFieldPermissionDTO(
                field_id='field_1',
                permission_type=PermissionTypes.READ.value)]

        import factory
        field_objects = FieldFactory.create_batch(
            size=2, field_id=factory.Iterator(expected_field_ids))
        FieldRoleFactory.create_batch(
            size=2, field=factory.Iterator(field_objects))

        # Act
        result = storage.get_user_field_permission_dtos(
            field_ids=expected_field_ids, roles=['FIN_PAYMENT_REQUESTER'])

        # Assert
        assert result == expected_user_field_permission_dtos
