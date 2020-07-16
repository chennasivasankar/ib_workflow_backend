from unittest.mock import Mock, patch

import pytest


class TestUpdateUserPasswordInteractor:
    @pytest.fixture()
    def presenter_mock(self):
        from unittest.mock import create_autospec
        from ib_iam.interactors.presenter_interfaces.presenter_interface import \
            AuthPresenterInterface
        presenter = create_autospec(AuthPresenterInterface)
        return presenter

    @patch(
        "ib_iam.adapters.auth_service.AuthService.update_user_password"
    )
    def test_with_token_which_does_not_exist_raise_exception(
            self, update_user_password_mock, presenter_mock
    ):
        # Arrange
        token = "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9"
        password = "sankar123"
        expected_presenter_token_does_not_exist_mock = Mock()

        from ib_iam.interactors.update_user_password_interactor import \
            TokenDoesNotExist
        update_user_password_mock.side_effect = TokenDoesNotExist

        presenter = presenter_mock
        presenter.raise_exception_for_token_does_not_exists.return_value \
            = expected_presenter_token_does_not_exist_mock
        from ib_iam.interactors.update_user_password_interactor import \
            UpdateUserPasswordInteractor
        interactor = UpdateUserPasswordInteractor()

        # Act
        response = interactor.update_user_password_wrapper(
            token=token, password=password, presenter=presenter
        )

        # Assert
        assert response == expected_presenter_token_does_not_exist_mock
        presenter.raise_exception_for_token_does_not_exists.assert_called_once()

    @patch(
        "ib_iam.adapters.auth_service.AuthService.update_user_password"
    )
    def test_with_weak_password_raise_exception(
            self, update_user_password_mock, presenter_mock
    ):
        # Arrange
        token = "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9"
        password = "sankar123"
        expected_presenter_raise_not_a_strong_password_mock = Mock()

        from ib_iam.interactors.update_user_password_interactor import \
            NotStrongPassword
        update_user_password_mock.side_effect = NotStrongPassword

        presenter = presenter_mock
        presenter.raise_exception_for_not_a_strong_password.return_value \
            = expected_presenter_raise_not_a_strong_password_mock
        from ib_iam.interactors.update_user_password_interactor import \
            UpdateUserPasswordInteractor
        interactor = UpdateUserPasswordInteractor()

        # Act
        response = interactor.update_user_password_wrapper(
            token=token, password=password, presenter=presenter
        )

        # Assert
        assert response == expected_presenter_raise_not_a_strong_password_mock
        presenter.raise_exception_for_not_a_strong_password.assert_called_once()

    @patch(
        "ib_iam.adapters.auth_service.AuthService.update_user_password"
    )
    def test_with_token_expired_raise_exception(
            self, update_user_password_mock, presenter_mock
    ):
        # Arrange
        token = "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9"
        password = "sankar123"
        expected_presenter_token_expired_mock = Mock()

        from ib_iam.interactors.update_user_password_interactor import \
            TokenHasExpired
        update_user_password_mock.side_effect = TokenHasExpired

        presenter = presenter_mock
        presenter.raise_exception_for_token_has_expired.return_value \
            = expected_presenter_token_expired_mock
        from ib_iam.interactors.update_user_password_interactor import \
            UpdateUserPasswordInteractor
        interactor = UpdateUserPasswordInteractor()

        # Act
        response = interactor.update_user_password_wrapper(
            token=token, password=password, presenter=presenter
        )

        # Assert
        assert response == expected_presenter_token_expired_mock
        presenter.raise_exception_for_token_has_expired.assert_called_once()

    @patch(
        "ib_iam.adapters.auth_service.AuthService.update_user_password"
    )
    def test_with_valid_details_update_password(
            self, update_user_password_mock, presenter_mock
    ):
        # Arrange
        token = "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9"
        password = "sankar123"
        expected_presenter_success_response_mock = Mock()

        presenter = presenter_mock
        presenter.get_update_user_password_success_response.return_value \
            = expected_presenter_success_response_mock
        from ib_iam.interactors.update_user_password_interactor import \
            UpdateUserPasswordInteractor
        interactor = UpdateUserPasswordInteractor()

        # Act
        response = interactor.update_user_password_wrapper(
            token=token, password=password, presenter=presenter
        )

        # Assert
        assert response == expected_presenter_success_response_mock
        presenter.get_update_user_password_success_response.assert_called_once()
