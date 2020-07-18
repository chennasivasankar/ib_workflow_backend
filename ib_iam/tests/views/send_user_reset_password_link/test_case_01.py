"""
    Invalid Email -- Empty string
"""
from unittest.mock import patch

import pytest
from django_swagger_utils.utils.test_v1 import TestUtils
from . import APP_NAME, OPERATION_NAME, REQUEST_METHOD, URL_SUFFIX


class TestCase01SendUserResetPasswordLinkAPITestCase(TestUtils):
    APP_NAME = APP_NAME
    OPERATION_NAME = OPERATION_NAME
    REQUEST_METHOD = REQUEST_METHOD
    URL_SUFFIX = URL_SUFFIX
    SECURITY = {'oauth': {'scopes': ['read']}}

    @pytest.mark.django_db
    def test_case(self, mocker, snapshot):
        body = {'email': ''}
        from ib_iam.exceptions.custom_exceptions import InvalidEmail
        from ib_iam.tests.common_fixtures.adapters.auth_service_adapter_mocks import \
            prepare_get_reset_password_token_mock
        prepare_get_reset_password_token_mock(mocker).side_effect = InvalidEmail
        path_params = {}
        query_params = {}
        headers = {}
        response = self.default_test_case(
            body=body, path_params=path_params,
            query_params=query_params, headers=headers, snapshot=snapshot
        )
