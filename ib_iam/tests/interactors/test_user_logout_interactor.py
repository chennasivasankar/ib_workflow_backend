import pytest


class TestUserLogoutResponse:

    @pytest.fixture
    def interactor(self):
        from ib_iam.interactors.user_logout_interactor import \
            UserLogoutInteractor
        return UserLogoutInteractor()

    def test_with_valid_user_id_return_response(
            self, mocker, interactor
    ):
        # Arrange
        user_id = 1

        from ib_iam.tests.common_fixtures.adapters.auth_service_adapter_mocks \
            import user_log_out_from_a_device_mock
        user_log_out_from_a_device_mock \
            = user_log_out_from_a_device_mock(mocker)

        # Act
        interactor.user_logout_wrapper(user_id=user_id)

        # Assert
        user_log_out_from_a_device_mock.assert_called_once()
