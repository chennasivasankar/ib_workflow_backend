import pytest

from ib_iam.models.role import Role
from ib_iam.storages.storage_implementation import StorageImplementation


class TestCreateRoles:
    @pytest.mark.django_db
    def test_create_roles_given_role_dtos_then_store_roles_in_db(self):
        # Arrange
        storage = StorageImplementation()
        previous_storage_len = Role.objects.count()
        objects_count = 3
        from ib_iam.tests.factories.storage_dtos import RoleDTOFactory
        role_dtos = RoleDTOFactory.create_batch(objects_count)

        # Act
        storage.create_roles(role_dtos=role_dtos)

        # Assert
        current_storage_len = Role.objects.count()
        no_of_objects_created = current_storage_len - previous_storage_len
        assert no_of_objects_created == objects_count
