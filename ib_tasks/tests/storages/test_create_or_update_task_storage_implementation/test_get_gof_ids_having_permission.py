import pytest

from ib_tasks.constants.constants import ALL_ROLES_ID
from ib_tasks.tests.factories.models import GoFRoleFactory


@pytest.mark.django_db
class TestGetGoFIdsHavingPermission:
    def test_given_gof_ids_and_user_roles_returns_gof_ids_having_permission_for_roles(
            self, storage, snapshot
    ):
        # Arrange
        gof_role_objects = GoFRoleFactory.create_batch(size=10)
        gof_role_obj = GoFRoleFactory(role=ALL_ROLES_ID)
        gof_ids = [
            gof_role_objects[0].gof_id,
            gof_role_objects[3].gof_id,
            gof_role_objects[5].gof_id,
            gof_role_objects[9].gof_id,
            gof_role_objects[1].gof_id,
            gof_role_obj.gof_id
        ]
        user_roles = [
            gof_role_objects[3].role,
            gof_role_objects[9].role,
            gof_role_objects[1].role
        ]

        # Act
        gof_ids_having_permission = storage.get_gof_ids_having_permission(
            gof_ids=gof_ids, user_roles=user_roles)

        # Assert
        snapshot.assert_match(
            name="gof_ids_having_permission", value=gof_ids_having_permission)

    def test_given_gof_ids_and_user_roles_not_having_permission_for_gof_ids_but_permission_for_all_roles_returns_gof_ids(
            self, snapshot, storage
    ):
        # Arrange
        gof_role_objs = GoFRoleFactory.create_batch(size=10)
        gof_role_obj = GoFRoleFactory(role=ALL_ROLES_ID)
        gof_ids = [
            gof_role_objs[0].gof_id,
            gof_role_objs[3].gof_id,
            gof_role_objs[5].gof_id,
            gof_role_objs[9].gof_id,
            gof_role_objs[1].gof_id,
            gof_role_obj.gof_id
        ]
        user_roles = [
            "ADMIN"
        ]

        # Act
        gof_ids_having_permission = storage.get_gof_ids_having_permission(
            gof_ids=gof_ids, user_roles=user_roles)

        # Assert
        snapshot.assert_match(
            name="gof_ids_having_permission", value=gof_ids_having_permission)
