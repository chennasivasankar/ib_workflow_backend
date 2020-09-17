"""
Success case for verified email
"""
import pytest
from django_swagger_utils.utils.test_utils import TestUtils
from . import APP_NAME, OPERATION_NAME, REQUEST_METHOD, URL_SUFFIX


class TestCase01VerifyEmailAPITestCase(TestUtils):
    APP_NAME = APP_NAME
    OPERATION_NAME = OPERATION_NAME
    REQUEST_METHOD = REQUEST_METHOD
    URL_SUFFIX = URL_SUFFIX
    SECURITY = {'oauth': {'scopes': ['write', 'read']}}

    @pytest.mark.django_db
    def test_case_for_success_case_and_verified_email(self, snapshot, mocker):
        self.mock_all_third_party_modules_for_verify_email(mocker=mocker)
        body = {}
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
    def mock_all_third_party_modules_for_verify_email(mocker):
        user_id = "76fcdf69-853e-486d-bb90-2ef99bb43aa5"
        from ib_iam.tests.common_fixtures.adapters.user_service import \
            prepare_get_user_profile_dto_mock
        get_user_profile_dto_mock = prepare_get_user_profile_dto_mock(
            mocker=mocker)
        from ib_iam.adapters.dtos import UserProfileDTO
        get_user_profile_dto_mock.return_value = UserProfileDTO(
            email="example@gmail.com",
            user_id=user_id,
            name="Baba",
            is_email_verified=False
        )
        from ib_iam.tests.common_fixtures.adapters.auth_service_adapter_mocks import \
            update_is_email_verified_value_mock
        update_is_email_verified_value_mock = update_is_email_verified_value_mock(
            mocker=mocker)
        update_is_email_verified_value_mock.return_value = None
