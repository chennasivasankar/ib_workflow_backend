"""
update password
"""
import pytest
from django_swagger_utils.utils.test_utils import TestUtils

from . import APP_NAME, OPERATION_NAME, REQUEST_METHOD, URL_SUFFIX


class TestCase01UpdateUserPasswordAPITestCase(TestUtils):
    APP_NAME = APP_NAME
    OPERATION_NAME = OPERATION_NAME
    REQUEST_METHOD = REQUEST_METHOD
    URL_SUFFIX = URL_SUFFIX
    SECURITY = {'oauth': {'scopes': ['write']}}

    @pytest.mark.django_db
    def test_case(self, mocker, snapshot):
        from ib_iam.tests.common_fixtures.adapters.auth_service_adapter_mocks \
            import prepare_update_user_password_with_reset_password_token_mock
        prepare_update_user_password_with_reset_password_token_mock(mocker)
        body = {'password': 'string'}
        path_params = {}
        query_params = {'token': "735"}
        headers = {}
        response = self.make_api_call(
            body=body, path_params=path_params,
            query_params=query_params, headers=headers, snapshot=snapshot
        )
