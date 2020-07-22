"""
Raise UserHasNoAccess exception as the user is not admin
"""
import pytest
from django_swagger_utils.utils.test_v1 import TestUtils
from . import APP_NAME, OPERATION_NAME, REQUEST_METHOD, URL_SUFFIX
from ib_iam.tests.factories.models import (
    UserDetailsFactory
)


class TestCase02GetListOfTeamsAPITestCase(TestUtils):
    APP_NAME = APP_NAME
    OPERATION_NAME = OPERATION_NAME
    REQUEST_METHOD = REQUEST_METHOD
    URL_SUFFIX = URL_SUFFIX
    SECURITY = {'oauth': {'scopes': ['read']}}

    @pytest.mark.django_db
    def test_case(self, snapshot, setup):
        body = {}
        path_params = {}
        query_params = {'limit': 5, 'offset': 0}
        headers = {}
        response = self.default_test_case(
            body=body, path_params=path_params,
            query_params=query_params, headers=headers, snapshot=snapshot
        )

    @pytest.fixture()
    def setup(self, api_user):
        user_obj = api_user
        UserDetailsFactory.reset_sequence(1)
        UserDetailsFactory.create(user_id=user_obj.id)
