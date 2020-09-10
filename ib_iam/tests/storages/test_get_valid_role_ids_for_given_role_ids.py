import pytest
from ib_iam.tests.common_fixtures.reset_fixture \
    import reset_sequence_role_factory


class TestGetValidRoleIds:
    @pytest.mark.django_db
    def test_get_valid_role_ids(self):
        # Arrange
        role_ids = ["12233442", "12312323", "4141264557"]
        expected_valid_role_ids = ["12233442", "12312323"]

        from ib_iam.storages.user_storage_implementation \
            import UserStorageImplementation
        storage = UserStorageImplementation()
        reset_sequence_role_factory()
        from ib_iam.tests.factories.models import ProjectRoleFactory
        for role_id in expected_valid_role_ids:
            ProjectRoleFactory.create(role_id=role_id)

        # Act
        valid_role_ids = storage.get_valid_role_ids(role_ids=role_ids)

        # Assert
        assert valid_role_ids == expected_valid_role_ids
