from unittest.mock import patch

from freezegun import freeze_time


class TestAuthService:

    @patch(
        "ib_users.interfaces.service_interface.ServiceInterface.get_user_auth_tokens_for_login_with_email_and_password"
    )
    @freeze_time("2020-01-14 12:00:01")
    def test_get_user_tokens_dto_for_given_email_and_password_dto(
            self, get_user_auth_tokens_for_login_with_email_and_password_mock
    ):
        # Arrange
        from ib_iam.adapters.auth_service import EmailAndPasswordDTO
        email_and_password_dto = EmailAndPasswordDTO(
            email="test@gmail.com",
            password="test123"
        )

        from ib_users.interactors.third_party.user_tokens_generator import \
            UserAuthTokensDTO
        from datetime import datetime
        user_auth_tokens_dto = UserAuthTokensDTO(
            access_token="asdfaldskfjdfdlsdkf",
            refresh_token="sadfenkljkdfeller",
            expires_in=datetime(year=2199, month=1, day=2),
            user_id="11"
        )

        from ib_iam.adapters.auth_service import UserTokensDTO
        expected_user_tokens_dtos = UserTokensDTO(
            access_token='asdfaldskfjdfdlsdkf',
            refresh_token='sadfenkljkdfeller',
            expires_in_seconds=5647665599,
            user_id='11'
        )

        get_user_auth_tokens_for_login_with_email_and_password_mock.return_value \
            = user_auth_tokens_dto

        from ib_iam.adapters.service_adapter import ServiceAdapter
        service_adapter = ServiceAdapter()
        auth_service = service_adapter.auth_service

        # Act
        response = auth_service.get_user_tokens_dto_for_given_email_and_password_dto(
            email_and_password_dto=email_and_password_dto
        )

        # Assert
        assert response == expected_user_tokens_dtos

    @patch(
        "ib_users.interfaces.service_interface.ServiceInterface.get_reset_password_token_for_reset_password"
    )
    def test_get_reset_password_token(
            self, get_reset_password_token_for_reset_password_mock
    ):
        # Arrange
        email = "test@gmail.com"
        expires_in_sec = 5647665599
        expected_token = "string"

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

    @patch(
        "ib_users.interfaces.service_interface.ServiceInterface.reset_password_for_given_user_password_reset_token"
    )
    def test_update_user_password_with_reset_password_token(
            self, reset_password_for_given_user_password_reset_token_mock
    ):
        # Arrange
        reset_password_token = "string"
        password = "string123"

        # Act
        from ib_iam.adapters.service_adapter import ServiceAdapter
        service_adapter = ServiceAdapter()
        auth_service = service_adapter.auth_service

        # Act
        response = auth_service.update_user_password_with_reset_password_token(
            reset_password_token=reset_password_token,
            password=password
        )

        # Assert
        reset_password_for_given_user_password_reset_token_mock. \
            assert_called_once()
