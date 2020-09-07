import factory
import pytest

from ib_tasks.constants.enum import PermissionTypes
from ib_tasks.tests.factories.models import GoFRoleFactory


@pytest.mark.django_db
class TestGetGoFIdsHavingWritePermissionForUser:

    def test_get_gof_ids_having_write_permission_for_user(self, storage):
        # Arrange
        user_roles = ["FIN_MAN"]
        from ib_tasks.tests.factories.models import GoFFactory
        gofs = GoFFactory.create_batch(size=2)
        GoFRoleFactory.create_batch(
            size=2, permission_type=PermissionTypes.WRITE.value,
            role=factory.Iterator(user_roles),
            gof=factory.Iterator(gofs)
        )
        gof_ids = [gof.gof_id for gof in gofs]

        # Act
        gof_ids_having_write_permission_for_user = \
            storage.get_gof_ids_having_write_permission_for_user(
                gof_ids=gof_ids, user_roles=user_roles)

        # Assert
        assert gof_ids_having_write_permission_for_user == gof_ids

    def test_get_gof_ids_having_write_permission_for_user_in_all_roles_case(
            self, storage):
        # Arrange
        user_roles = ["FIN_MAN"]
        from ib_tasks.tests.factories.models import GoFFactory
        gofs = GoFFactory.create_batch(size=2)
        from ib_tasks.constants.constants import ALL_ROLES_ID
        GoFRoleFactory.create_batch(
            size=2, permission_type=PermissionTypes.WRITE.value,
            role=factory.Iterator([ALL_ROLES_ID]),
            gof=factory.Iterator(gofs)
        )
        gof_ids = [gof.gof_id for gof in gofs]

        # Act
        gof_ids_having_write_permission_for_user = \
            storage.get_gof_ids_having_write_permission_for_user(
                gof_ids=gof_ids, user_roles=user_roles)

        # Assert
        assert gof_ids_having_write_permission_for_user == gof_ids
