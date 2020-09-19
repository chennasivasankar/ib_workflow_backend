import pytest
from freezegun import freeze_time


class TestGetUserTokens:

    @staticmethod
    def get_user_auth_tokens_mock(mocker):
        mock = mocker.patch(
            "ib_users.interfaces.service_interface.ServiceInterface.get_user_auth_tokens_for_login_with_email_and_password"
        )
        return mock

    @freeze_time("2020-01-14 12:00:01")
    def test_get_user_tokens_dto_for_given_email_and_password_dto(
            self, mocker
    ):
        # Arrange
        from ib_iam.adapters.dtos import EmailAndPasswordDTO
        email_and_password_dto = EmailAndPasswordDTO(
            email="test@gmail.com",
            password="test123"
        )
        get_user_auth_tokens_for_login_with_email_and_password_mock = \
            self.get_user_auth_tokens_mock(mocker=mocker)

        from ib_users.interactors.third_party.user_tokens_generator import \
            UserAuthTokensDTO

        # TODO: UserAuthDTO in ib_users expecting the expires_in is datetime but working for integers
        user_auth_tokens_dto = UserAuthTokensDTO(
            access_token="asdfaldskfjdfdlsdkf",
            refresh_token="sadfenkljkdfeller",
            expires_in=5647665599,
            user_id="11"
        )

        from ib_iam.adapters.dtos import UserTokensDTO
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
        get_user_auth_tokens_for_login_with_email_and_password_mock. \
            assert_called_once_with(
            email=email_and_password_dto.email,
            password=email_and_password_dto.password
        )

    # TODO: use assert_called_once_with to assert with parameters
    def test_with_invalid_email_raise_exception(
            self, mocker
    ):
        # Arrange
        from ib_iam.adapters.dtos import EmailAndPasswordDTO
        email_and_password_dto = EmailAndPasswordDTO(
            email="test@gmail.com",
            password="test123"
        )
        get_user_auth_tokens_for_login_with_email_and_password_mock = \
            self.get_user_auth_tokens_mock(mocker=mocker)

        from ib_users.constants.custom_exception_messages import INVALID_EMAIL
        from ib_users.validators.base_validator import CustomException
        get_user_auth_tokens_for_login_with_email_and_password_mock.side_effect \
            = CustomException(exception_type=INVALID_EMAIL.code,
                              message=INVALID_EMAIL.message)

        from ib_iam.adapters.service_adapter import ServiceAdapter
        service_adapter = ServiceAdapter()
        auth_service = service_adapter.auth_service

        # Assert
        from ib_iam.exceptions.custom_exceptions import InvalidEmail
        with pytest.raises(InvalidEmail):
            auth_service.get_user_tokens_dto_for_given_email_and_password_dto(
                email_and_password_dto=email_and_password_dto
            )
        get_user_auth_tokens_for_login_with_email_and_password_mock. \
            assert_called_once_with(
            email=email_and_password_dto.email,
            password=email_and_password_dto.password
        )

    def test_incorrect_password_for_password_at_least_one_special_character_raise_exception(
            self, mocker
    ):
        # Arrange
        from ib_iam.adapters.dtos import EmailAndPasswordDTO
        email_and_password_dto = EmailAndPasswordDTO(
            email="test@gmail.com",
            password="test123"
        )
        get_user_auth_tokens_for_login_with_email_and_password_mock = \
            self.get_user_auth_tokens_mock(mocker=mocker)

        from ib_users.constants.custom_exception_messages import \
            PASSWORD_AT_LEAST_1_SPECIAL_CHARACTER
        from ib_users.validators.base_validator import CustomException
        get_user_auth_tokens_for_login_with_email_and_password_mock.side_effect \
            = CustomException(
            exception_type=PASSWORD_AT_LEAST_1_SPECIAL_CHARACTER.code,
            message=PASSWORD_AT_LEAST_1_SPECIAL_CHARACTER.message)

        from ib_iam.adapters.service_adapter import ServiceAdapter
        service_adapter = ServiceAdapter()
        auth_service = service_adapter.auth_service

        # Assert
        from ib_iam.interactors.auth.user_login_interactor import IncorrectPassword
        with pytest.raises(IncorrectPassword):
            auth_service.get_user_tokens_dto_for_given_email_and_password_dto(
                email_and_password_dto=email_and_password_dto
            )
        get_user_auth_tokens_for_login_with_email_and_password_mock. \
            assert_called_once_with(
            email=email_and_password_dto.email,
            password=email_and_password_dto.password
        )

    def test_incorrect_password_for_password_min_length_raise_exception(
            self, mocker
    ):
        # Arrange
        from ib_iam.adapters.dtos import EmailAndPasswordDTO
        email_and_password_dto = EmailAndPasswordDTO(
            email="test@gmail.com",
            password="test123"
        )
        get_user_auth_tokens_for_login_with_email_and_password_mock = \
            self.get_user_auth_tokens_mock(mocker=mocker)

        from ib_users.constants.custom_exception_messages import \
            PASSWORD_MIN_LENGTH_IS
        from ib_users.validators.base_validator import CustomException
        from ib_iam.constants.config import REQUIRED_PASSWORD_MIN_LENGTH
        get_user_auth_tokens_for_login_with_email_and_password_mock.side_effect \
            = CustomException(
            exception_type=PASSWORD_MIN_LENGTH_IS.code,
            message=PASSWORD_MIN_LENGTH_IS.message.format(
                val=REQUIRED_PASSWORD_MIN_LENGTH))

        from ib_iam.adapters.service_adapter import ServiceAdapter
        service_adapter = ServiceAdapter()
        auth_service = service_adapter.auth_service

        # Assert
        from ib_iam.interactors.auth.user_login_interactor import IncorrectPassword
        with pytest.raises(IncorrectPassword):
            auth_service.get_user_tokens_dto_for_given_email_and_password_dto(
                email_and_password_dto=email_and_password_dto
            )
        get_user_auth_tokens_for_login_with_email_and_password_mock. \
            assert_called_once_with(
            email=email_and_password_dto.email,
            password=email_and_password_dto.password
        )

    def test_user_account_does_not_exist_raise_exception(
            self, mocker
    ):
        # Arrange
        from ib_iam.adapters.dtos import EmailAndPasswordDTO
        email_and_password_dto = EmailAndPasswordDTO(
            email="test@gmail.com",
            password="test123"
        )
        get_user_auth_tokens_for_login_with_email_and_password_mock = \
            self.get_user_auth_tokens_mock(mocker=mocker)

        from ib_users.constants.custom_exception_messages import \
            USER_ACCOUNT_IS_DEACTIVATED
        from ib_users.validators.base_validator import CustomException
        get_user_auth_tokens_for_login_with_email_and_password_mock.side_effect \
            = CustomException(
            exception_type=USER_ACCOUNT_IS_DEACTIVATED.code,
            message=USER_ACCOUNT_IS_DEACTIVATED.message)

        from ib_iam.adapters.service_adapter import ServiceAdapter
        service_adapter = ServiceAdapter()
        auth_service = service_adapter.auth_service

        # Assert
        from ib_iam.exceptions.custom_exceptions import UserAccountDoesNotExist
        with pytest.raises(UserAccountDoesNotExist):
            auth_service.get_user_tokens_dto_for_given_email_and_password_dto(
                email_and_password_dto=email_and_password_dto
            )
        get_user_auth_tokens_for_login_with_email_and_password_mock. \
            assert_called_once_with(
            email=email_and_password_dto.email,
            password=email_and_password_dto.password
        )

    def test_user_account_not_registered_raise_exception(
            self, mocker
    ):
        # Arrange
        from ib_iam.adapters.dtos import EmailAndPasswordDTO
        email_and_password_dto = EmailAndPasswordDTO(
            email="test@gmail.com",
            password="test123"
        )
        get_user_auth_tokens_for_login_with_email_and_password_mock = \
            self.get_user_auth_tokens_mock(mocker=mocker)

        from ib_users.validators.base_validator import CustomException
        from ib_users.exceptions.custom_exception_constants import \
            NOT_REGISTERED_USER
        get_user_auth_tokens_for_login_with_email_and_password_mock.side_effect \
            = CustomException(
            exception_type=NOT_REGISTERED_USER.code,
            message=NOT_REGISTERED_USER.message)

        from ib_iam.adapters.service_adapter import ServiceAdapter
        service_adapter = ServiceAdapter()
        auth_service = service_adapter.auth_service

        # Assert
        from ib_iam.exceptions.custom_exceptions import UserAccountDoesNotExist
        with pytest.raises(UserAccountDoesNotExist):
            auth_service.get_user_tokens_dto_for_given_email_and_password_dto(
                email_and_password_dto=email_and_password_dto
            )
        get_user_auth_tokens_for_login_with_email_and_password_mock. \
            assert_called_once_with(
            email=email_and_password_dto.email,
            password=email_and_password_dto.password
        )

    def test_with_incorrect_password_then_raise_exception(
            self, mocker
    ):
        # Arrange
        from ib_iam.adapters.dtos import EmailAndPasswordDTO
        email_and_password_dto = EmailAndPasswordDTO(
            email="test@gmail.com",
            password="test123"
        )
        get_user_auth_tokens_for_login_with_email_and_password_mock = \
            self.get_user_auth_tokens_mock(mocker=mocker)

        from ib_users.exceptions.custom_exception_constants import \
            INCORRECT_PASSWORD
        from ib_users.validators.base_validator import CustomException
        get_user_auth_tokens_for_login_with_email_and_password_mock.side_effect \
            = CustomException(
            exception_type=INCORRECT_PASSWORD.code,
            message=INCORRECT_PASSWORD.message)

        from ib_iam.adapters.service_adapter import ServiceAdapter
        service_adapter = ServiceAdapter()
        auth_service = service_adapter.auth_service

        # Assert
        from ib_iam.interactors.auth.user_login_interactor import IncorrectPassword
        with pytest.raises(IncorrectPassword):
            auth_service.get_user_tokens_dto_for_given_email_and_password_dto(
                email_and_password_dto=email_and_password_dto
            )
        get_user_auth_tokens_for_login_with_email_and_password_mock. \
            assert_called_once_with(
            email=email_and_password_dto.email,
            password=email_and_password_dto.password
        )
