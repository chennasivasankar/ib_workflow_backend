from unittest.mock import patch


class TestUserLogoutResponse:

    @patch("ib_iam.adapters.auth_service.AuthService.user_log_out_from_a_device")
    def test_with_valid_user_id_return_response(self,
                                                user_log_out_from_a_device_mock):
        # Arrange
        user_id = 1

        from ib_iam.interactors.user_logout_interactor import \
            UserLogoutInteractor

        interactor = UserLogoutInteractor()

        # Act
        interactor.user_logout_wrapper(user_id=user_id)

        # Assert
        user_log_out_from_a_device_mock.assert_called_once()