"""
    Invalid Email -- Empty string
"""
from unittest.mock import patch

import pytest
from django_swagger_utils.utils.test_v1 import TestUtils
from . import APP_NAME, OPERATION_NAME, REQUEST_METHOD, URL_SUFFIX


class TestCase01UserResetPasswordLinkAPITestCase(TestUtils):
    APP_NAME = APP_NAME
    OPERATION_NAME = OPERATION_NAME
    REQUEST_METHOD = REQUEST_METHOD
    URL_SUFFIX = URL_SUFFIX
    SECURITY = {'oauth': {'scopes': ['read']}}

    @pytest.mark.django_db
    @patch(
        "ib_iam.adapters.auth_service.AuthService.get_token_for_reset_password"
    )
    def test_case(self, get_token_for_reset_password, snapshot):
        from ib_iam.exceptions.custom_exceptions import InvalidEmail
        get_token_for_reset_password.side_effect = InvalidEmail
        body = {'email': 'test@gmail.com'}
        path_params = {}
        query_params = {}
        headers = {}
        response = self.default_test_case(
            body=body, path_params=path_params,
            query_params=query_params, headers=headers, snapshot=snapshot
        )
