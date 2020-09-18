"""
returns success response as the password updated successfully
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
    def test_case(self, mocker, api_user, snapshot):
        from ib_iam.tests.common_fixtures.adapters.auth_service_adapter_mocks import \
            update_user_password_mock
        update_user_password_mock(mocker)
        body = {'current_password': 'password@1', 'new_password': 'p@ssword#1'}
        path_params = {}
        query_params = {}
        headers = {}
        self.make_api_call(
            body=body, path_params=path_params, query_params=query_params,
            headers=headers, snapshot=snapshot
        )
