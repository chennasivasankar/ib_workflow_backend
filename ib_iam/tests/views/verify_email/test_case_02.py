"""
For All exceptions
1. email already verified
"""
import pytest
from django_swagger_utils.utils.test_utils import TestUtils
from . import APP_NAME, OPERATION_NAME, REQUEST_METHOD, URL_SUFFIX


class TestCase02VerifyEmailAPITestCase(TestUtils):
    APP_NAME = APP_NAME
    OPERATION_NAME = OPERATION_NAME
    REQUEST_METHOD = REQUEST_METHOD
    URL_SUFFIX = URL_SUFFIX
    SECURITY = {'oauth': {'scopes': ['write', 'read']}}

    @pytest.mark.django_db
    def test_with_already_verified_email_then_raise_exception(
            self, snapshot, mocker):
        self.mock_all_third_party_modules_for_already_verified_email(
            mocker=mocker)
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
    def mock_all_third_party_modules_for_already_verified_email(mocker):
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
            is_email_verify=True
        )
