import pytest
from unittest.mock import patch, Mock


class TestLoginInteractor:

    @pytest.fixture()
    def presenter_mock_setup(self):
        from unittest.mock import create_autospec

        from ib_iam.interactors.presenter_interfaces. \
            presenter_interface import PresenterInterface
        presenter = create_autospec(PresenterInterface)
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
        "ib_iam.adapters.auth_service.AuthService.get_user_id_from_email_and_password_dto"
    )
    def test_validate_password_raise_exception(
            self, get_user_id_from_email_and_password_dto,
            email_and_password_dto, presenter_mock_setup
    ):
        # Arrange
        expected_raise_invalid_password_mock = Mock()

        from ib_iam.interactors.user_login_interactor import InvalidPassword
        get_user_id_from_email_and_password_dto.side_effect = InvalidPassword

        presenter_mock = presenter_mock_setup
        presenter_mock.raise_invalid_password.return_value \
            = expected_raise_invalid_password_mock

        from ib_iam.interactors.user_login_interactor import LoginInteractor
        interactor = LoginInteractor()

        # Act
        response = interactor.login_wrapper(
            email_and_password_dto=email_and_password_dto,
            presenter=presenter_mock)

        # Assert
        assert response == expected_raise_invalid_password_mock
        presenter_mock_setup.raise_invalid_password.assert_called_once()

    @patch(
        "ib_iam.adapters.auth_service.AuthService.get_user_id_from_email_and_password_dto")
    def test_validate_email_raise_exception(
            self, get_user_id_from_email_and_password_dto,
            email_and_password_dto, presenter_mock_setup
    ):
        # Arrange
        expected_raise_invalid_email_mock = Mock()

        from ib_iam.interactors.user_login_interactor import AccountDoesNotExist
        get_user_id_from_email_and_password_dto.side_effect \
            = AccountDoesNotExist

        presenter_mock = presenter_mock_setup
        presenter_mock.raise_invalid_email.return_value \
            = expected_raise_invalid_email_mock

        from ib_iam.interactors.user_login_interactor import LoginInteractor
        interactor = LoginInteractor()

        # Act
        response = interactor.login_wrapper(
            email_and_password_dto=email_and_password_dto,
            presenter=presenter_mock)

        # Assert
        assert response == expected_raise_invalid_email_mock
        presenter_mock_setup.raise_invalid_email.assert_called_once()

    @patch(
        "ib_iam.adapters.auth_service.AuthService.get_tokens_dto_from_user_id")
    @patch(
        "ib_iam.adapters.auth_service.AuthService.get_user_id_from_email_and_password_dto")
    def test_with_valid_email_and_password_dto(
            self, get_user_id_from_email_and_password_dto,
            get_tokens_dto_from_user_id, email_and_password_dto,
            presenter_mock_setup
    ):
        # Arrange
        user_id = 1
        from ib_iam.adapters.auth_service import TokensDTO
        tokens_dto = TokensDTO(
            access_token="asdfaldskfjdfdlsdkf",
            refresh_token="sadfenkljkdfeller",
            expires_in_seconds=1000
        )

        get_user_id_from_email_and_password_dto.return_value = user_id
        get_tokens_dto_from_user_id.return_value = tokens_dto

        expected_presenter_mock_response = Mock()
        presenter_mock = presenter_mock_setup
        presenter_mock.prepare_response_for_tokens_dto.return_value \
            = expected_presenter_mock_response

        from ib_iam.interactors.user_login_interactor import LoginInteractor
        interactor = LoginInteractor()

        # Act
        response = interactor.login_wrapper(
            email_and_password_dto=email_and_password_dto,
            presenter=presenter_mock)

        # Assert
        assert response == expected_presenter_mock_response
