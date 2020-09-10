"""
# Returns invalid_users_exception response as invalid user_ids has given
"""
import pytest
from django_swagger_utils.utils.test_utils import TestUtils
from . import APP_NAME, OPERATION_NAME, REQUEST_METHOD, URL_SUFFIX
from ...factories.models import TeamFactory, TeamUserFactory, UserDetailsFactory

import pytest
from django_swagger_utils.utils.test_utils import TestUtils

from . import APP_NAME, OPERATION_NAME, REQUEST_METHOD, URL_SUFFIX
from ...factories.models import TeamFactory, TeamUserFactory, \
    UserDetailsFactory


class TestCase05UpdateTeamDetailsAPITestCase(TestUtils):
    APP_NAME = APP_NAME
    OPERATION_NAME = OPERATION_NAME
    REQUEST_METHOD = REQUEST_METHOD
    URL_SUFFIX = URL_SUFFIX
    SECURITY = {'oauth': {'scopes': ['write']}}

    @pytest.fixture
    def setup(self, api_user):
        user_id = str(api_user.user_id)
        UserDetailsFactory.reset_sequence(1)
        TeamUserFactory.reset_sequence(1)
        TeamFactory.reset_sequence(1)
        UserDetailsFactory(user_id=user_id, is_admin=True)
        team_id = "f2c02d98-f311-4ab2-8673-3daa00757002"
        team = TeamFactory.create(team_id=team_id)
        for user_id in ["2", "3"]:
            TeamUserFactory.create(team=team, user_id=user_id)
            UserDetailsFactory.create(user_id=user_id)
        return team_id

    @pytest.mark.django_db
    def test_case(self, setup, snapshot):
        team_id = setup
        body = {'name': 'team1', 'description': '', 'user_ids': ["2", "3", "4"]}
        path_params = {"team_id": team_id}
        query_params = {}
        headers = {}
        response = self.make_api_call(
            body=body, path_params=path_params,
            query_params=query_params, headers=headers, snapshot=snapshot
        )
