from uuid import UUID

import pytest


class TestGetUserIdWIthRoleIdsDTOS:

    @pytest.mark.django_db
    def test_get_user_id_with_role_ids_dtos(self):
        # Arrange
        from ib_iam.interactors.DTOs.common_dtos import UserIdWithRoleIdsDTO
        expected_user_id_with_role_ids_dtos = [
            UserIdWithRoleIdsDTO(
                user_id='eca1a0c1-b9ef-4e59-b415-60a28ef17b10',
                role_ids=[
                    'b953895a-b77b-4a60-b94d-e4ee6a9b8c3a',
                    '804c2d9f-8985-454f-a504-eb39482315c0'
                ]
            ),
            UserIdWithRoleIdsDTO(
                user_id='abc1a0c1-b9ef-4e59-b415-60a28ef17b10',
                role_ids=[
                    '635bbec1-2054-4860-80fa-1af3f6458df3',
                    '22832ab6-100e-4d8e-b3a3-f3e0c6aa65f6',
                    '66040b6e-c8e5-46ab-a313-5e3fc083776b'
                ]
            ),
            UserIdWithRoleIdsDTO(
                user_id='1231a0c1-b9ef-4e59-b415-60a28ef17b10',
                role_ids=[]
            )
        ]

        expected_role_ids = [
            'b953895a-b77b-4a60-b94d-e4ee6a9b8c3a',
            '804c2d9f-8985-454f-a504-eb39482315c0',
            '635bbec1-2054-4860-80fa-1af3f6458df3',
            '22832ab6-100e-4d8e-b3a3-f3e0c6aa65f6',
            '66040b6e-c8e5-46ab-a313-5e3fc083776b'
        ]
        from ib_iam.tests.factories.models import RoleFactory
        role_objects = [
            RoleFactory(id=role_id)
            for role_id in expected_role_ids
        ]

        user_id1 = "eca1a0c1-b9ef-4e59-b415-60a28ef17b10"
        user_id2 = "abc1a0c1-b9ef-4e59-b415-60a28ef17b10"
        user_id3 = "1231a0c1-b9ef-4e59-b415-60a28ef17b10"
        from ib_iam.tests.factories.models import UserRoleFactory
        UserRoleFactory.create(user_id=user_id1, role=role_objects[0])
        UserRoleFactory.create(user_id=user_id1, role=role_objects[1])
        UserRoleFactory.create(user_id=user_id2, role=role_objects[2])
        UserRoleFactory.create(user_id=user_id2, role=role_objects[3])
        UserRoleFactory.create(user_id=user_id2, role=role_objects[4])

        from ib_iam.storages.storage_implementation import StorageImplementation
        storage = StorageImplementation()

        # Act
        response = storage.get_user_id_with_role_ids_dtos(
            user_ids=[user_id1, user_id2, user_id3]
        )

        # Assert
        assert response == expected_user_id_with_role_ids_dtos
