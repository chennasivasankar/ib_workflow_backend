"""
Deletes a team as valid parameters are given
"""
import pytest
from django_swagger_utils.utils.test_utils import TestUtils

from . import APP_NAME, OPERATION_NAME, REQUEST_METHOD, URL_SUFFIX


class TestCase01DeleteTeamAPITestCase(TestUtils):
    APP_NAME = APP_NAME
    OPERATION_NAME = OPERATION_NAME
    REQUEST_METHOD = REQUEST_METHOD
    URL_SUFFIX = URL_SUFFIX
    SECURITY = {'oauth': {'scopes': ['delete']}}

    @pytest.mark.django_db
    def test_case(self, setup, snapshot):
        team_id = setup
        body = {}
        path_params = {"team_id": team_id}
        query_params = {}
        headers = {}
        response = self.make_api_call(
            body=body, path_params=path_params,
            query_params=query_params, headers=headers, snapshot=snapshot
        )

    @pytest.fixture
    def setup(self, api_user):
        user_id = api_user.user_id
        team_id = "413642ff-1272-4990-b878-6607a5e02bc1"
        from ib_iam.tests.factories.models import TeamFactory, \
            UserDetailsFactory
        UserDetailsFactory.reset_sequence(1)
        TeamFactory.reset_sequence(1)
        UserDetailsFactory.create(user_id=user_id, is_admin=True)
        TeamFactory.create(team_id=team_id)
        return team_id
