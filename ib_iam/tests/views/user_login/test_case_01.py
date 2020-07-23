"""
Valid email and password return response
"""
from unittest.mock import patch

import pytest
from django_swagger_utils.utils.test_v1 import TestUtils
from . import APP_NAME, OPERATION_NAME, REQUEST_METHOD, URL_SUFFIX


class TestCase01UserLoginAPITestCase(TestUtils):
    APP_NAME = APP_NAME
    OPERATION_NAME = OPERATION_NAME
    REQUEST_METHOD = REQUEST_METHOD
    URL_SUFFIX = URL_SUFFIX
    SECURITY = {'oauth': {'scopes': ['read']}}

    @pytest.mark.django_db
    def test_case(self, mocker, snapshot):
        from ib_iam.adapters.auth_service import UserTokensDTO
        tokens_dto = UserTokensDTO(
            access_token="asdfaldskfjdfdlsdkf",
            refresh_token="sadfenkljkdfeller",
            user_id="1",
            expires_in_seconds=1000
        )
        from ib_iam.tests.factories.models import UserFactory
        UserFactory.reset_sequence(1)
        UserFactory()

        from ib_iam.tests.common_fixtures.adapters.auth_service_adapter_mocks import \
            prepare_get_user_tokens_dto_for_given_email_and_password_dto_mock
        get_tokens_dto_for_given_email_and_password_dto_mock \
            = prepare_get_user_tokens_dto_for_given_email_and_password_dto_mock(mocker)
        get_tokens_dto_for_given_email_and_password_dto_mock.return_value \
            = tokens_dto

        body = {'email': 'string@gmail.com', 'password': 'sankaR@123'}
        path_params = {}
        query_params = {}
        headers = {}
        response = self.default_test_case(
            body=body, path_params=path_params,
            query_params=query_params, headers=headers, snapshot=snapshot
        )
