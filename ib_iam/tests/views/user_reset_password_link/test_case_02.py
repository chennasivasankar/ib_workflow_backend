"""
    UserAccountDoesNotExist
"""
from unittest.mock import patch

import pytest
from django_swagger_utils.utils.test_v1 import TestUtils
from . import APP_NAME, OPERATION_NAME, REQUEST_METHOD, URL_SUFFIX


class TestCase02UserResetPasswordLinkAPITestCase(TestUtils):
    APP_NAME = APP_NAME
    OPERATION_NAME = OPERATION_NAME
    REQUEST_METHOD = REQUEST_METHOD
    URL_SUFFIX = URL_SUFFIX
    SECURITY = {'oauth': {'scopes': ['read']}}

    @patch(
        "ib_iam.adapters.auth_service.AuthService.get_token_for_reset_password"
    )
    @pytest.mark.django_db
    def test_case(self,get_token_for_reset_password_mock, snapshot):
        body = {'email': 'test@gmail.com'}
        from ib_iam.interactors.DTOs.common_dtos import UserAccountDoesNotExist
        get_token_for_reset_password_mock.side_effect \
            = UserAccountDoesNotExist()
        path_params = {}
        query_params = {}
        headers = {}
        response = self.default_test_case(
            body=body, path_params=path_params,
            query_params=query_params, headers=headers, snapshot=snapshot
        )
        get_token_for_reset_password_mock.assert_called_once()
