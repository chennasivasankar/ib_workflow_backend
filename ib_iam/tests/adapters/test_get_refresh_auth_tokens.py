import pytest


class TestGetRefreshAuthTokens:

    @staticmethod
    def prepare_get_refresh_auth_tokens_mock(mocker):
        mock = mocker.patch(
            "ib_users.interfaces.service_interface.ServiceInterface.refresh_auth_tokens"
        )
        return mock

    def test_with_access_token_not_found_raise_exception(self, mocker):
        # Arrange
        access_token = "rNYAlle5thjiWD5MIt63GkhAws5suQ"
        refresh_token = "pNYAlle5thjiWD5MIt63GkhAws5suQ"

        get_refresh_tokens_mock = self.prepare_get_refresh_auth_tokens_mock(
            mocker=mocker)
        from django_swagger_utils.drf_server.exceptions import NotFound

        from ib_users.constants.custom_exception_messages import \
            INVALID_ACCESS_TOKEN
        get_refresh_tokens_mock.side_effect = NotFound(
            message=INVALID_ACCESS_TOKEN.message,
            res_status=INVALID_ACCESS_TOKEN.code
        )

        from ib_iam.adapters.service_adapter import ServiceAdapter
        service_adapter = ServiceAdapter()

        # Assert
        from ib_iam.adapters.auth_service import AccessTokenNotFound
        with pytest.raises(AccessTokenNotFound):
            service_adapter.auth_service.get_refresh_auth_tokens_dto(
                access_token=access_token, refresh_token=refresh_token
            )

    def test_with_user_account_not_found_raise_exception(self, mocker):
        # Arrange
        access_token = "rNYAlle5thjiWD5MIt63GkhAws5suQ"
        refresh_token = "pNYAlle5thjiWD5MIt63GkhAws5suQ"

        get_refresh_tokens_mock = self.prepare_get_refresh_auth_tokens_mock(
            mocker=mocker)
        from ib_users.validators.base_validator import CustomException

        from ib_users.constants.custom_exception_messages import \
            USER_ACCOUNT_IS_DEACTIVATED
        get_refresh_tokens_mock.side_effect = CustomException(
            exception_type=USER_ACCOUNT_IS_DEACTIVATED.code,
            message=USER_ACCOUNT_IS_DEACTIVATED.message
        )

        from ib_iam.adapters.service_adapter import ServiceAdapter
        service_adapter = ServiceAdapter()

        # Assert
        from ib_iam.adapters.auth_service import UserAccountNotFound
        with pytest.raises(UserAccountNotFound):
            service_adapter.auth_service.get_refresh_auth_tokens_dto(
                access_token=access_token, refresh_token=refresh_token
            )

    def test_with_refresh_token_has_expired_raise_exception(self, mocker):
        # Arrange
        access_token = "rNYAlle5thjiWD5MIt63GkhAws5suQ"
        refresh_token = "pNYAlle5thjiWD5MIt63GkhAws5suQ"

        get_refresh_tokens_mock = self.prepare_get_refresh_auth_tokens_mock(
            mocker=mocker)
        from ib_users.exceptions.oauth2_exceptions import RefreshTokenExpired
        get_refresh_tokens_mock.side_effect = RefreshTokenExpired

        from ib_iam.adapters.service_adapter import ServiceAdapter
        service_adapter = ServiceAdapter()

        # Assert
        from ib_iam.adapters.auth_service import RefreshTokenHasExpired
        with pytest.raises(RefreshTokenHasExpired):
            service_adapter.auth_service.get_refresh_auth_tokens_dto(
                access_token=access_token, refresh_token=refresh_token
            )

    def test_with_refresh_token_not_found_raise_exception(self, mocker):
        # Arrange
        access_token = "rNYAlle5thjiWD5MIt63GkhAws5suQ"
        refresh_token = "pNYAlle5thjiWD5MIt63GkhAws5suQ"

        get_refresh_tokens_mock = self.prepare_get_refresh_auth_tokens_mock(
            mocker=mocker)
        from ib_users.exceptions.oauth2_exceptions import RefreshTokenNotFound
        get_refresh_tokens_mock.side_effect = RefreshTokenNotFound

        from ib_iam.adapters.service_adapter import ServiceAdapter
        service_adapter = ServiceAdapter()

        # Assert
        from ib_iam.adapters.auth_service import RefreshTokenHasNotFound
        with pytest.raises(RefreshTokenHasNotFound):
            service_adapter.auth_service.get_refresh_auth_tokens_dto(
                access_token=access_token, refresh_token=refresh_token
            )

    def test_with_valid_details_return_response(self, mocker):
        # Arrange
        access_token = "rNYAlle5thjiWD5MIt63GkhAws5suQ"
        refresh_token = "pNYAlle5thjiWD5MIt63GkhAws5suQ"
        from ib_users.interactors.third_party.user_tokens_generator import \
            UserAuthTokensDTO
        user_auth_tokens_dto = UserAuthTokensDTO(
            access_token="asdfaldskfjdfdlsdkf",
            refresh_token="sadfenkljkdfeller",
            expires_in=5647665599,
            user_id="11"
        )

        from ib_iam.tests.factories.adapter_dtos import UserTokensDTOFactory
        expected_user_tokens_dto = UserTokensDTOFactory(
            access_token='asdfaldskfjdfdlsdkf',
            refresh_token='sadfenkljkdfeller',
            expires_in_seconds=5647665599,
            user_id='11'
        )

        get_refresh_tokens_mock = self.prepare_get_refresh_auth_tokens_mock(
            mocker=mocker)
        get_refresh_tokens_mock.return_value = user_auth_tokens_dto

        from ib_iam.adapters.service_adapter import ServiceAdapter
        service_adapter = ServiceAdapter()

        # Act
        response = service_adapter.auth_service.get_refresh_auth_tokens_dto(
            access_token=access_token, refresh_token=refresh_token
        )

        # Assert
        assert response == expected_user_tokens_dto
