import factory
import pytest

from ib_tasks.constants.constants import ALL_ROLES_ID
from ib_tasks.constants.enum import PermissionTypes
from ib_tasks.tests.factories.models import FieldFactory, FieldRoleFactory


@pytest.mark.django_db
class TestGetFieldIdsHavingReadPermissionsForUser:

    def test_get_field_ids_having_read_permission_for_user(self, storage):
        # Arrange
        user_roles = ["FIN_MAN"]
        fields = FieldFactory.create_batch(size=2)
        FieldRoleFactory.create_batch(
            size=2, permission_type=PermissionTypes.READ.value,
            role=factory.Iterator(user_roles),
            field=factory.Iterator(fields)
        )
        field_ids = [field.field_id for field in fields]

        # Act
        field_ids_having_read_permission_for_user = \
            storage.get_field_ids_having_read_permission_for_user(
                field_ids=field_ids, user_roles=user_roles)

        # Assert
        assert field_ids_having_read_permission_for_user == field_ids

    def test_get_field_ids_having_read_permission_for_user_when_fields_has_all_roles(
            self, storage):
        # Arrange
        user_roles = ["FIN_MAN"]
        fields = FieldFactory.create_batch(size=2)
        FieldRoleFactory.create_batch(
            size=2, permission_type=factory.Iterator(
                [PermissionTypes.WRITE.value, PermissionTypes.READ.value]),
            role=factory.Iterator([ALL_ROLES_ID]),
            field=factory.Iterator(fields)
        )
        field_ids = [field.field_id for field in fields]

        # Act
        field_ids_having_read_permission_for_user = \
            storage.get_field_ids_having_read_permission_for_user(
                field_ids=field_ids, user_roles=user_roles)

        # Assert
        assert field_ids_having_read_permission_for_user == field_ids
