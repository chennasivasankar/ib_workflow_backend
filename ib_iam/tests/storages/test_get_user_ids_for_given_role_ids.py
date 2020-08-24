import pytest
from ib_iam.tests.common_fixtures.reset_fixture \
    import reset_sequence_role_factory


class TestGetUserIdsForGivenRoleIds:
    @pytest.mark.django_db
    def test_get_user_ids_for_given_role_ids(self):
        # Arrange
        role_ids = ["12233442", "12312323", "4141264557"]
        actual_user_ids = ["1234", "1234", "12345"]
        user_roles = [
            {"role_id": role_id, "user_id": actual_user_ids[index]}
            for index, role_id in enumerate(role_ids)
        ]

        from ib_iam.storages.user_storage_implementation \
            import UserStorageImplementation
        storage = UserStorageImplementation()
        reset_sequence_role_factory()
        from ib_iam.tests.factories.models import UserRoleFactory, ProjectRoleFactory
        for user_role in user_roles:
            role_object = ProjectRoleFactory.create(role_id=user_role["role_id"])
            UserRoleFactory.create(
                project_role=role_object, user_id=user_role["user_id"])

        # Act
        expected_user_ids = storage.get_user_ids(role_ids=role_ids)

        # Assert
        assert actual_user_ids == expected_user_ids
