"""
# Returns user has no access exception as he is not admin
"""
import pytest
from django_swagger_utils.utils.test_v1 import TestUtils
from . import APP_NAME, OPERATION_NAME, REQUEST_METHOD, URL_SUFFIX
from ...factories import TeamFactory, UserFactory


class TestCase02UpdateTeamDetailsAPITestCase(TestUtils):
    APP_NAME = APP_NAME
    OPERATION_NAME = OPERATION_NAME
    REQUEST_METHOD = REQUEST_METHOD
    URL_SUFFIX = URL_SUFFIX
    SECURITY = {'oauth': {'scopes': ['update']}}

    @pytest.fixture
    def setup(self, api_user):
        user_id = str(api_user.id)
        UserFactory.reset_sequence(1)
        TeamFactory.reset_sequence(1)
        UserFactory(user_id=user_id)
        team_id = "f2c02d98-f311-4ab2-8673-3daa00757002"
        TeamFactory.create(team_id=team_id)
        return team_id

    @pytest.mark.django_db
    def test_case(self, setup, snapshot):
        team_id = setup
        body = {'name': 'team1', 'description': '', 'user_ids': ["2", "3"]}
        path_params = {"team_id": team_id}
        query_params = {}
        headers = {}
        response = self.default_test_case(
            body=body, path_params=path_params,
            query_params=query_params, headers=headers, snapshot=snapshot
        )
