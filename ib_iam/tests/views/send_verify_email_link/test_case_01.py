"""
Success case for send verify email link to given email
"""
import pytest
from django_swagger_utils.utils.test_utils import TestUtils
from . import APP_NAME, OPERATION_NAME, REQUEST_METHOD, URL_SUFFIX


class TestCase01SendVerifyEmailLinkAPITestCase(TestUtils):
    APP_NAME = APP_NAME
    OPERATION_NAME = OPERATION_NAME
    REQUEST_METHOD = REQUEST_METHOD
    URL_SUFFIX = URL_SUFFIX
    SECURITY = {'oauth': {'scopes': []}}

    @pytest.mark.django_db
    def test_case_for_valid_details_then_send_verify_email_link(
            self, snapshot, mocker):
        self.mock_all_third_party_modules_for_send_verify_email_link(
            mocker=mocker)
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

    @staticmethod
    def mock_all_third_party_modules_for_send_verify_email_link(mocker):
        user_id = "123e4567-e89b-12d3-a456-426614174000"
        from ib_iam.tests.common_fixtures.adapters.auth_service_adapter_mocks import \
            create_auth_tokens_for_user_mock
        from ib_iam.tests.common_fixtures.adapters.user_service import \
            get_user_id_for_given_email_mock
        get_user_id_for_given_email_mock = get_user_id_for_given_email_mock(
            mocker=mocker)
        get_user_id_for_given_email_mock.return_value = user_id
        from ib_iam.tests.common_fixtures.adapters.user_service import \
            get_user_profile_dto_mock
        get_user_profile_dto_mock = get_user_profile_dto_mock(
            mocker=mocker)
        from ib_iam.tests.factories.adapter_dtos import UserProfileDTOFactory
        UserProfileDTOFactory.reset_sequence(0)
        get_user_profile_dto_mock.return_value = UserProfileDTOFactory.create(
            user_id=user_id, is_email_verified=False)
        create_auth_tokens_for_user_mock = create_auth_tokens_for_user_mock(
            mocker=mocker)
        from ib_iam.tests.factories.adapter_dtos import UserTokensDTOFactory
        UserTokensDTOFactory.reset_sequence(0)
        create_auth_tokens_for_user_mock.return_value = \
            UserTokensDTOFactory.create()
        from ib_iam.tests.common_fixtures.adapters.email_service_adapter_mocks import \
            send_email_mock
        send_email_mock = send_email_mock(mocker=mocker)
        send_email_mock.return_value = None
