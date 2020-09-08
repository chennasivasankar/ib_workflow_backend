import pytest

from ib_tasks.tests.factories.models import FieldRoleFactory


@pytest.mark.django_db
class TestValidateUserRolesWithFieldRoles:

    def test_validate_user_roles_with_field_ids_roles_return_error_message(
            self, storage):
        # Arrange
        fields = FieldRoleFactory.create_batch(3)
        field_ids = [field.field_id for field in fields]
        user_roles = ['User', 'Admin']

        # Act
        from ib_tasks.exceptions.filter_exceptions import \
            UserNotHaveAccessToFields
        with pytest.raises(UserNotHaveAccessToFields):
            storage.validate_user_roles_with_field_ids_roles(
                field_ids=field_ids, user_roles=user_roles
            )

    def test_validate_user_roles_with_field_ids_with_valid_roles(
            self, storage):
        # Arrange
        fields = FieldRoleFactory.create_batch(3)
        field_ids = [field.field_id for field in fields]
        user_roles = [field.role for field in fields]

        # Act
        storage.validate_user_roles_with_field_ids_roles(
            field_ids=field_ids, user_roles=user_roles
        )
