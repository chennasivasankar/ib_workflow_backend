import pytest


class TestGetValidRoleIds:
    @pytest.mark.django_db
    def test_get_valid_role_ids(self):
        # Arrange
        role_ids = ["12233442", "12312323", "4141264557"]
        expected_valid_ids = ["12233442", "12312323"]

        from ib_iam.storages.storage_implementation import StorageImplementation
        storage = StorageImplementation()
        from ib_iam.tests.factories.models import RoleFactory
        RoleFactory.create(role_id=expected_valid_ids[0])
        RoleFactory.create(role_id=expected_valid_ids[1])

        # Act
        valid_role_ids = storage.get_valid_role_ids(role_ids=role_ids)

        # Assert
        assert valid_role_ids == expected_valid_ids

