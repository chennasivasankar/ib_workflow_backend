"""
All Invalid Cases (exception)
"""
import pytest
from django_swagger_utils.utils.test_utils import TestUtils

from . import APP_NAME, OPERATION_NAME, REQUEST_METHOD, URL_SUFFIX


class TestCase02GetProjectsAPITestCase(TestUtils):
    APP_NAME = APP_NAME
    OPERATION_NAME = OPERATION_NAME
    REQUEST_METHOD = REQUEST_METHOD
    URL_SUFFIX = URL_SUFFIX
    SECURITY = {'oauth': {'scopes': ['read']}}

    @pytest.mark.django_db
    def test_with_invalid_limit_value(self, snapshot):
        body = {}
        path_params = {}
        query_params = {'offset': 0, 'limit': -1}
        headers = {}
        self.make_api_call(
            body=body, path_params=path_params, query_params=query_params,
            headers=headers, snapshot=snapshot
        )

    @pytest.mark.django_db
    def test_with_invalid_offset_value(self, snapshot):
        body = {}
        path_params = {}
        query_params = {'offset': -1, 'limit': 5}
        headers = {}
        self.make_api_call(
            body=body, path_params=path_params, query_params=query_params,
            headers=headers, snapshot=snapshot
        )

    @pytest.fixture
    def setup(self, api_user):
        user_id = api_user.user_id
        from ib_iam.tests.factories.models import UserDetailsFactory
        UserDetailsFactory.reset_sequence(0)
        user_object = UserDetailsFactory.create(user_id=user_id)
        return user_object

    @pytest.mark.django_db
    def test_with_non_admin_user_then_raise_exception(self, setup, snapshot):
        body = {}
        path_params = {}
        query_params = {'offset': 0, 'limit': 5}
        headers = {}
        self.make_api_call(
            body=body, path_params=path_params, query_params=query_params,
            headers=headers, snapshot=snapshot
        )
