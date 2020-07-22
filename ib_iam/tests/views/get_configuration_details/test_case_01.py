"""
# TODO: Update test case description
"""
import pytest
from django_swagger_utils.utils.test_v1 import TestUtils
from . import APP_NAME, OPERATION_NAME, REQUEST_METHOD, URL_SUFFIX

class TestCase01GetConfigurationDetailsAPITestCase(TestUtils):
    APP_NAME = APP_NAME
    OPERATION_NAME = OPERATION_NAME
    REQUEST_METHOD = REQUEST_METHOD
    URL_SUFFIX = URL_SUFFIX
    SECURITY = {'oauth': {'scopes': ['read']}}

    @pytest.fixture
    def user_set_up(self, api_user):
        user_id = api_user.user_id
        from ib_iam.tests.factories.models import UserDetailsFactory
        from ib_iam.tests.common_fixtures.storages import reset_all_factories_sequence
        reset_all_factories_sequence()
        UserDetailsFactory.create(user_id=user_id, is_admin=False)
        UserDetailsFactory.create_batch(4)

    @pytest.mark.django_db
    def test_case(self, user_set_up, snapshot):
        body = {}
        path_params = {}
        query_params = {}
        headers = {}
        response = self.default_test_case(
            body=body, path_params=path_params,
            query_params=query_params, headers=headers, snapshot=snapshot
        )