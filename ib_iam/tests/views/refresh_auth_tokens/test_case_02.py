"""
get refresh tokens
"""
import pytest
from django_swagger_utils.utils.test_utils import TestUtils
from ib_iam.tests.views.refresh_auth_tokens import APP_NAME, OPERATION_NAME, REQUEST_METHOD, URL_SUFFIX


class TestCase02RefreshTokensAPITestCase(TestUtils):
    APP_NAME = APP_NAME
    OPERATION_NAME = OPERATION_NAME
    REQUEST_METHOD = REQUEST_METHOD
    URL_SUFFIX = URL_SUFFIX
    SECURITY = {'oauth': {'scopes': ['write']}}

    @pytest.mark.django_db
    def test_with_valid_details_return_response(self, snapshot, mocker):
        access_token = "rNYAlle5thjiWD5MIt63GkhAws5suQ"
        refresh_token = "pNYAlle5thjiWD5MIt63GkhAws5suQ"

        from ib_iam.adapters.dtos import UserTokensDTO
        user_tokens_dto = UserTokensDTO(
            access_token='asdfaldskfjdfdlsdkf',
            refresh_token='sadfenkljkdfeller',
            expires_in_seconds=5647665599,
            user_id='11'
        )

        from ib_iam.tests.common_fixtures.adapters.auth_service_adapter_mocks \
            import get_refresh_auth_tokens_dto_mock
        get_refresh_auth_tokens_dto_mock = \
            get_refresh_auth_tokens_dto_mock(mocker)

        get_refresh_auth_tokens_dto_mock.return_value = user_tokens_dto

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
