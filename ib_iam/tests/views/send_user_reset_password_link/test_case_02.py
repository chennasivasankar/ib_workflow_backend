"""
    UserAccountDoesNotExist
"""
from unittest.mock import patch

import pytest
from django_swagger_utils.utils.test_utils import TestUtils
from . import APP_NAME, OPERATION_NAME, REQUEST_METHOD, URL_SUFFIX


class TestCase02SendUserResetPasswordLinkAPITestCase(TestUtils):
    APP_NAME = APP_NAME
    OPERATION_NAME = OPERATION_NAME
    REQUEST_METHOD = REQUEST_METHOD
    URL_SUFFIX = URL_SUFFIX
    SECURITY = {'oauth': {'scopes': ['read']}}

    @pytest.mark.django_db
    def test_case(self, mocker, snapshot):
        body = {'email': 'test@gmail.com'}
        from ib_iam.exceptions.custom_exceptions import UserAccountDoesNotExist
        from ib_iam.tests.common_fixtures.adapters.auth_service_adapter_mocks import \
            get_reset_password_token_mock
        get_reset_password_token_mock = get_reset_password_token_mock(
            mocker)
        get_reset_password_token_mock.side_effect = UserAccountDoesNotExist
        path_params = {}
        query_params = {"token": "123"}
        headers = {}
        self.make_api_call(
            body=body, path_params=path_params,
            query_params=query_params, headers=headers, snapshot=snapshot
        )
        get_reset_password_token_mock.assert_called_once()
