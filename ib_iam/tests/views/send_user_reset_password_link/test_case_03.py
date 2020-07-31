"""
    valid email. Sent email to user account
"""
from unittest.mock import patch

import pytest
from django_swagger_utils.utils.test_v1 import TestUtils
from . import APP_NAME, OPERATION_NAME, REQUEST_METHOD, URL_SUFFIX


class TestCase03SendUserResetPasswordLinkAPITestCase(TestUtils):
    APP_NAME = APP_NAME
    OPERATION_NAME = OPERATION_NAME
    REQUEST_METHOD = REQUEST_METHOD
    URL_SUFFIX = URL_SUFFIX
    SECURITY = {'oauth': {'scopes': ['read']}}

    @pytest.mark.django_db
    def test_case(self, mocker, snapshot):
        body = {'email': 'test@gmail.com'}
        user_reset_password_token = "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9"
        from ib_iam.tests.common_fixtures.adapters.auth_service_adapter_mocks import \
            prepare_get_reset_password_token_mock
        get_reset_password_token_mock = prepare_get_reset_password_token_mock(mocker)
        get_reset_password_token_mock.return_value = user_reset_password_token

        from ib_iam.tests.common_fixtures.adapters.email_service_adapter_mocks import \
            prepare_send_email_to_user_mock

        send_email_to_user_mock = prepare_send_email_to_user_mock(mocker)

        path_params = {}
        query_params = {"token": user_reset_password_token}
        headers = {}
        response = self.default_test_case(
            body=body, path_params=path_params,
            query_params=query_params, headers=headers, snapshot=snapshot
        )
        get_reset_password_token_mock.assert_called_once()
        send_email_to_user_mock.assert_called_once()