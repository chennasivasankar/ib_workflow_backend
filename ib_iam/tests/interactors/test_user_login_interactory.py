import pytest
from unittest.mock import patch, Mock


class TestLoginInteractor:

    @pytest.fixture()
    def storage_mock_setup(self):
        from unittest.mock import create_autospec

        from ib_iam.interactors.storage_interfaces.storage_interface import \
            StorageInterface
        storage = create_autospec(StorageInterface)
        return storage

    @pytest.fixture()
    def presenter_mock_setup(self):
        from unittest.mock import create_autospec

        from ib_iam.interactors.presenter_interfaces.presenter_interface \
            import AuthPresenterInterface
        presenter = create_autospec(AuthPresenterInterface)
        return presenter

    @pytest.fixture()
    def email_and_password_dto(self):
        from ib_iam.adapters.auth_service import EmailAndPasswordDTO
        email_and_password_dto = EmailAndPasswordDTO(
            email="test#gamil.com",
            password="test123"
        )
        return email_and_password_dto

    @patch(
        "ib_iam.adapters.auth_service.AuthService.get_tokens_dto_for_given_email_and_password_dto"
    )
    def test_validate_incorrect_password_raise_exception(
            self, get_tokens_dto_for_given_email_and_password_dto_mock,
            email_and_password_dto, presenter_mock_setup, storage_mock_setup
    ):
        # Arrange
        expected_raise_incorrect_password_mock = Mock()

        from ib_iam.interactors.user_login_interactor import IncorrectPassword
        get_tokens_dto_for_given_email_and_password_dto_mock.side_effect \
            = IncorrectPassword

        presenter_mock = presenter_mock_setup
        presenter_mock.raise_exception_for_incorrect_password.return_value \
            = expected_raise_incorrect_password_mock

        from ib_iam.interactors.user_login_interactor import LoginInteractor
        interactor = LoginInteractor(storage=storage_mock_setup)

        # Act
        response = interactor.login_wrapper(
            email_and_password_dto=email_and_password_dto,
            presenter=presenter_mock)

        # Assert
        assert response == expected_raise_incorrect_password_mock
        presenter_mock_setup.raise_exception_for_incorrect_password. \
            assert_called_once()

    @patch(
        "ib_iam.adapters.auth_service.AuthService.get_tokens_dto_for_given_email_and_password_dto"
    )
    def test_validate_for_email_account_not_exist_raise_exception(
            self, get_tokens_dto_for_given_email_and_password_dto_mock,
            email_and_password_dto, presenter_mock_setup, storage_mock_setup
    ):
        # Arrange
        expected_presenter_raise_email_does_not_exist_mock = Mock()

        from ib_iam.exceptions.custom_exceptions import UserAccountDoesNotExist
        get_tokens_dto_for_given_email_and_password_dto_mock.side_effect \
            = UserAccountDoesNotExist

        presenter_mock = presenter_mock_setup
        presenter_mock.raise_exception_for_user_account_does_not_exists. \
            return_value = expected_presenter_raise_email_does_not_exist_mock

        from ib_iam.interactors.user_login_interactor import LoginInteractor
        interactor = LoginInteractor(storage=storage_mock_setup)

        # Act
        response = interactor.login_wrapper(
            email_and_password_dto=email_and_password_dto,
            presenter=presenter_mock
        )

        # Assert
        assert response == expected_presenter_raise_email_does_not_exist_mock
        presenter_mock_setup.raise_exception_for_user_account_does_not_exists. \
            assert_called_once()

    @patch(
        "ib_iam.adapters.auth_service.AuthService.get_tokens_dto_for_given_email_and_password_dto"
    )
    def test_with_valid_email_and_password_dto_return_response(
            self, get_tokens_dto_for_given_email_and_password_dto_mock,
            email_and_password_dto, presenter_mock_setup, storage_mock_setup
    ):
        # Arrange
        from ib_iam.adapters.auth_service import TokensDTO
        tokens_dto = TokensDTO(
            access_token="asdfaldskfjdfdlsdkf",
            refresh_token="sadfenkljkdfeller",
            expires_in_seconds=1000
        )
        email_and_password_dto.password = "Test12345@"
        email_and_password_dto.email = "test@gmail.com"

        get_tokens_dto_for_given_email_and_password_dto_mock.return_value \
            = tokens_dto

        expected_presenter_mock_response = Mock()
        presenter_mock = presenter_mock_setup
        presenter_mock.prepare_response_for_tokens_dto.return_value \
            = expected_presenter_mock_response

        from ib_iam.interactors.user_login_interactor import LoginInteractor
        interactor = LoginInteractor(storage=storage_mock_setup)

        # Act
        response = interactor.login_wrapper(
            email_and_password_dto=email_and_password_dto,
            presenter=presenter_mock)

        # Assert
        assert response == expected_presenter_mock_response

    @patch(
        "ib_iam.adapters.auth_service.AuthService.get_tokens_dto_for_given_email_and_password_dto"
    )
    def test_validate_invalid_email_raise_exception(
            self, get_tokens_dto_for_given_email_and_password_dto_mock,
            email_and_password_dto, presenter_mock_setup, storage_mock_setup
    ):
        # Arrange
        expected_raise_invalid_email_mock = Mock()

        from ib_iam.exceptions.custom_exceptions import InvalidEmail
        get_tokens_dto_for_given_email_and_password_dto_mock.side_effect \
            = InvalidEmail

        presenter_mock = presenter_mock_setup
        presenter_mock.raise_exception_for_invalid_email.return_value \
            = expected_raise_invalid_email_mock

        from ib_iam.interactors.user_login_interactor import LoginInteractor
        interactor = LoginInteractor(storage=storage_mock_setup)

        # Act
        response = interactor.login_wrapper(
            email_and_password_dto=email_and_password_dto,
            presenter=presenter_mock)

        # Assert
        assert response == expected_raise_invalid_email_mock
        presenter_mock_setup.raise_exception_for_invalid_email.assert_called_once()

    @patch(
        "ib_iam.adapters.auth_service.AuthService.get_tokens_dto_for_given_email_and_password_dto"
    )
    def test_validate_password_min_length_raise_exception(
            self, get_tokens_dto_for_given_email_and_password_dto_mock,
            email_and_password_dto, presenter_mock_setup, storage_mock_setup
    ):
        # Arrange
        expected_raise_password_min_length_mock = Mock()

        from ib_iam.interactors.user_login_interactor import \
            PasswordMinLength

        get_tokens_dto_for_given_email_and_password_dto_mock.side_effect \
            = PasswordMinLength

        presenter_mock = presenter_mock_setup
        presenter_mock.raise_exception_for_password_min_length_required. \
            return_value = expected_raise_password_min_length_mock

        from ib_iam.interactors.user_login_interactor import LoginInteractor
        interactor = LoginInteractor(storage=storage_mock_setup)

        # Act
        response = interactor.login_wrapper(
            email_and_password_dto=email_and_password_dto,
            presenter=presenter_mock)

        # Assert
        assert response == expected_raise_password_min_length_mock
        presenter_mock_setup.raise_exception_for_password_min_length_required. \
            assert_called_once()

    @patch(
        "ib_iam.adapters.auth_service.AuthService.get_tokens_dto_for_given_email_and_password_dto"
    )
    def test_validate_password_at_least_one_special_character_raise_exception(
            self, get_tokens_dto_for_given_email_and_password_dto_mock,
            email_and_password_dto, presenter_mock_setup, storage_mock_setup
    ):
        # Arrange
        expected_raise_password_at_least_one_special_character_mock = Mock()

        from ib_iam.interactors.user_login_interactor import \
            PasswordAtLeastOneSpecialCharacter

        get_tokens_dto_for_given_email_and_password_dto_mock.side_effect \
            = PasswordAtLeastOneSpecialCharacter

        presenter_mock = presenter_mock_setup
        presenter_mock.raise_exception_for_password_at_least_one_special_character_required. \
            return_value = expected_raise_password_at_least_one_special_character_mock

        from ib_iam.interactors.user_login_interactor import LoginInteractor
        interactor = LoginInteractor(storage=storage_mock_setup)

        # Act
        response = interactor.login_wrapper(
            email_and_password_dto=email_and_password_dto,
            presenter=presenter_mock)

        # Assert
        assert response \
               == expected_raise_password_at_least_one_special_character_mock
        presenter_mock_setup.raise_exception_for_password_at_least_one_special_character_required. \
            assert_called_once()
