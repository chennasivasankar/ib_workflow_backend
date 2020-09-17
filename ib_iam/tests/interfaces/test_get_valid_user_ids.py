import pytest


class TestGetValidUserIds:

    @pytest.mark.django_db
    def test_get_valid_user_ids(self):
        # Arrange
        user_ids = [
            "eca1a0c1-b9ef-4e59-b415-60a28ef17b10",
            "abc1a0c1-b9ef-4e59-b415-60a28ef17b10",
            "1231a0c1-b9ef-4e59-b415-60a28ef17b10"
        ]
        expected_valid_user_ids = ["eca1a0c1-b9ef-4e59-b415-60a28ef17b10"]
        from ib_iam.tests.factories.models import UserDetailsFactory
        UserDetailsFactory.reset_sequence(0)
        UserDetailsFactory.create(user_id=user_ids[0])

        from ib_iam.app_interfaces.service_interface import ServiceInterface
        service_interface = ServiceInterface()

        # Act
        valid_user_ids = service_interface.get_valid_user_ids(user_ids=user_ids)

        # Assert
        assert valid_user_ids == expected_valid_user_ids
