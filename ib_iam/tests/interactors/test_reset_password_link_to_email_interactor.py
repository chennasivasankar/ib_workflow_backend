from unittest.mock import Mock

import pytest


class TestSendResetPasswordLinkToEmailInteractor:

    @pytest.fixture()
    def presenter_mock(self):
        from unittest.mock import create_autospec
        from ib_iam.interactors.presenter_interfaces.auth_presenter_interface \
            import AuthPresenterInterface
        presenter = create_autospec(AuthPresenterInterface)
        return presenter

    def test_invalid_email_raise_exception(self, mocker, presenter_mock):
        # Arrange
        email = "ss"
        from ib_iam.exceptions.custom_exceptions import InvalidEmail
        from ib_iam.tests.common_fixtures.adapters.auth_service_adapter_mocks import \
            get_reset_password_token_mock
        get_reset_password_token_mock(mocker).side_effect = InvalidEmail
        expected_presenter_raise_invalid_email_mock = Mock()

        presenter_mock.raise_exception_for_invalid_email.return_value \
            = expected_presenter_raise_invalid_email_mock

        from ib_iam.interactors.reset_password_link_to_email_interactor import \
            SendResetPasswordLinkToEmailInteractor
        interactor = SendResetPasswordLinkToEmailInteractor()

        # Act
        response = interactor.send_reset_password_link_to_user_email_wrapper(
            email=email, presenter=presenter_mock
        )

        # Assert
        assert response == expected_presenter_raise_invalid_email_mock
        presenter_mock.raise_exception_for_invalid_email.assert_called_once()

    def test_user_account_does_not_exist_raise_exception(
            self, presenter_mock, mocker
    ):
        # Arrange
        email = "test@gmail.com"
        from ib_iam.exceptions.custom_exceptions import UserAccountDoesNotExist
        from ib_iam.tests.common_fixtures.adapters.auth_service_adapter_mocks import \
            get_reset_password_token_mock
        get_reset_password_token_mock(mocker).side_effect \
            = UserAccountDoesNotExist

        expected_presenter_raise_user_account_does_not_exist_mock = Mock()

        presenter_mock.raise_exception_for_user_account_does_not_exists. \
            return_value = expected_presenter_raise_user_account_does_not_exist_mock

        from ib_iam.interactors.reset_password_link_to_email_interactor import \
            SendResetPasswordLinkToEmailInteractor
        interactor = SendResetPasswordLinkToEmailInteractor()

        # Act
        response = interactor.send_reset_password_link_to_user_email_wrapper(
            email=email, presenter=presenter_mock
        )

        # Assert
        assert response \
               == expected_presenter_raise_user_account_does_not_exist_mock
        presenter_mock.raise_exception_for_user_account_does_not_exists. \
            assert_called_once()

    def test_with_valid_email_then_email_sent_to_user(
            self, presenter_mock, mocker
    ):
        # Arrange
        email = "test@gmail.com"
        user_reset_password_token = "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9"
        from ib_iam.tests.common_fixtures.adapters.auth_service_adapter_mocks import \
            get_reset_password_token_mock
        get_reset_password_token_mock(mocker).return_value \
            = user_reset_password_token

        from ib_iam.tests.common_fixtures.adapters.email_service_adapter_mocks import \
            send_email_to_user_mock

        send_email_to_user_mock = send_email_to_user_mock(mocker)

        expected_presenter_success_response_mock = Mock()

        presenter_mock. \
            get_success_response_for_reset_password_link_to_user_email.return_value \
            = expected_presenter_success_response_mock

        from ib_iam.interactors.reset_password_link_to_email_interactor import \
            SendResetPasswordLinkToEmailInteractor
        interactor = SendResetPasswordLinkToEmailInteractor()

        # Act
        response = interactor.send_reset_password_link_to_user_email_wrapper(
            email=email, presenter=presenter_mock
        )

        # Assert
        send_email_to_user_mock.assert_called_once()
        assert response == expected_presenter_success_response_mock
