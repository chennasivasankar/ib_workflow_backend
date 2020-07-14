"""
# TODO: Invaild password raise exception
"""
from unittest.mock import patch

import pytest
from django_swagger_utils.utils.test_v1 import TestUtils
from . import APP_NAME, OPERATION_NAME, REQUEST_METHOD, URL_SUFFIX


class TestCase03UserLoginAPITestCase(TestUtils):
    APP_NAME = APP_NAME
    OPERATION_NAME = OPERATION_NAME
    REQUEST_METHOD = REQUEST_METHOD
    URL_SUFFIX = URL_SUFFIX
    SECURITY = {'oauth': {'scopes': ['read']}}


    @pytest.mark.django_db
    @patch(
        "ib_iam.adapters.auth_service.AuthService.get_user_id_from_email_and_password_dto")
    def test_case(self, get_user_id_from_email_and_password_dto, snapshot):
        from ib_iam.interactors.user_login_interactor import InvalidPassword
        get_user_id_from_email_and_password_dto.side_effect = InvalidPassword()
        body = {'email': 'sasnkar@gmail.com', 'password': 'test123'}
        path_params = {}
        query_params = {}
        headers = {}
        response = self.default_test_case(
            body=body, path_params=path_params,
            query_params=query_params, headers=headers, snapshot=snapshot
        )
