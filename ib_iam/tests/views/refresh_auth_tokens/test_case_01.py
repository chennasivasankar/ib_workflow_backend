"""
All exceptions
"""
import pytest
from django_swagger_utils.utils.test_utils import TestUtils

from ib_iam.tests.views.refresh_auth_tokens import APP_NAME, OPERATION_NAME, \
    REQUEST_METHOD, URL_SUFFIX


class TestCase01RefreshTokensAPITestCase(TestUtils):
    APP_NAME = APP_NAME
    OPERATION_NAME = OPERATION_NAME
    REQUEST_METHOD = REQUEST_METHOD
    URL_SUFFIX = URL_SUFFIX
    SECURITY = {'oauth': {'scopes': ['write']}}

    @pytest.mark.django_db
    def test_with_invalid_access_token_return_response(self, snapshot, mocker):
        access_token = "rNYAlle5thjiWD5MIt63GkhAws5suQ"
        refresh_token = "pNYAlle5thjiWD5MIt63GkhAws5suQ"

        from ib_iam.tests.common_fixtures.adapters.auth_service_adapter_mocks \
            import get_refresh_auth_tokens_dto_mock
        get_refresh_auth_tokens_dto_mock = \
            get_refresh_auth_tokens_dto_mock(mocker)

        from ib_iam.adapters.auth_service import AccessTokenNotFound
        get_refresh_auth_tokens_dto_mock.side_effect = AccessTokenNotFound

        body = {
            'access_token': access_token,
            'refresh_token': refresh_token
        }
        path_params = {}
        query_params = {}
        headers = {}
        self.make_api_call(body=body,
                                      path_params=path_params,
                                      query_params=query_params,
                                      headers=headers,
                                      snapshot=snapshot)

    @pytest.mark.django_db
    def test_with_refresh_token_expire_return_response(self, snapshot, mocker):
        access_token = "rNYAlle5thjiWD5MIt63GkhAws5suQ"
        refresh_token = "pNYAlle5thjiWD5MIt63GkhAws5suQ"

        from ib_iam.tests.common_fixtures.adapters.auth_service_adapter_mocks \
            import get_refresh_auth_tokens_dto_mock
        get_refresh_auth_tokens_dto_mock = \
            get_refresh_auth_tokens_dto_mock(mocker)

        from ib_iam.adapters.auth_service import RefreshTokenHasExpired
        get_refresh_auth_tokens_dto_mock.side_effect = RefreshTokenHasExpired

        body = {
            'access_token': access_token,
            'refresh_token': refresh_token
        }
        path_params = {}
        query_params = {}
        headers = {}
        self.make_api_call(body=body,
                                      path_params=path_params,
                                      query_params=query_params,
                                      headers=headers,
                                      snapshot=snapshot)

    @pytest.mark.django_db
    def test_with_refresh_token_not_found_return_response(self, snapshot,
                                                          mocker):
        access_token = "rNYAlle5thjiWD5MIt63GkhAws5suQ"
        refresh_token = "pNYAlle5thjiWD5MIt63GkhAws5suQ"

        from ib_iam.tests.common_fixtures.adapters.auth_service_adapter_mocks \
            import get_refresh_auth_tokens_dto_mock
        get_refresh_auth_tokens_dto_mock = \
            get_refresh_auth_tokens_dto_mock(mocker)

        from ib_iam.adapters.auth_service import RefreshTokenHasNotFound
        get_refresh_auth_tokens_dto_mock.side_effect = RefreshTokenHasNotFound

        body = {
            'access_token': access_token,
            'refresh_token': refresh_token
        }
        path_params = {}
        query_params = {}
        headers = {}
        self.make_api_call(body=body,
                                      path_params=path_params,
                                      query_params=query_params,
                                      headers=headers,
                                      snapshot=snapshot)

    @pytest.mark.django_db
    def test_with_user_account_not_found_return_response(self, snapshot,
                                                         mocker):
        access_token = "rNYAlle5thjiWD5MIt63GkhAws5suQ"
        refresh_token = "pNYAlle5thjiWD5MIt63GkhAws5suQ"

        from ib_iam.tests.common_fixtures.adapters.auth_service_adapter_mocks \
            import get_refresh_auth_tokens_dto_mock
        get_refresh_auth_tokens_dto_mock = \
            get_refresh_auth_tokens_dto_mock(mocker)

        from ib_iam.adapters.auth_service import UserAccountNotFound
        get_refresh_auth_tokens_dto_mock.side_effect = UserAccountNotFound

        body = {
            'access_token': access_token,
            'refresh_token': refresh_token
        }
        path_params = {}
        query_params = {}
        headers = {}
        self.make_api_call(body=body,
                                      path_params=path_params,
                                      query_params=query_params,
                                      headers=headers,
                                      snapshot=snapshot)
