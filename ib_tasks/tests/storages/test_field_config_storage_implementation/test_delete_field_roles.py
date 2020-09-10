import pytest

from ib_tasks.models import FieldRole
from ib_tasks.tests.factories.models import FieldRoleFactory


@pytest.mark.django_db
class TestDeleteFieldRoles:

    def test_delete_field_roles_given_field_ids(self, storage):
        # Arrange
        field_roles = FieldRoleFactory.create_batch(size=2)
        field_ids = [field_role.field_id for field_role in field_roles]

        # Act
        storage.delete_field_roles(field_ids)

        # Assert
        field_roles = list(FieldRole.objects.filter(field_id__in=field_ids))
        assert field_roles == []
