from unittest.mock import patch

import pytest


class TestGetResetPasswordToken:
    @staticmethod
    def get_reset_password_token_mock(mocker):
        mock = mocker.patch(
            "ib_users.interfaces.service_interface.ServiceInterface.get_reset_password_token_for_reset_password"
        )
        return mock

    def test_get_reset_password_token(
            self, mocker
    ):
        # Arrange
        email = "test@gmail.com"
        expires_in_sec = 5647665599
        expected_token = "string"
        get_reset_password_token_for_reset_password_mock = \
            self.get_reset_password_token_mock(mocker)

        get_reset_password_token_for_reset_password_mock.return_value \
            = expected_token

        from ib_iam.adapters.service_adapter import ServiceAdapter
        service_adapter = ServiceAdapter()
        auth_service = service_adapter.auth_service

        # Act
        response = auth_service.get_reset_password_token(
            email=email, expires_in_sec=expires_in_sec
        )

        # Assert
        assert response == expected_token
        get_reset_password_token_for_reset_password_mock.assert_called_once()

    def test_with_invalid_email_raise_exception_for_reset_password_token(
            self, mocker):
        # Arrange
        email = "test@gmail.com"
        expires_in_sec = 5647665599
        get_reset_password_token_for_reset_password_mock = \
            self.get_reset_password_token_mock(mocker)

        from ib_users.constants.custom_exception_messages import INVALID_EMAIL
        from ib_users.validators.base_validator import CustomException
        get_reset_password_token_for_reset_password_mock.side_effect \
            = CustomException(exception_type=INVALID_EMAIL.code,
                              message=INVALID_EMAIL.message)

        from ib_iam.adapters.service_adapter import ServiceAdapter
        service_adapter = ServiceAdapter()
        auth_service = service_adapter.auth_service

        # Assert
        from ib_iam.exceptions.custom_exceptions import InvalidEmail
        with pytest.raises(InvalidEmail):
            auth_service.get_reset_password_token(
                email=email, expires_in_sec=expires_in_sec
            )
        get_reset_password_token_for_reset_password_mock.assert_called_once()
