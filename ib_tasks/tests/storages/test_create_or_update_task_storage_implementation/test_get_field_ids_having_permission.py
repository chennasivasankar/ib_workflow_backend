import pytest

from ib_tasks.constants.constants import ALL_ROLES_ID
from ib_tasks.tests.factories.models import FieldRoleFactory


@pytest.mark.django_db
class TestFieldIdsHavingPermission:

    def test_given_field_ids_and_user_roles_returns_field_ids_having_permission_for_roles(
            self, storage, snapshot
    ):
        # Arrange
        field_role_objs = FieldRoleFactory.create_batch(size=10)
        field_role_obj = FieldRoleFactory(role=ALL_ROLES_ID)
        field_ids = [
            field_role_objs[0].field_id,
            field_role_objs[3].field_id,
            field_role_objs[9].field_id,
            field_role_objs[6].field_id,
            field_role_obj.field_id
        ]
        user_roles = [
            field_role_objs[0].role
        ]

        # Act
        field_ids_having_permission = storage.get_field_ids_having_permission(
            field_ids=field_ids, user_roles=user_roles)

        # Assert
        snapshot.assert_match(
            name="field_ids_having_permission",
            value=field_ids_having_permission)

    def test_given_field_ids_and_user_roles_not_having_permission_for_field_ids_but_permission_for_all_roles_returns_field_ids(
            self, snapshot, storage
    ):
        # Arrange
        field_role_objs = FieldRoleFactory.create_batch(size=10)
        field_role_obj = FieldRoleFactory(role=ALL_ROLES_ID)
        field_ids = [
            field_role_objs[0].field_id,
            field_role_objs[3].field_id,
            field_role_objs[9].field_id,
            field_role_objs[6].field_id,
            field_role_obj.field_id
        ]
        user_roles = ["ADMIN"]

        # Act
        field_ids_having_permission = storage.get_field_ids_having_permission(
            field_ids=field_ids, user_roles=user_roles
        )

        # Assert
        snapshot.assert_match(
            name="field_ids_having_permission",
            value=field_ids_having_permission)
