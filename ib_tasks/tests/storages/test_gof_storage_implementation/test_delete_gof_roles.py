import pytest

from ib_tasks.models import GoFRole
from ib_tasks.tests.factories.models import GoFRoleFactory


@pytest.mark.django_db
class TestDeleteGoFRoles:

    def test_delete_gof_roles(self, storage):

        # Arrange
        gof_roles = GoFRoleFactory.create_batch(size=2)
        gof_ids = [gof_role.gof_id for gof_role in gof_roles]

        # Act
        storage.delete_gof_roles(gof_ids=gof_ids)

        # Assert
        gof_roles = list(GoFRole.objects.filter(gof_id__in=gof_ids))
        assert gof_roles == []
