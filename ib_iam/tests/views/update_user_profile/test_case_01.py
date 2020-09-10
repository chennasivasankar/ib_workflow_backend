"""
Given valid details, it updates user profile
"""
import pytest
from django_swagger_utils.utils.test_utils import TestUtils

from . import APP_NAME, OPERATION_NAME, REQUEST_METHOD, URL_SUFFIX


class TestCase01UpdateUserProfileAPITestCase(TestUtils):
    APP_NAME = APP_NAME
    OPERATION_NAME = OPERATION_NAME
    REQUEST_METHOD = REQUEST_METHOD
    URL_SUFFIX = URL_SUFFIX
    SECURITY = {'oauth': {'scopes': ['write']}}

    @pytest.mark.django_db
    def test_case(self, mocker, setup, snapshot):
        user_id = setup
        from ib_iam.tests.common_fixtures.adapters.user_service \
            import prepare_update_user_profile_adapter_mock
        prepare_update_user_profile_adapter_mock(mocker=mocker)
        body = {'name': 'username',
                'email': 'jaswanthmamidipudi@gmail.com',
                'profile_pic_url': 'https://sample.com',
                "cover_page_url": ""}
        path_params = {}
        query_params = {}
        headers = {}
        response = self.make_api_call(body=body,
                                      path_params=path_params,
                                      query_params=query_params,
                                      headers=headers,
                                      snapshot=snapshot)
        from ib_iam.models import UserDetails
        user_object = UserDetails.objects.get(user_id=user_id)
        snapshot.assert_match(user_object.name, "updated_user_name")

    @pytest.fixture
    def setup(self, api_user):
        user_id = str(api_user.user_id)
        from ib_iam.tests.factories.models import UserDetailsFactory
        UserDetailsFactory.create(user_id=user_id)
        return user_id
