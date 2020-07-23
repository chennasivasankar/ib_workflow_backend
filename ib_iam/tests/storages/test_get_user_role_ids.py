from uuid import UUID

import pytest


class TestGetUserRoleIds:
    @pytest.mark.django_db
    def test_get_user_role_ids(self):
        # Arrange
        expected_role_ids =  [
            UUID('b953895a-b77b-4a60-b94d-e4ee6a9b8c3a'),
            UUID('804c2d9f-8985-454f-a504-eb39482315c0'),
            UUID('635bbec1-2054-4860-80fa-1af3f6458df3'),
            UUID('22832ab6-100e-4d8e-b3a3-f3e0c6aa65f6'),
            UUID('66040b6e-c8e5-46ab-a313-5e3fc083776b')
        ]
        user_id = "eca1a0c1-b9ef-4e59-b415-60a28ef17b10"

        from ib_iam.storages.storage_implementation import StorageImplementation
        storage = StorageImplementation()
        from ib_iam.tests.factories.models import UserRoleFactory, RoleFactory
        role_objects = [
            RoleFactory(id=role_id)
            for role_id in expected_role_ids
        ]

        RoleFactory.create_batch(3)
        UserRoleFactory.create_batch(3)
        for role_object in role_objects:
            UserRoleFactory.create(user_id=user_id, role=role_object)

        # Act
        response = storage.get_user_role_ids(user_id=user_id)

        # Assert
        assert response == expected_role_ids
