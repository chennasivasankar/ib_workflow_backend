"""
Returns Invalid Limit response as BadRequest
as the given limit is invalid
"""
import pytest
from django_swagger_utils.utils.test_utils import TestUtils

from ib_iam.tests.factories.models import (
    UserDetailsFactory
)
from . import APP_NAME, OPERATION_NAME, REQUEST_METHOD, URL_SUFFIX


class TestCase03GetListOfTeamsAPITestCase(TestUtils):
    APP_NAME = APP_NAME
    OPERATION_NAME = OPERATION_NAME
    REQUEST_METHOD = REQUEST_METHOD
    URL_SUFFIX = URL_SUFFIX
    SECURITY = {'oauth': {'scopes': ['read']}}

    @pytest.mark.django_db
    def test_case(self, snapshot, setup):
        body = {}
        path_params = {}
        query_params = {'limit': -1, 'offset': 5}
        headers = {}
        response = self.make_api_call(
            body=body, path_params=path_params,
            query_params=query_params, headers=headers, snapshot=snapshot
        )

    @pytest.fixture()
    def setup(self, api_user):
        user_obj = api_user
        UserDetailsFactory.reset_sequence(1)
        UserDetailsFactory.create(user_id=user_obj.user_id, is_admin=True)
