from unittest.mock import Mock
import pytest


class TestResetUserPasswordInteractor:
    @pytest.fixture()
    def presenter_mock(self):
        from unittest.mock import create_autospec
        from ib_iam.interactors.presenter_interfaces.auth_presenter_interface import \
            AuthPresenterInterface
        presenter = create_autospec(AuthPresenterInterface)
        return presenter

    def test_with_token_which_does_not_exist_raise_exception(
            self, presenter_mock, mocker):
        # Arrange
        token = "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9"
        password = "sankar123"
        expected_presenter_token_does_not_exist_mock = Mock()

        from ib_iam.interactors.reset_user_password_interactor import \
            TokenDoesNotExist
        from ib_iam.tests.common_fixtures.adapters.auth_service_adapter_mocks import \
            prepare_update_user_password_with_reset_password_token_mock
        update_user_password_mock \
            = prepare_update_user_password_with_reset_password_token_mock(
            mocker)
        update_user_password_mock.side_effect = TokenDoesNotExist

        presenter = presenter_mock
        presenter.raise_exception_for_token_does_not_exists.return_value \
            = expected_presenter_token_does_not_exist_mock
        from ib_iam.interactors.reset_user_password_interactor import \
            ResetUserPasswordInteractor
        interactor = ResetUserPasswordInteractor()

        # Act
        response = interactor.reset_user_password_wrapper(
            reset_password_token=token, password=password, presenter=presenter
        )

        # Assert
        assert response == expected_presenter_token_does_not_exist_mock
        presenter.raise_exception_for_token_does_not_exists.assert_called_once()

    def test_with_token_expired_raise_exception(
            self, presenter_mock, mocker):
        # Arrange
        token = "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9"
        password = "sankar123"
        expected_presenter_token_expired_mock = Mock()

        from ib_iam.interactors.reset_user_password_interactor import \
            TokenHasExpired
        from ib_iam.tests.common_fixtures.adapters.auth_service_adapter_mocks import \
            prepare_update_user_password_with_reset_password_token_mock
        update_user_password_mock \
            = prepare_update_user_password_with_reset_password_token_mock(
            mocker)
        update_user_password_mock.side_effect = TokenHasExpired

        presenter = presenter_mock
        presenter.raise_exception_for_token_has_expired.return_value \
            = expected_presenter_token_expired_mock
        from ib_iam.interactors.reset_user_password_interactor import \
            ResetUserPasswordInteractor
        interactor = ResetUserPasswordInteractor()

        # Act
        response = interactor.reset_user_password_wrapper(
            reset_password_token=token, password=password, presenter=presenter)

        # Assert
        assert response == expected_presenter_token_expired_mock
        presenter.raise_exception_for_token_has_expired.assert_called_once()

    def test_with_valid_details_update_password(
            self, mocker, presenter_mock):
        # Arrange
        token = "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9"
        password = "sankar123"
        expected_presenter_success_response_mock = Mock()
        from ib_iam.tests.common_fixtures.adapters.auth_service_adapter_mocks import \
            prepare_update_user_password_with_reset_password_token_mock
        update_user_password_mock \
            = prepare_update_user_password_with_reset_password_token_mock(
            mocker)
        presenter = presenter_mock
        presenter.get_update_user_password_success_response.return_value \
            = expected_presenter_success_response_mock
        from ib_iam.interactors.reset_user_password_interactor import \
            ResetUserPasswordInteractor
        interactor = ResetUserPasswordInteractor()

        # Act
        response = interactor.reset_user_password_wrapper(
            reset_password_token=token, password=password, presenter=presenter)

        # Assert
        assert response == expected_presenter_success_response_mock
        presenter.get_update_user_password_success_response.assert_called_once()
        update_user_password_mock.assert_called_once()

    def test_validate_password_min_length_raise_exception(
            self, mocker, presenter_mock):
        # Arrange
        expected_raise_password_min_length_mock = Mock()
        token = "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9"
        password = "sankar123"

        from ib_iam.interactors.reset_user_password_interactor import \
            PasswordMinLength
        from ib_iam.tests.common_fixtures.adapters.auth_service_adapter_mocks import \
            prepare_update_user_password_with_reset_password_token_mock
        update_user_password_mock \
            = prepare_update_user_password_with_reset_password_token_mock(
            mocker)
        update_user_password_mock.side_effect \
            = PasswordMinLength

        presenter_mock = presenter_mock
        presenter_mock.raise_exception_for_password_min_length_required. \
            return_value = expected_raise_password_min_length_mock

        from ib_iam.interactors.reset_user_password_interactor import \
            ResetUserPasswordInteractor
        interactor = ResetUserPasswordInteractor()

        # Act
        response = interactor.reset_user_password_wrapper(
            reset_password_token=token, password=password,
            presenter=presenter_mock)

        # Assert
        assert response == expected_raise_password_min_length_mock
        presenter_mock.raise_exception_for_password_min_length_required. \
            assert_called_once()

    def test_validate_password_at_least_one_special_character_raise_exception(
            self, mocker, presenter_mock):
        # Arrange
        expected_raise_password_at_least_one_special_character_mock = Mock()
        token = "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9"
        password = "sankar123"
        from ib_iam.interactors.reset_user_password_interactor import \
            PasswordAtLeastOneSpecialCharacter
        from ib_iam.tests.common_fixtures.adapters.auth_service_adapter_mocks import \
            prepare_update_user_password_with_reset_password_token_mock
        update_user_password_mock \
            = prepare_update_user_password_with_reset_password_token_mock(
            mocker)
        update_user_password_mock.side_effect \
            = PasswordAtLeastOneSpecialCharacter

        presenter_mock = presenter_mock
        presenter_mock.raise_exception_for_password_at_least_one_special_character_required. \
            return_value = expected_raise_password_at_least_one_special_character_mock

        from ib_iam.interactors.reset_user_password_interactor import \
            ResetUserPasswordInteractor
        interactor = ResetUserPasswordInteractor()

        # Act
        response = interactor.reset_user_password_wrapper(
            reset_password_token=token, password=password,
            presenter=presenter_mock)

        # Assert
        assert response \
               == expected_raise_password_at_least_one_special_character_mock
        presenter_mock.raise_exception_for_password_at_least_one_special_character_required. \
            assert_called_once()
