"""
Test ALL Exceptions
"""

import pytest
from django_swagger_utils.utils.test_utils import TestUtils

from . import APP_NAME, OPERATION_NAME, REQUEST_METHOD, URL_SUFFIX


class TestCase02UserLoginAPITestCase(TestUtils):
    APP_NAME = APP_NAME
    OPERATION_NAME = OPERATION_NAME
    REQUEST_METHOD = REQUEST_METHOD
    URL_SUFFIX = URL_SUFFIX
    SECURITY = {'oauth': {'scopes': ['read']}}

    @pytest.mark.django_db
    def test_case_user_account_not_exist(self, mocker, snapshot):
        from ib_iam.exceptions.custom_exceptions import UserAccountDoesNotExist
        from ib_iam.tests.common_fixtures.adapters.auth_service_adapter_mocks import \
            prepare_get_user_tokens_dto_for_given_email_and_password_dto_mock
        get_tokens_dto_for_given_email_and_password_dto \
            = prepare_get_user_tokens_dto_for_given_email_and_password_dto_mock(
            mocker)
        get_tokens_dto_for_given_email_and_password_dto.side_effect \
            = UserAccountDoesNotExist

        self._create_user()
        body = {'email': 'sasnkar@gmail.com', 'password': 'test123'}
        path_params = {}
        query_params = {}
        headers = {}
        response = self.make_api_call(
            body=body, path_params=path_params,
            query_params=query_params, headers=headers, snapshot=snapshot
        )

    @staticmethod
    def _create_user():
        from ib_iam.tests.factories.models import UserFactory
        UserFactory.reset_sequence(1)
        UserFactory()

    @pytest.mark.django_db
    def test_case_incorrect_password(self, mocker, snapshot):
        from ib_iam.interactors.user_login_interactor import IncorrectPassword
        from ib_iam.tests.common_fixtures.adapters.auth_service_adapter_mocks import \
            prepare_get_user_tokens_dto_for_given_email_and_password_dto_mock
        get_tokens_dto_for_given_email_and_password_dto \
            = prepare_get_user_tokens_dto_for_given_email_and_password_dto_mock(
            mocker)
        get_tokens_dto_for_given_email_and_password_dto.side_effect \
            = IncorrectPassword
        self._create_user()
        body = {'email': 'sasnkar@gmail.com', 'password': 'test123'}
        path_params = {}
        query_params = {}
        headers = {}
        response = self.make_api_call(
            body=body, path_params=path_params,
            query_params=query_params, headers=headers, snapshot=snapshot
        )

    @pytest.mark.django_db
    def test_case_for_invalid_email(self, mocker, snapshot):
        from ib_iam.exceptions.custom_exceptions import InvalidEmail
        from ib_iam.tests.common_fixtures.adapters.auth_service_adapter_mocks import \
            prepare_get_user_tokens_dto_for_given_email_and_password_dto_mock
        get_tokens_dto_for_given_email_and_password_dto \
            = prepare_get_user_tokens_dto_for_given_email_and_password_dto_mock(
            mocker)
        get_tokens_dto_for_given_email_and_password_dto.side_effect \
            = InvalidEmail
        self._create_user()
        body = {'email': 'sasnka', 'password': 'test123'}
        path_params = {}
        query_params = {}
        headers = {}
        response = self.make_api_call(
            body=body, path_params=path_params,
            query_params=query_params, headers=headers, snapshot=snapshot
        )
