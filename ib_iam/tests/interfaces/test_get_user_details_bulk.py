import pytest


class TestGetUserDetailsBulk:

    @pytest.fixture()
    def user_profile_dtos(self):
        user_ids = ["user1", "user2", "user3"]
        from ib_iam.tests.factories.adapter_dtos import UserProfileDTOFactory
        user_profile_dtos = [UserProfileDTOFactory.create(user_id=user_id) \
                             for user_id in user_ids]
        return user_profile_dtos

    def test_with_valid_user_ids_return_respone(self, mocker,
                                                user_profile_dtos):
        # Arrange
        user_ids = ["user1", "user2", "user3"]

        from ib_iam.tests.common_fixtures.adapters.user_service \
            import get_users_adapter_mock
        get_users_adapter_mock(
            mocker=mocker,
            user_profile_dtos=user_profile_dtos
        )

        from ib_iam.app_interfaces.service_interface import ServiceInterface
        service_interface = ServiceInterface()

        # Act
        response = service_interface.get_user_details_bulk(user_ids=user_ids)

        # Assert
        assert response == user_profile_dtos
