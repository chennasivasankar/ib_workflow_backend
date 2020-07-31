from unittest.mock import patch


class TestCreateUserProfile:
    @patch('ib_users.interfaces.service_interface.ServiceInterface.create_user_profile')
    def test_create_user_profile_creates_user(self, create_user_profile_mock):
        # Arrange
        name = 'parker'
        email = 'parker2020@gmail.com'
        user_id = 'e06b8a3b-94af-4d2e-ba14-bcec11140277'
        from ib_iam.adapters.dtos import UserProfileDTO
        profile_dto_from_interactor = UserProfileDTO(
            user_id=user_id,
            name=name,
            email=email
        )
        from ib_iam.adapters.service_adapter import ServiceAdapter
        service_adapter = ServiceAdapter()

        # Act
        service_adapter.user_service.create_user_profile(
            user_id=user_id, user_profile_dto=profile_dto_from_interactor)

        # Assert
        create_user_profile_mock.assert_called_once()