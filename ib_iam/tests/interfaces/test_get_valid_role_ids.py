import pytest


class TestGetValidRoleIds:

    @pytest.mark.django_db
    def test_with_role_ids_return_valid_role_ids(self, snapshot):
        # Arrange
        role_ids = ["12233442", "12312323", "4141264557", "12312323"]
        expected_valid_role_ids = ["12233442", "12312323"]
        from ib_iam.tests.factories.models import RoleFactory
        RoleFactory.create(role_id=expected_valid_role_ids[0])
        RoleFactory.create(role_id=expected_valid_role_ids[1])

        from ib_iam.app_interfaces.service_interface import ServiceInterface
        service_interface = ServiceInterface()

        # Act
        valid_role_ids = service_interface.get_valid_role_ids(
            role_ids=role_ids)

        # Assert
        assert valid_role_ids == expected_valid_role_ids
