"""
    valid email. Sent email to user account
"""
from unittest.mock import patch

import pytest
from django_swagger_utils.utils.test_v1 import TestUtils
from . import APP_NAME, OPERATION_NAME, REQUEST_METHOD, URL_SUFFIX


class TestCase03UserResetPasswordLinkAPITestCase(TestUtils):
    APP_NAME = APP_NAME
    OPERATION_NAME = OPERATION_NAME
    REQUEST_METHOD = REQUEST_METHOD
    URL_SUFFIX = URL_SUFFIX
    SECURITY = {'oauth': {'scopes': ['read']}}

    @patch(
        "ib_iam.adapters.email_service.EmailService.send_email_to_user"
    )
    @patch(
        "ib_iam.adapters.auth_service.AuthService.get_token_for_reset_password"
    )
    @pytest.mark.django_db
    def test_case(self, get_token_for_reset_password_mock,
                  send_email_to_user_mock, snapshot
                  ):
        body = {'email': 'test@gmail.com'}
        user_token = "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9"
        get_token_for_reset_password_mock.return_value \
            = user_token

        path_params = {}
        query_params = {}
        headers = {}
        response = self.default_test_case(
            body=body, path_params=path_params,
            query_params=query_params, headers=headers, snapshot=snapshot
        )
        get_token_for_reset_password_mock.assert_called_once()
        send_email_to_user_mock.assert_called_once()
