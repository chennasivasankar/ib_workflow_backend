"""
All Invalid Cases and Raise Exceptions
"""
import pytest
from django_swagger_utils.utils.test_utils import TestUtils
from . import APP_NAME, OPERATION_NAME, REQUEST_METHOD, URL_SUFFIX


class TestCase02SendVerifyEmailLinkAPITestCase(TestUtils):
    APP_NAME = APP_NAME
    OPERATION_NAME = OPERATION_NAME
    REQUEST_METHOD = REQUEST_METHOD
    URL_SUFFIX = URL_SUFFIX
    SECURITY = {'oauth': {'scopes': []}}

    @pytest.fixture
    def set_up_account_not_found(self, mocker):
        from ib_iam.tests.common_fixtures.adapters.user_service import \
            get_user_id_for_given_email_mock
        get_user_id_for_given_email_mock = get_user_id_for_given_email_mock(
            mocker=mocker)
        from ib_iam.interactors.send_verify_email_link_interactor import \
            UserAccountDoesNotExist
        get_user_id_for_given_email_mock.side_effect = \
            UserAccountDoesNotExist()

    @pytest.mark.django_db
    def test_case_invalid_email_then_raise_account_not_found_exception(
            self, set_up_account_not_found, snapshot):
        body = {'email': 'durgaprasad@gmail.com'}
        path_params = {}
        query_params = {}
        headers = {}
        self.make_api_call(
            body=body,
            path_params=path_params,
            query_params=query_params,
            headers=headers,
            snapshot=snapshot
        )

    @pytest.fixture
    def set_up_for_already_verified_email(self, mocker):
        user_id = "123e4567-e89b-12d3-a456-426614174000"
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
        UserProfileDTOFactory.reset_sequence(0)
        get_user_profile_dto_mock.return_value = UserProfileDTOFactory.create(
            user_id=user_id, is_email_verified=True)

    @pytest.mark.django_db
    def test_case_already_active_email_and_email_verified_then_raise_account_is_already_verifys_exception(
            self, set_up_for_already_verified_email, snapshot):
        body = {'email': 'durgaprasad@gmail.com'}
        path_params = {}
        query_params = {}
        headers = {}
        self.make_api_call(
            body=body,
            path_params=path_params,
            query_params=query_params,
            headers=headers,
            snapshot=snapshot
        )
# TODO for email validation test case need to write
