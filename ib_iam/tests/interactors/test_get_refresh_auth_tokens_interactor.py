from unittest.mock import Mock

import pytest


class TestGetRefreshTokensInteractor:

    @pytest.fixture()
    def presenter_mock(self):
        from unittest.mock import create_autospec
        from ib_iam.interactors.presenter_interfaces.get_refresh_auth_tokens_presenter_interface import \
            GetRefreshTokensPresenterInterface
        presenter = create_autospec(GetRefreshTokensPresenterInterface)
        return presenter

    @pytest.fixture()
    def interactor(self):
        from ib_iam.interactors.get_refresh_auth_tokens_interactor import \
            GetRefreshTokensInteractor
        interactor = GetRefreshTokensInteractor()
        return interactor

    def test_with_invalid_access_token_return_response(
            self, presenter_mock, interactor, mocker):
        # Arrange
        access_token = "rNYAlle5thjiWD5MIt63GkhAws5suQ"
        refresh_token = "pNYAlle5thjiWD5MIt63GkhAws5suQ"
        expected_response_for_access_token_not_found_mock = Mock()

        presenter_mock.response_for_access_token_not_found.return_value = \
            expected_response_for_access_token_not_found_mock

        from ib_iam.tests.common_fixtures.adapters.auth_service_adapter_mocks \
            import prepare_get_refresh_auth_tokens_dto_mock
        get_refresh_auth_tokens_dto_mock = \
            prepare_get_refresh_auth_tokens_dto_mock(mocker)

        from ib_iam.adapters.auth_service import AccessTokenNotFound
        get_refresh_auth_tokens_dto_mock.side_effect = AccessTokenNotFound

        # Act
        response = interactor.get_refresh_auth_tokens_wrapper(
            access_token=access_token, refresh_token=refresh_token,
            presenter=presenter_mock
        )

        # Assert
        assert response == expected_response_for_access_token_not_found_mock

        presenter_mock.response_for_access_token_not_found.assert_called_once()
        get_refresh_auth_tokens_dto_mock.assert_called_with(
            access_token=access_token, refresh_token=refresh_token
        )

    def test_with_refresh_token_expire_return_response(
            self, presenter_mock, interactor, mocker):
        # Arrange
        access_token = "rNYAlle5thjiWD5MIt63GkhAws5suQ"
        refresh_token = "pNYAlle5thjiWD5MIt63GkhAws5suQ"
        expected_response_for_refresh_token_expired_mock = Mock()

        presenter_mock.response_for_refresh_token_expired.return_value = \
            expected_response_for_refresh_token_expired_mock

        from ib_iam.tests.common_fixtures.adapters.auth_service_adapter_mocks \
            import prepare_get_refresh_auth_tokens_dto_mock
        get_refresh_auth_tokens_dto_mock = \
            prepare_get_refresh_auth_tokens_dto_mock(mocker)

        from ib_iam.adapters.auth_service import RefreshTokenHasExpired
        get_refresh_auth_tokens_dto_mock.side_effect = RefreshTokenHasExpired

        # Act
        response = interactor.get_refresh_auth_tokens_wrapper(
            access_token=access_token, refresh_token=refresh_token,
            presenter=presenter_mock
        )

        # Assert
        assert response == expected_response_for_refresh_token_expired_mock

        presenter_mock.response_for_refresh_token_expired.assert_called_once()
        get_refresh_auth_tokens_dto_mock.assert_called_with(
            access_token=access_token, refresh_token=refresh_token
        )

    def test_with_refresh_token_not_found_return_response(
            self, presenter_mock, interactor, mocker):
        # Arrange
        access_token = "rNYAlle5thjiWD5MIt63GkhAws5suQ"
        refresh_token = "pNYAlle5thjiWD5MIt63GkhAws5suQ"
        expected_response_for_refresh_token_not_found_mock = Mock()

        presenter_mock.response_for_refresh_token_not_found.return_value = \
            expected_response_for_refresh_token_not_found_mock

        from ib_iam.tests.common_fixtures.adapters.auth_service_adapter_mocks \
            import prepare_get_refresh_auth_tokens_dto_mock
        get_refresh_auth_tokens_dto_mock = \
            prepare_get_refresh_auth_tokens_dto_mock(mocker)

        from ib_iam.adapters.auth_service import RefreshTokenHasNotFound
        get_refresh_auth_tokens_dto_mock.side_effect = RefreshTokenHasNotFound

        # Act
        response = interactor.get_refresh_auth_tokens_wrapper(
            access_token=access_token, refresh_token=refresh_token,
            presenter=presenter_mock
        )

        # Assert
        assert response == expected_response_for_refresh_token_not_found_mock

        presenter_mock.response_for_refresh_token_not_found.assert_called_once()
        get_refresh_auth_tokens_dto_mock.assert_called_with(
            access_token=access_token, refresh_token=refresh_token
        )

    def test_with_user_account_not_found_return_response(
            self, presenter_mock, interactor, mocker):
        # Arrange
        access_token = "rNYAlle5thjiWD5MIt63GkhAws5suQ"
        refresh_token = "pNYAlle5thjiWD5MIt63GkhAws5suQ"
        expected_response_for_user_account_not_found_mock = Mock()

        presenter_mock.response_for_user_account_not_found.return_value = \
            expected_response_for_user_account_not_found_mock

        from ib_iam.tests.common_fixtures.adapters.auth_service_adapter_mocks \
            import prepare_get_refresh_auth_tokens_dto_mock
        get_refresh_auth_tokens_dto_mock = \
            prepare_get_refresh_auth_tokens_dto_mock(mocker)

        from ib_iam.adapters.auth_service import UserAccountNotFound
        get_refresh_auth_tokens_dto_mock.side_effect = UserAccountNotFound

        # Act
        response = interactor.get_refresh_auth_tokens_wrapper(
            access_token=access_token, refresh_token=refresh_token,
            presenter=presenter_mock
        )

        # Assert
        assert response == expected_response_for_user_account_not_found_mock

        presenter_mock.response_for_user_account_not_found.assert_called_once()
        get_refresh_auth_tokens_dto_mock.assert_called_with(
            access_token=access_token, refresh_token=refresh_token
        )

    def test_with_valid_details_return_response(
            self, presenter_mock, interactor, mocker):
        # Arrange
        access_token = "rNYAlle5thjiWD5MIt63GkhAws5suQ"
        refresh_token = "pNYAlle5thjiWD5MIt63GkhAws5suQ"

        from ib_iam.adapters.auth_service import UserTokensDTO
        user_tokens_dto = UserTokensDTO(
            access_token='asdfaldskfjdfdlsdkf',
            refresh_token='sadfenkljkdfeller',
            expires_in_seconds=5647665599,
            user_id='11'
        )

        expected_response_for_user_tokens_dto_mock = Mock()

        presenter_mock.response_for_user_tokens_dto.return_value = \
            expected_response_for_user_tokens_dto_mock

        from ib_iam.tests.common_fixtures.adapters.auth_service_adapter_mocks \
            import prepare_get_refresh_auth_tokens_dto_mock
        get_refresh_auth_tokens_dto_mock = \
            prepare_get_refresh_auth_tokens_dto_mock(mocker)
        get_refresh_auth_tokens_dto_mock.return_value = user_tokens_dto

        # Act
        response = interactor.get_refresh_auth_tokens_wrapper(
            access_token=access_token, refresh_token=refresh_token,
            presenter=presenter_mock
        )

        # Assert
        assert response == expected_response_for_user_tokens_dto_mock

        presenter_mock.response_for_user_tokens_dto.assert_called_once_with(
            user_tokens_dto=user_tokens_dto
        )
        get_refresh_auth_tokens_dto_mock.assert_called_with(
            access_token=access_token, refresh_token=refresh_token
        )
