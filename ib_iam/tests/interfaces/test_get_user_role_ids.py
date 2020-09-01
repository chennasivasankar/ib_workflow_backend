import pytest


class TestGetUserRoleIds:

    @pytest.mark.django_db
    def test_get_user_role_ids_for_valid_user_ids_return_response(self):
        # Arrange
        expected_role_ids = [
            '1af3f6458df3',
            '5e3fc083776b',
            'e4ee6a9b8c3a',
            'eb39482315c0',
            'f3e0c6aa65f6'
        ]
        role_ids = [
            "e4ee6a9b8c3a",
            "eb39482315c0",
            "1af3f6458df3",
            "f3e0c6aa65f6",
            "5e3fc083776b"
        ]
        user_id = "eca1a0c1-b9ef-4e59-b415-60a28ef17b10"
        from ib_iam.models import UserDetails
        UserDetails.objects.create(user_id=user_id)

        from ib_iam.tests.factories.models import UserRoleFactory, \
            ProjectRoleFactory
        role_objects = [
            ProjectRoleFactory(role_id=role_id)
            for role_id in role_ids
        ]

        ProjectRoleFactory.create_batch(3)
        UserRoleFactory.create_batch(3)
        for role_object in role_objects:
            UserRoleFactory.create(user_id=user_id, project_role=role_object)

        from ib_iam.app_interfaces.service_interface import ServiceInterface
        service_interface = ServiceInterface()

        # Act
        response = service_interface.get_user_role_ids(user_id=user_id)

        # Assert
        assert response == expected_role_ids

    @pytest.mark.django_db
    def test_with_invalid_user_id_raise_exception(self, snapshot):
        # Arrange
        user_id = "eca1a0c1-b9ef-4e59-b415-60a28ef17b10"

        from ib_iam.app_interfaces.service_interface import ServiceInterface
        service_interface = ServiceInterface()

        # Assert
        from ib_iam.exceptions.custom_exceptions import InvalidUserId
        with pytest.raises(InvalidUserId):
            service_interface.get_user_role_ids(user_id=user_id)
