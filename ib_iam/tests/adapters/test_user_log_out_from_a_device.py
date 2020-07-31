from unittest.mock import patch


class TestLogOutFromADevice:

    @patch(
        "ib_users.interfaces.service_interface.ServiceInterface.logout_in_all_devices"
    )
    def test_user_log_out_from_a_device(self, logout_in_all_devices_mock):
        # Arrange
        user_id = "string"
        from ib_iam.adapters.service_adapter import ServiceAdapter
        service_adapter = ServiceAdapter()
        auth_service = service_adapter.auth_service

        # Act
        auth_service.user_log_out_from_a_device(user_id=user_id)

        # Assert
        logout_in_all_devices_mock.assert_called_once()
