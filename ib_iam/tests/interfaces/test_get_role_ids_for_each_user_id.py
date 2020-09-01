from uuid import UUID

import pytest


class TestGetUserIdWithRoleIdsDTO:

    @pytest.mark.django_db
    def test_with_invalid_user_ids_raise_exception(self):
        # Arrange
        user_ids = [
            "eca1a0c1-b9ef-4e59-b415-60a28ef17b10",
            "1231a0c1-b9ef-4e59-b415-60a28ef17b10",
            "adc1a0c1-b9ef-4e59-b415-60a28ef17b10"
        ]
        invalid_user_ids = [
            "1231a0c1-b9ef-4e59-b415-60a28ef17b10",
            "adc1a0c1-b9ef-4e59-b415-60a28ef17b10"
        ]
        from ib_iam.models import UserDetails
        UserDetails.objects.create(user_id=user_ids[0])

        from ib_iam.app_interfaces.service_interface import ServiceInterface
        service_interface = ServiceInterface()

        # Assert
        from ib_iam.exceptions.custom_exceptions import InvalidUserIds
        with pytest.raises(InvalidUserIds) as err:
            service_interface.get_users_role_ids(user_ids=user_ids)
        assert err.value.user_ids == invalid_user_ids

    @pytest.mark.django_db
    def test_with_valid_user_ids_return_response(self):
        # Arrange
        from ib_iam.interactors.dtos.dtos import UserIdWithRoleIdsDTO
        expected_response = [
            UserIdWithRoleIdsDTO(
                user_id='eca1a0c1-b9ef-4e59-b415-60a28ef17b10',
                role_ids=[
                    'e4ee6a9b8c3a',
                    'eb39482315c0'
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
        user_ids = [
            "eca1a0c1-b9ef-4e59-b415-60a28ef17b10",
            "abc1a0c1-b9ef-4e59-b415-60a28ef17b10",
            "1231a0c1-b9ef-4e59-b415-60a28ef17b10"
        ]
        from ib_iam.models import UserDetails
        UserDetails.objects.create(user_id=user_ids[0])
        UserDetails.objects.create(user_id=user_ids[1])
        UserDetails.objects.create(user_id=user_ids[2])

        role_ids = [
            "e4ee6a9b8c3a",
            "eb39482315c0",
            "1af3f6458df3",
            "f3e0c6aa65f6",
            "5e3fc083776b"
        ]
        from ib_iam.tests.factories.models import ProjectRoleFactory
        role_objects = [
            ProjectRoleFactory(role_id=role_id)
            for role_id in role_ids
        ]

        user_id1 = "eca1a0c1-b9ef-4e59-b415-60a28ef17b10"
        user_id2 = "abc1a0c1-b9ef-4e59-b415-60a28ef17b10"
        from ib_iam.tests.factories.models import UserRoleFactory
        UserRoleFactory.create(user_id=user_id1, project_role=role_objects[0])
        UserRoleFactory.create(user_id=user_id1, project_role=role_objects[1])
        UserRoleFactory.create(user_id=user_id2, project_role=role_objects[2])
        UserRoleFactory.create(user_id=user_id2, project_role=role_objects[3])
        UserRoleFactory.create(user_id=user_id2, project_role=role_objects[4])

        from ib_iam.app_interfaces.service_interface import ServiceInterface
        service_interface = ServiceInterface()

        # Act
        response = service_interface.get_users_role_ids(user_ids=user_ids)

        # Assert
        assert response == expected_response
