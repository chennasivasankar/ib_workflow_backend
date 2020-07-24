"""
# Returns team_id as valid parameters are given
"""
import pytest
from django_swagger_utils.utils.test_v1 import TestUtils
from . import APP_NAME, OPERATION_NAME, REQUEST_METHOD, URL_SUFFIX
from ...factories.models import TeamFactory, UserTeamFactory, \
    UserDetailsFactory


class TestCase01UpdateTeamDetailsAPITestCase(TestUtils):
    APP_NAME = APP_NAME
    OPERATION_NAME = OPERATION_NAME
    REQUEST_METHOD = REQUEST_METHOD
    URL_SUFFIX = URL_SUFFIX
    SECURITY = {'oauth': {'scopes': ['write']}}

    @pytest.fixture
    def setup(self, api_user):
        user_id = str(api_user.user_id)
        UserDetailsFactory.reset_sequence(1)
        UserTeamFactory.reset_sequence(1)
        TeamFactory.reset_sequence(1)
        UserDetailsFactory(user_id=user_id, is_admin=True)
        team_id = "f2c02d98-f311-4ab2-8673-3daa00757002"
        team = TeamFactory.create(team_id=team_id)
        from ib_iam.models import Team, UserTeam, UserDetails
        print(Team.objects.values())
        for user_id in ["2", "3"]:
            UserTeamFactory.create(team=team, user_id=user_id)
            print(UserTeam.objects.values())
            UserDetailsFactory.create(user_id=user_id)
            print(UserDetails.objects.values())
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
