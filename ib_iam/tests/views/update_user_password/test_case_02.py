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
    @patch(
        "ib_iam.adapters.auth_service.AuthService.update_user_password_with_reset_password_token"
    )
    def test_token_does_not_exist(self, update_user_password_mock,
                                  snapshot):
        from ib_iam.interactors.update_user_password_interactor import \
            TokenDoesNotExist
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
    @patch(
        "ib_iam.adapters.auth_service.AuthService.update_user_password_with_reset_password_token"
    )
    def test_token_has_expired(self, update_user_password_mock,
                               snapshot):
        from ib_iam.interactors.update_user_password_interactor import \
            TokenHasExpired
        update_user_password_mock.side_effect = TokenHasExpired()
        body = {'password': 'string'}
        path_params = {}
        query_params = {'token': 184}
        headers = {}
        response = self.default_test_case(
            body=body, path_params=path_params,
            query_params=query_params, headers=headers, snapshot=snapshot
        )

    @pytest.mark.django_db
    @patch(
        "ib_iam.adapters.auth_service.AuthService.update_user_password_with_reset_password_token"
    )
    def test_case_for_required_password_min_length(
            self, update_user_password, snapshot
    ):
        from ib_iam.interactors.update_user_password_interactor import \
            PasswordMinLength
        update_user_password.side_effect \
            = PasswordMinLength

        body = {'email': 'test@gmail.com', 'password': 'test123'}
        path_params = {}
        query_params = {}
        headers = {}
        response = self.default_test_case(
            body=body, path_params=path_params,
            query_params=query_params, headers=headers, snapshot=snapshot
        )

    @pytest.mark.django_db
    @patch(
        "ib_iam.adapters.auth_service.AuthService.update_user_password_with_reset_password_token"
    )
    def test_case_for_required_password_one_special_character(
            self, update_user_password,
            snapshot
    ):
        from ib_iam.interactors.update_user_password_interactor import \
            PasswordAtLeastOneSpecialCharacter
        update_user_password.side_effect \
            = PasswordAtLeastOneSpecialCharacter
        body = {'email': 'test@gmail.com', 'password': 'test123'}
        path_params = {}
        query_params = {}
        headers = {}
        response = self.default_test_case(
            body=body, path_params=path_params,
            query_params=query_params, headers=headers, snapshot=snapshot
        )
