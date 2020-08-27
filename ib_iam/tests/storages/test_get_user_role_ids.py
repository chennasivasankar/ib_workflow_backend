import pytest


class TestGetUserRoleIds:
    @pytest.mark.django_db
    def test_get_user_role_ids(self):
        # Arrange
        expected_role_ids = [
            'e4ee6a9b8c3a',
            'eb39482315c0',
            '1af3f6458df3',
            'f3e0c6aa65f6',
            '5e3fc083776b'
        ]

        role_ids = [
            "e4ee6a9b8c3a",
            "eb39482315c0",
            "1af3f6458df3",
            "f3e0c6aa65f6",
            "5e3fc083776b"
        ]
        user_id = "eca1a0c1-b9ef-4e59-b415-60a28ef17b10"

        from ib_iam.storages.roles_storage_implementation import \
            RolesStorageImplementation
        storage = RolesStorageImplementation()
        from ib_iam.tests.factories.models import UserRoleFactory, \
            ProjectRoleFactory
        role_objects = [
            ProjectRoleFactory(role_id=role_id)
            for role_id in role_ids
        ]

        ProjectRoleFactory.create_batch(3)
        # Todo if below line uncomment we will get tear down error
        # UserRoleFactory.create_batch(3)
        for role_object in role_objects:
            UserRoleFactory.create(user_id=user_id, project_role=role_object)

        # Act
        response = storage.get_user_role_ids(user_id=user_id)

        # Assert
        assert response == expected_role_ids

    @pytest.mark.django_db
    def test_invalid_user_id_raise_exception(self):
        # Arrange
        user_id = "eca1a0c1-b9ef-4e59-b415-60a28ef17b10"

        from ib_iam.storages.roles_storage_implementation import \
            RolesStorageImplementation
        storage = RolesStorageImplementation()

        # Assert
        from ib_iam.exceptions.custom_exceptions import InvalidUserId
        with pytest.raises(InvalidUserId):
            storage.validate_user_id(user_id=user_id)
