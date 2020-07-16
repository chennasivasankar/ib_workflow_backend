"""
# TODO: Update test case description
"""
import pytest
from django_swagger_utils.utils.test_v1 import TestUtils
from . import APP_NAME, OPERATION_NAME, REQUEST_METHOD, URL_SUFFIX
from ...factories.models import UserProfileFactory

USER_ID= '7e39bf1c-f9a5-4e76-8451-b962ddd520fc'
class TestCase01GetUsersAPITestCase(TestUtils):
    APP_NAME = APP_NAME
    OPERATION_NAME = OPERATION_NAME
    REQUEST_METHOD = REQUEST_METHOD
    URL_SUFFIX = URL_SUFFIX
    SECURITY = {'oauth': {'scopes': ['read']}}

    @pytest.fixture
    def set_up(self, api_user):
        user_id = api_user.id
        from ib_iam.models import UserProfile
        UserProfile.objects.create(user_id=user_id, is_admin=False)


    @pytest.mark.django_db
    def test_case(self, set_up, snapshot):

        body = {}
        path_params = {}
        query_params = {'offset': 0, 'limit': 10}
        headers = {}
        response = self.default_test_case(
            body=body, path_params=path_params,
            query_params=query_params, headers=headers, snapshot=snapshot
        )

