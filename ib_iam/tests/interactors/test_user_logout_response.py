from unittest.mock import patch


class TestUserLogoutResponse:

    def test_with_valid_user_id_return_response(
            self, mocker
    ):
        # Arrange
        user_id = 1

        from ib_iam.interactors.user_logout_interactor import \
            UserLogoutInteractor
        from ib_iam.tests.common_fixtures.adapters.auth_service_adapter_mocks \
            import prepare_user_log_out_from_a_device_mock
        user_log_out_from_a_device_mock \
            = prepare_user_log_out_from_a_device_mock(mocker)
        interactor = UserLogoutInteractor()

        # Act
        interactor.user_logout_wrapper(user_id=user_id)

        # Assert
        user_log_out_from_a_device_mock.assert_called_once()
