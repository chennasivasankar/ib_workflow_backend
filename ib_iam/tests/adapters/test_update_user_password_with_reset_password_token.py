import pytest


class TestUpdateUserPasswordAdapter:
    def reset_password_mock(self, mocker):
        mock = mocker.patch(
            "ib_users.interfaces.service_interface.ServiceInterface.reset_password_for_given_user_password_reset_token"
        )
        return mock

    def test_update_user_password_with_reset_password_token(
            self, mocker):
        # Arrange
        reset_password_token = "string"
        password = "string123"
        reset_password_for_given_user_password_reset_token_mock = \
            self.reset_password_mock(mocker=mocker)

        # Act
        from ib_iam.adapters.service_adapter import ServiceAdapter
        service_adapter = ServiceAdapter()
        auth_service = service_adapter.auth_service

        # Act
        auth_service.update_user_password_with_reset_password_token(
            reset_password_token=reset_password_token,
            password=password
        )

        # Assert
        reset_password_for_given_user_password_reset_token_mock. \
            assert_called_once()

    def test_incorrect_password_for_password_at_least_one_special_character_raise_exception(
            self, mocker
    ):
        # Arrange
        reset_password_token = "string"
        password = "string123"
        reset_password_for_given_user_password_reset_token_mock = \
            self.reset_password_mock(mocker=mocker)

        from ib_users.constants.custom_exception_messages import \
            PASSWORD_AT_LEAST_1_SPECIAL_CHARACTER
        from ib_users.validators.base_validator import CustomException
        reset_password_for_given_user_password_reset_token_mock.side_effect \
            = CustomException(
            exception_type=PASSWORD_AT_LEAST_1_SPECIAL_CHARACTER.code,
            message=PASSWORD_AT_LEAST_1_SPECIAL_CHARACTER.message)

        from ib_iam.adapters.service_adapter import ServiceAdapter
        service_adapter = ServiceAdapter()
        auth_service = service_adapter.auth_service

        # Assert
        from ib_iam.interactors.update_user_password_interactor import \
            PasswordAtLeastOneSpecialCharacter
        with pytest.raises(PasswordAtLeastOneSpecialCharacter):
            auth_service.update_user_password_with_reset_password_token(
                reset_password_token=reset_password_token,
                password=password
            )

        reset_password_for_given_user_password_reset_token_mock. \
            assert_called_once()

    def test_incorrect_password_for_password_min_length_raise_exception(
            self, mocker
    ):
        # Arrange
        reset_password_token = "string"
        password = "string123"
        reset_password_for_given_user_password_reset_token_mock = \
            self.reset_password_mock(mocker=mocker)

        from ib_users.constants.custom_exception_messages import \
            PASSWORD_MIN_LENGTH_IS
        from ib_users.validators.base_validator import CustomException
        from ib_iam.constants.config import REQUIRED_PASSWORD_MIN_LENGTH
        reset_password_for_given_user_password_reset_token_mock.side_effect \
            = CustomException(
            exception_type=PASSWORD_MIN_LENGTH_IS.code,
            message=PASSWORD_MIN_LENGTH_IS.message.format(
                val=REQUIRED_PASSWORD_MIN_LENGTH))

        from ib_iam.adapters.service_adapter import ServiceAdapter
        service_adapter = ServiceAdapter()
        auth_service = service_adapter.auth_service

        # Assert
        from ib_iam.interactors.update_user_password_interactor import \
            PasswordMinLength
        with pytest.raises(PasswordMinLength):
            auth_service.update_user_password_with_reset_password_token(
                reset_password_token=reset_password_token,
                password=password
            )

        reset_password_for_given_user_password_reset_token_mock. \
            assert_called_once()

    def test_with_token_does_not_exist_raise_exception(
            self, mocker
    ):
        # Arrange
        reset_password_token = "string"
        password = "string123"
        reset_password_for_given_user_password_reset_token_mock = \
            self.reset_password_mock(mocker=mocker)

        from ib_users.interactors.exceptions.user_credentials_exceptions import \
            InvalidTokenException
        reset_password_for_given_user_password_reset_token_mock.side_effect \
            = InvalidTokenException

        from ib_iam.adapters.service_adapter import ServiceAdapter
        service_adapter = ServiceAdapter()
        auth_service = service_adapter.auth_service

        # Assert
        from ib_iam.interactors.update_user_password_interactor import \
            TokenDoesNotExist
        with pytest.raises(TokenDoesNotExist):
            auth_service.update_user_password_with_reset_password_token(
                reset_password_token=reset_password_token,
                password=password
            )

        reset_password_for_given_user_password_reset_token_mock. \
            assert_called_once()

    def test_with_token_has_expired_raise_exception(
            self, mocker
    ):
        # Arrange
        reset_password_token = "string"
        password = "string123"
        reset_password_for_given_user_password_reset_token_mock = \
            self.reset_password_mock(mocker=mocker)

        from ib_users.interactors.exceptions.user_credentials_exceptions import \
            TokenExpiredException
        reset_password_for_given_user_password_reset_token_mock.side_effect \
            = TokenExpiredException

        from ib_iam.adapters.service_adapter import ServiceAdapter
        service_adapter = ServiceAdapter()
        auth_service = service_adapter.auth_service

        # Assert

        from ib_iam.interactors.update_user_password_interactor import \
            TokenHasExpired
        with pytest.raises(TokenHasExpired):
            auth_service.update_user_password_with_reset_password_token(
                reset_password_token=reset_password_token,
                password=password
            )
        reset_password_for_given_user_password_reset_token_mock. \
            assert_called_once()
