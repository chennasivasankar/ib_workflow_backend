"""
test all cases
"""
import pytest
from django_swagger_utils.utils.test_v1 import TestUtils
from . import APP_NAME, OPERATION_NAME, REQUEST_METHOD, URL_SUFFIX


class TestCase01GetUserProfileAPITestCase(TestUtils):
    APP_NAME = APP_NAME
    OPERATION_NAME = OPERATION_NAME
    REQUEST_METHOD = REQUEST_METHOD
    URL_SUFFIX = URL_SUFFIX
    SECURITY = {'oauth': {'scopes': ['read']}}

    @pytest.mark.django_db
    def test_user_account_does_not_exist(self, api_user, snapshot):
        body = {}
        path_params = {}
        query_params = {}
        headers = {}

        response = self.default_test_case(
            body=body, path_params=path_params,
            query_params=query_params, headers=headers, snapshot=snapshot
        )

    @pytest.mark.django_db
    def test_valid_user_id(self, mocker, api_user, snapshot):
        body = {}
        path_params = {}
        query_params = {}
        headers = {}

        from ib_iam.tests.common_fixtures.adapters.user_service import \
            prepare_get_user_profile_dto_mock
        get_user_profile_dto_mock = prepare_get_user_profile_dto_mock(mocker)
        from ib_iam.adapters.dtos import UserProfileDTO
        get_user_profile_dto_mock.return_value = UserProfileDTO(
            user_id=api_user.id,
            email="test@gmail.com",
            profile_pic_url="test.com",
            is_admin=False,
            name="test"
        )
        from ib_iam.tests.factories.models import UserProfileFactory
        UserProfileFactory(user_id=api_user.id)

        response = self.default_test_case(
            body=body, path_params=path_params,
            query_params=query_params, headers=headers, snapshot=snapshot
        )
