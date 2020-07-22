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
        expeected_role_objs = Role.objects.all()
        assert no_of_objects_created == objects_count
        for role_dto, role_obj in zip(role_dtos, expeected_role_objs):
            assert role_obj.role_id == role_dto.role_id

