from uuid import UUID

import pytest


class TestGetUserRoleIds:

    @pytest.mark.django_db
    def test_get_user_role_ids_for_valid_user_ids_return_response(self):
        # Arrange
        expected_role_ids = [
            'e4ee6a9b8c3a',
            'eb39482315c0',
            '1af3f6458df3',
            'f3e0c6aa65f6',
            '5e3fc083776b'
        ]
        ids_and_role_ids = [
            (UUID('b953895a-b77b-4a60-b94d-e4ee6a9b8c3a'), "e4ee6a9b8c3a"),
            (UUID('804c2d9f-8985-454f-a504-eb39482315c0'), "eb39482315c0"),
            (UUID('635bbec1-2054-4860-80fa-1af3f6458df3'), "1af3f6458df3"),
            (UUID('22832ab6-100e-4d8e-b3a3-f3e0c6aa65f6'), "f3e0c6aa65f6"),
            (UUID('66040b6e-c8e5-46ab-a313-5e3fc083776b'), "5e3fc083776b")
        ]
        user_id = "eca1a0c1-b9ef-4e59-b415-60a28ef17b10"
        from ib_iam.models import UserDetails
        UserDetails.objects.create(user_id=user_id)

        from ib_iam.tests.factories.models import UserRoleFactory, ProjectRoleFactory
        role_objects = [
            ProjectRoleFactory(id=id, role_id=role_id)
            for id, role_id in ids_and_role_ids
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
