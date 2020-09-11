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

    @staticmethod
    def _create_user():
        from ib_iam.tests.factories.models import UserFactory
        UserFactory.reset_sequence(1)
        UserFactory()

    @pytest.mark.django_db
    def test_case_incorrect_password(self, mocker, snapshot):
        user_id = "1"
        from ib_iam.tests.common_fixtures.adapters.user_service import \
            get_user_id_for_given_email_mock
        get_user_id_for_given_email_mock = get_user_id_for_given_email_mock(
            mocker=mocker)
        get_user_id_for_given_email_mock.return_value = user_id
        from ib_iam.tests.common_fixtures.adapters.user_service import \
            prepare_get_user_profile_dto_mock
        get_user_profile_dto_mock = prepare_get_user_profile_dto_mock(
            mocker=mocker)
        from ib_iam.tests.factories.adapter_dtos import UserProfileDTOFactory
        get_user_profile_dto_mock.return_value = UserProfileDTOFactory.create(
            user_id=user_id, is_email_verified=True
        )
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
        self.make_api_call(
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
        self.make_api_call(
            body=body, path_params=path_params,
            query_params=query_params, headers=headers, snapshot=snapshot
        )

    @pytest.mark.django_db
    def test_case_email_is_not_verify_then_raise_email_not_verify(
            self, mocker, snapshot):
        user_id = "1"
        from ib_iam.tests.common_fixtures.adapters.user_service import \
            get_user_id_for_given_email_mock
        get_user_id_for_given_email_mock = get_user_id_for_given_email_mock(
            mocker=mocker)
        get_user_id_for_given_email_mock.return_value = user_id
        from ib_iam.tests.common_fixtures.adapters.user_service import \
            prepare_get_user_profile_dto_mock
        get_user_profile_dto_mock = prepare_get_user_profile_dto_mock(
            mocker=mocker)
        from ib_iam.tests.factories.adapter_dtos import UserProfileDTOFactory
        get_user_profile_dto_mock.return_value = UserProfileDTOFactory.create(
            user_id=user_id, is_email_verified=False
        )
        self._create_user()
        body = {'email': 'sasnkar@gmail.com', 'password': 'test123'}
        path_params = {}
        query_params = {}
        headers = {}
        self.make_api_call(
            body=body, path_params=path_params,
            query_params=query_params, headers=headers, snapshot=snapshot
        )

    @pytest.mark.django_db
    def test_with_not_register_email_then_raise_account_not_found_exception(
            self, mocker, snapshot):
        from ib_iam.tests.common_fixtures.adapters.user_service import \
            get_user_id_for_given_email_mock
        get_user_id_for_given_email_mock = get_user_id_for_given_email_mock(
            mocker=mocker)
        from ib_iam.exceptions.custom_exceptions import UserAccountDoesNotExist
        get_user_id_for_given_email_mock.side_effect = UserAccountDoesNotExist

        self._create_user()
        body = {'email': 'sasnkar@gmail.com', 'password': 'test123'}
        path_params = {}
        query_params = {}
        headers = {}
        self.make_api_call(
            body=body, path_params=path_params,
            query_params=query_params, headers=headers, snapshot=snapshot
        )
