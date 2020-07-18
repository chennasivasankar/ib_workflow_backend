"""
All Exception in the user update password
"""
from unittest.mock import patch

import pytest
from django_swagger_utils.utils.test_v1 import TestUtils
from . import APP_NAME, OPERATION_NAME, REQUEST_METHOD, URL_SUFFIX


class TestCase02UpdateUserPasswordAPITestCase(TestUtils):
    APP_NAME = APP_NAME
    OPERATION_NAME = OPERATION_NAME
    REQUEST_METHOD = REQUEST_METHOD
    URL_SUFFIX = URL_SUFFIX
    SECURITY = {'oauth': {'scopes': ['write']}}

    @pytest.mark.django_db
    def test_token_does_not_exist(self, mocker, snapshot):
        from ib_iam.interactors.update_user_password_interactor import \
            TokenDoesNotExist
        from ib_iam.tests.common_fixtures.adapters.auth_service_adapter_mocks import \
            prepare_update_user_password_with_reset_password_token_mock
        update_user_password_mock \
            = prepare_update_user_password_with_reset_password_token_mock(mocker)
        update_user_password_mock.side_effect = TokenDoesNotExist()
        body = {'password': 'string'}
        path_params = {}
        query_params = {'token': "184"}
        headers = {}
        response = self.default_test_case(
            body=body, path_params=path_params,
            query_params=query_params, headers=headers, snapshot=snapshot
        )

    @pytest.mark.django_db
    def test_token_has_expired(self, mocker, snapshot):
        from ib_iam.interactors.update_user_password_interactor import \
            TokenHasExpired
        from ib_iam.tests.common_fixtures.adapters.auth_service_adapter_mocks import \
            prepare_update_user_password_with_reset_password_token_mock
        update_user_password_mock \
            = prepare_update_user_password_with_reset_password_token_mock(mocker)
        update_user_password_mock.side_effect = TokenHasExpired()
        body = {'password': 'string'}
        path_params = {}
        query_params = {'token': "184"}
        headers = {}
        response = self.default_test_case(
            body=body, path_params=path_params,
            query_params=query_params, headers=headers, snapshot=snapshot
        )

    @pytest.mark.django_db
    def test_case_for_required_password_min_length(
            self, mocker, snapshot
    ):
        from ib_iam.interactors.update_user_password_interactor import \
            PasswordMinLength
        from ib_iam.tests.common_fixtures.adapters.auth_service_adapter_mocks import \
            prepare_update_user_password_with_reset_password_token_mock
        update_user_password_mock \
            = prepare_update_user_password_with_reset_password_token_mock(mocker)
        update_user_password_mock.side_effect \
            = PasswordMinLength

        body = {'email': 'test@gmail.com', 'password': 'test123'}
        path_params = {}
        query_params = {'token': "184"}
        headers = {}
        response = self.default_test_case(
            body=body, path_params=path_params,
            query_params=query_params, headers=headers, snapshot=snapshot
        )

    @pytest.mark.django_db
    def test_case_for_required_password_one_special_character(
            self, mocker, snapshot
    ):
        from ib_iam.interactors.update_user_password_interactor import \
            PasswordAtLeastOneSpecialCharacter
        from ib_iam.tests.common_fixtures.adapters.auth_service_adapter_mocks import \
            prepare_update_user_password_with_reset_password_token_mock
        update_user_password_mock \
            = prepare_update_user_password_with_reset_password_token_mock(mocker)
        update_user_password_mock.side_effect \
            = PasswordAtLeastOneSpecialCharacter
        reset_password_token = "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9"
        body = {'email': 'test@gmail.com', 'password': 'test123'}
        path_params = {}
        query_params = {'token': reset_password_token}
        headers = {}
        response = self.default_test_case(
            body=body, path_params=path_params,
            query_params=query_params, headers=headers, snapshot=snapshot
        )
