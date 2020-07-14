import pytest

from ib_iam.storages.storage_implementation import StorageImplementation
from ib_iam.tests.factories.models import RoleFactory


class TestCreateRoles:
    @pytest.mark.django_db
    def test_from_list_of_roles(self):

        # Arrange
        storage = StorageImplementation()
        from ib_iam.tests.factories.storage_dtos import RoleDTOFactory
        list_of_role_dtos = RoleDTOFactory.create_batch(3)
        print(list_of_role_dtos)
        # Act
        roles = storage.create_roles_from_list_of_role_dtos(list_of_role_dtos)

        # Assert
        expected_roles = RoleFactory.create_batch(3)
        # role = roles[0]
        assert roles[0].role_id == expected_roles[0].role_id
