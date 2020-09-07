import pytest


class TestGetUserIdWIthRoleIdsDTOS:

    @pytest.mark.django_db
    def test_get_user_id_with_role_ids_dtos(self):
        # Arrange
        from ib_iam.interactors.dtos.dtos import UserIdWithRoleIdsDTO
        expected_user_id_with_role_ids_dtos = [
            UserIdWithRoleIdsDTO(
                user_id='eca1a0c1-b9ef-4e59-b415-60a28ef17b10',
                role_ids=[
                    "e4ee6a9b8c3a",
                    "eb39482315c0"
                ]
            ),
            UserIdWithRoleIdsDTO(
                user_id='abc1a0c1-b9ef-4e59-b415-60a28ef17b10',
                role_ids=[
                    '1af3f6458df3',
                    '5e3fc083776b',
                    'f3e0c6aa65f6'
                ]
            ),
            UserIdWithRoleIdsDTO(
                user_id='1231a0c1-b9ef-4e59-b415-60a28ef17b10',
                role_ids=[]
            )
        ]

        ids_and_role_ids = [
            "e4ee6a9b8c3a",
            "eb39482315c0",
            "1af3f6458df3",
            "f3e0c6aa65f6",
            "5e3fc083776b"
        ]
        from ib_iam.tests.factories.models import ProjectRoleFactory
        role_objects = [
            ProjectRoleFactory(role_id=role_id)
            for role_id in ids_and_role_ids
        ]

        user_id1 = "eca1a0c1-b9ef-4e59-b415-60a28ef17b10"
        user_id2 = "abc1a0c1-b9ef-4e59-b415-60a28ef17b10"
        user_id3 = "1231a0c1-b9ef-4e59-b415-60a28ef17b10"
        from ib_iam.tests.factories.models import UserRoleFactory
        UserRoleFactory.create(user_id=user_id1, project_role=role_objects[0])
        UserRoleFactory.create(user_id=user_id1, project_role=role_objects[1])
        UserRoleFactory.create(user_id=user_id2, project_role=role_objects[2])
        UserRoleFactory.create(user_id=user_id2, project_role=role_objects[3])
        UserRoleFactory.create(user_id=user_id2, project_role=role_objects[4])

        from ib_iam.storages.roles_storage_implementation import \
            RolesStorageImplementation
        storage = RolesStorageImplementation()

        # Act
        response = storage.get_user_id_with_role_ids_dtos(
            user_ids=[user_id1, user_id2, user_id3]
        )

        # Assert
        assert response == expected_user_id_with_role_ids_dtos

    @pytest.mark.django_db
    def test_invalid_user_ids_raise_exception(self):
        # Arrange
        user_ids = [
            "eca1a0c1-b9ef-4e59-b415-60a28ef17b10",
            "acd1a0c1-b9ef-4e59-b415-60a28ef17b10"
        ]
        invalid_user_ids = user_ids

        from ib_iam.storages.roles_storage_implementation import \
            RolesStorageImplementation
        storage = RolesStorageImplementation()

        # Assert
        from ib_iam.exceptions.custom_exceptions import InvalidUserIds
        with pytest.raises(InvalidUserIds) as err:
            storage.validate_user_ids(user_ids=user_ids)

        assert err.value.user_ids == invalid_user_ids
