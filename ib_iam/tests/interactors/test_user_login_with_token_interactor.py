from unittest import mock

import pytest


class TestLoginInteractor:

    @pytest.fixture()
    def storage_mock(self):
        from unittest.mock import create_autospec

        from ib_iam.interactors.storage_interfaces.user_storage_interface import \
            UserStorageInterface
        storage = create_autospec(UserStorageInterface)
        return storage

    @pytest.fixture()
    def presenter_mock(self):
        from unittest.mock import create_autospec

        from ib_iam.interactors.presenter_interfaces.auth_presenter_interface import \
            LoginWithUserTokePresenterInterface
        presenter = create_autospec(LoginWithUserTokePresenterInterface)
        return presenter

    @pytest.fixture
    def interactor_mock(self, storage_mock):
        from ib_iam.interactors.auth.user_login_interactor import \
            LoginInteractor
        return LoginInteractor(storage=storage_mock)

    def test_given_valid_token_returns_success_response(
            self, interactor_mock, storage_mock, presenter_mock, mocker
    ):
        # Arrange
        from django.conf import settings
        from ib_iam.tests.common_fixtures.adapters \
            .auth_service_adapter_mocks import create_auth_tokens_for_user_mock
        from ib_iam.tests.factories.adapter_dtos import UserTokensDTOFactory
        token = "user_token"
        is_admin = True
        user_id = "user_id_1"
        expiry_in_seconds = settings.USER_VERIFICATION_EMAIL_EXPIRY_IN_SECONDS
        user_tokens_dto = UserTokensDTOFactory(user_id=user_id)
        storage_mock.get_user_id_for_given_token.return_value = user_id
        storage_mock.is_user_admin.return_value = is_admin
        create_auth_tokens_for_user_mock = create_auth_tokens_for_user_mock(
            mocker=mocker
        )
        create_auth_tokens_for_user_mock.return_value = user_tokens_dto
        mock_object = mock.Mock
        presenter_mock.prepare_response_for_user_tokens_dto_and_is_admin \
            .return_value = mock_object

        # Act
        response = interactor_mock.login_with_token_wrapper(
            token=token, presenter=presenter_mock
        )

        # Assert
        assert response == mock_object
        storage_mock.get_user_id_for_given_token.assert_called_once_with(
            token=token
        )
        storage_mock.is_user_admin.assert_called_once_with(
            user_id=user_id
        )
        create_auth_tokens_for_user_mock.assert_called_once_with(
            user_id=user_id, expiry_in_seconds=expiry_in_seconds
        )
        presenter_mock.prepare_response_for_user_tokens_dto_and_is_admin \
            .assert_called_once_with(
            tokens_dto=user_tokens_dto, is_admin=is_admin
        )
