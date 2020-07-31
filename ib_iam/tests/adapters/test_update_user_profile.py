from unittest.mock import patch


class TestUpdateUserProfile:
    @patch('ib_users.interfaces.service_interface.ServiceInterface.update_user_profile')
    def test_update_user_profile_updates_profile_of_user_in_ib_users(
            self, update_user_profile_mock):
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
        from ib_users.interactors.user_profile_interactor \
            import UserProfileDTO
        user_profile = UserProfileDTO(
            name=profile_dto_from_interactor.name,
            email=profile_dto_from_interactor.email,
        )
        # Act
        service_adapter.user_service.update_user_profile(
            user_id, profile_dto_from_interactor)

        # Assert
        update_user_profile_mock.assert_called_once_with(
            user_id=user_id, user_profile=user_profile)