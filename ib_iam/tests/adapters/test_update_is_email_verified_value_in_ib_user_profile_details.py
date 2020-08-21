class TestUpdateIsEmailVerifiedValueInIbUsers:
    def update_user_profile_mock(self, mocker):
        mock = mocker.patch(
            "ib_users.interfaces.service_interface.ServiceInterface.update_user_profile"
        )
        return mock

    def test_update_is_email_verified_value_as_false(self, mocker):
        is_email_verified = False
        user_id = "1"
        from ib_users.interactors.user_profile_interactor import UserProfileDTO
        user_profile = UserProfileDTO(
            is_email_verified=is_email_verified
        )
        update_user_profile_mock = self.update_user_profile_mock(mocker=mocker)
        update_user_profile_mock.return_value = None

        from ib_iam.adapters.service_adapter import ServiceAdapter
        service_adapter = ServiceAdapter()
        auth_service = service_adapter.auth_service
        auth_service.update_is_email_verified_value_in_ib_user_profile_details(
            user_id=user_id, is_email_verified=is_email_verified)

        update_user_profile_mock.assert_called_once_with(
            user_id=user_id, user_profile=user_profile)

    def test_update_is_email_verified_value_as_true(self, mocker):
        is_email_verified = True
        user_id = "1"
        from ib_users.interactors.user_profile_interactor import UserProfileDTO
        user_profile = UserProfileDTO(
            is_email_verified=is_email_verified
        )
        update_user_profile_mock = self.update_user_profile_mock(mocker=mocker)
        update_user_profile_mock.return_value = None

        from ib_iam.adapters.service_adapter import ServiceAdapter
        service_adapter = ServiceAdapter()
        auth_service = service_adapter.auth_service
        auth_service.update_is_email_verified_value_in_ib_user_profile_details(
            user_id=user_id, is_email_verified=is_email_verified)

        update_user_profile_mock.assert_called_once_with(
            user_id=user_id, user_profile=user_profile)
