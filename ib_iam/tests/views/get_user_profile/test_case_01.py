"""
test all cases
"""
import pytest
from django_swagger_utils.utils.test_utils import TestUtils
from ib_users.models import UserAccount

from . import APP_NAME, OPERATION_NAME, REQUEST_METHOD, URL_SUFFIX


class TestCase01GetUserProfileAPITestCase(TestUtils):
    APP_NAME = APP_NAME
    OPERATION_NAME = OPERATION_NAME
    REQUEST_METHOD = REQUEST_METHOD
    URL_SUFFIX = URL_SUFFIX
    SECURITY = {'oauth': {'scopes': ['read']}}

    @pytest.mark.django_db
    def test_user_account_does_not_exist(self, mocker, snapshot):
        body = {}
        path_params = {}
        query_params = {}
        headers = {}

        from ib_iam.tests.common_fixtures.adapters.user_service import \
            prepare_get_user_profile_dto_mock
        get_user_profile_dto_mock = prepare_get_user_profile_dto_mock(mocker)
        from ib_iam.adapters.user_service import UserAccountDoesNotExist
        get_user_profile_dto_mock.side_effect = UserAccountDoesNotExist
        response = self.make_api_call(
            body=body, path_params=path_params,
            query_params=query_params, headers=headers, snapshot=snapshot
        )

    def _get_or_create_user(self):
        user_id = "c8939223-79a0-4566-ba13-b4fbf7db6f93"
        user = UserAccount.objects.create(user_id=user_id)
        return user

    @pytest.mark.django_db
    def test_valid_user_id(self, mocker, snapshot):
        body = {}
        path_params = {}
        query_params = {}
        headers = {}
        user_id = "c8939223-79a0-4566-ba13-b4fbf7db6f93"

        from ib_iam.tests.common_fixtures.adapters.user_service import \
            prepare_get_user_profile_dto_mock
        get_user_profile_dto_mock = prepare_get_user_profile_dto_mock(mocker)
        from ib_iam.adapters.dtos import UserProfileDTO
        get_user_profile_dto_mock.return_value = UserProfileDTO(
            user_id=user_id,
            email="test@gmail.com",
            profile_pic_url="test.com",
            is_admin=False,
            name="test"
        )
        from ib_iam.tests.factories.models import UserDetailsFactory
        UserDetailsFactory(user_id=user_id, is_admin=False)

        response = self.default_test_case(
            body=body, path_params=path_params,
            query_params=query_params, headers=headers, snapshot=snapshot
        )
