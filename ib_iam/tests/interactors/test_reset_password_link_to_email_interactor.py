from unittest.mock import Mock, patch

import pytest


class TestResetPasswordLinkToEmailInteractor:

    @pytest.fixture()
    def presenter_mock(self):
        from unittest.mock import create_autospec
        from ib_iam.interactors.presenter_interfaces.presenter_interface \
            import AuthPresenterInterface
        presenter = create_autospec(AuthPresenterInterface)
        return presenter

    def test_invalid_email_raise_exception(self, presenter_mock):
        # Arrange
        email = ""
        expected_presenter_raise_invalid_email_mock = Mock()

        presenter_mock.raise_invalid_email.return_value \
            = expected_presenter_raise_invalid_email_mock

        from ib_iam.interactors.rest_password_link_to_email_interactor import \
            ResetPasswordLinkToEmailInteractor
        interactor = ResetPasswordLinkToEmailInteractor()

        # Act
        response = interactor.reset_password_link_to_user_email_wrapper(
            email=email, presenter=presenter_mock
        )

        # Assert
        assert response == expected_presenter_raise_invalid_email_mock
        presenter_mock.raise_invalid_email.assert_called_once()

    @patch(
        "ib_iam.adapters.auth_service.AuthService.get_token_for_reset_password"
    )
    def test_user_account_does_not_exist_raise_exception(
            self, get_token_for_reset_password_mock, presenter_mock
        ):
        # Arrange
        email = "test@gmail.com"
        from ib_iam.interactors.rest_password_link_to_email_interactor import \
            UserAccountDoesNotExist
        get_token_for_reset_password_mock.side_effect \
            = UserAccountDoesNotExist()

        expected_presenter_raise_user_account_does_not_exist_mock = Mock()

        presenter_mock.raise_user_account_does_not_exist.return_value \
            = expected_presenter_raise_user_account_does_not_exist_mock

        from ib_iam.interactors.rest_password_link_to_email_interactor import \
            ResetPasswordLinkToEmailInteractor
        interactor = ResetPasswordLinkToEmailInteractor()

        # Act
        response = interactor.reset_password_link_to_user_email_wrapper(
            email=email, presenter=presenter_mock
        )

        # Assert
        assert response \
               == expected_presenter_raise_user_account_does_not_exist_mock
        presenter_mock.raise_user_account_does_not_exist.assert_called_once()

    @patch(
        "ib_iam.adapters.email_service.EmailService.send_email_to_user"
    )
    @patch(
        "ib_iam.adapters.auth_service.AuthService.get_token_for_reset_password"
    )
    def test_with_valid_email_then_email_sent_to_user(
            self, get_token_for_reset_password_mock, send_email_to_user_mock,
            presenter_mock
    ):
        # Arrange
        email = "test@gmail.com"
        user_token = "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9"
        get_token_for_reset_password_mock.return_value \
            = user_token

        expected_presenter_success_response_mock = Mock()

        presenter_mock.\
            get_success_response_for_reset_password_link_to_user_email.return_value \
            = expected_presenter_success_response_mock

        from ib_iam.interactors.rest_password_link_to_email_interactor import \
            ResetPasswordLinkToEmailInteractor
        interactor = ResetPasswordLinkToEmailInteractor()

        # Act
        response = interactor.reset_password_link_to_user_email_wrapper(
            email=email, presenter=presenter_mock
        )

        # Assert
        send_email_to_user_mock.assert_called_once()
        assert response == expected_presenter_success_response_mock
