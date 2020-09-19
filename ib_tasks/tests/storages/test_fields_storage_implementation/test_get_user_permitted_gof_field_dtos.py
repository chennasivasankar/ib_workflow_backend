import pytest


@pytest.mark.django_db
class TestGetUserPermissionGofFieldDTOS:


    def expected_response(self):
        from ib_tasks.tests.factories.storage_dtos import FieldNameDTOFactory
        FieldNameDTOFactory.reset_sequence(1)
        field_name_dtos = FieldNameDTOFactory.create_batch(1)
        return field_name_dtos

    def set_up_storage(self):
        from ib_tasks.tests.factories.models import (
            FieldFactory, FieldRoleFactory, GoFFactory
        )
        FieldRoleFactory.reset_sequence()
        GoFFactory.reset_sequence()
        FieldFactory.reset_sequence(1)
        fields = FieldFactory.create_batch(
            1, field_id="field_1", display_name="display_name_1"
        )
        FieldRoleFactory.create_batch(2, field=fields[0])

    def test_get_user_field_permission_dtos(self, storage):

        # Arrange
        self.set_up_storage()
        expected = self.expected_response()
        gof_ids = ["gof_1"]

        # Act
        result = storage.get_user_permitted_gof_field_dtos(
            gof_ids=gof_ids, user_roles=['FIN_PAYMENT_REQUESTER'])

        # Assert
        assert result == expected

    def test_get_user_empty_field_permission_dtos(self, storage):

        # Arrange
        self.set_up_storage()
        expected = []
        gof_ids = ["gof_1"]

        # Act
        result = storage.get_user_permitted_gof_field_dtos(
            gof_ids=gof_ids, user_roles=["role_1", "role_2"])

        # Assert
        assert result == expected
