import factory
import pytest

from ib_tasks.constants.constants import ALL_ROLES_ID
from ib_tasks.constants.enum import PermissionTypes
from ib_tasks.tests.factories.models import FieldFactory, FieldRoleFactory


@pytest.mark.django_db
class TestIsUserHasWritePermissionForAField:

    def test_check_is_user_has_write_permission_for_field_with_invalid_role_returns_false(
            self, storage):
        # Arrange
        user_roles = ["FIN_MAN"]
        field = FieldFactory.create()
        FieldRoleFactory.create(
            permission_type=PermissionTypes.WRITE.value,
            role=factory.Iterator(["RP_VALIDATIONS"]), field=field
        )
        field_id = field.field_id

        # Act
        is_user_has_read_permission_for_field = \
            storage.check_is_user_has_write_permission_for_field(
                field_id=field_id, user_roles=user_roles)

        # Assert
        assert is_user_has_read_permission_for_field is False

    def test_check_is_user_has_write_permission_for_field_with_valid_role_returns_true(
            self, storage):
        # Arrange
        user_roles = ["FIN_MAN"]
        field = FieldFactory.create()
        FieldRoleFactory.create(
            permission_type=PermissionTypes.WRITE.value,
            role=factory.Iterator(user_roles), field=field
        )
        field_id = field.field_id

        # Act
        is_user_has_read_permission_for_field = \
            storage.check_is_user_has_write_permission_for_field(
                field_id=field_id, user_roles=user_roles)

        # Assert
        assert is_user_has_read_permission_for_field is True

    def test_check_is_user_has_write_permission_for_field_with_all_roles_returns_true(
            self, storage):
        # Arrange
        user_roles = ["FIN_MAN"]
        field = FieldFactory.create()
        FieldRoleFactory.create(
            permission_type=PermissionTypes.WRITE.value,
            role=factory.Iterator([ALL_ROLES_ID]), field=field
        )
        field_id = field.field_id

        # Act
        is_user_has_read_permission_for_field = \
            storage.check_is_user_has_write_permission_for_field(
                field_id=field_id, user_roles=user_roles)

        # Assert
        assert is_user_has_read_permission_for_field is True
