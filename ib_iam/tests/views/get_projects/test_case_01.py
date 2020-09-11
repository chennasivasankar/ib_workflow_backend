"""
get projects success case which returns projects
"""
import pytest
from django_swagger_utils.utils.test_utils import TestUtils

from . import APP_NAME, OPERATION_NAME, REQUEST_METHOD, URL_SUFFIX


class TestCase01GetProjectsAPITestCase(TestUtils):
    APP_NAME = APP_NAME
    OPERATION_NAME = OPERATION_NAME
    REQUEST_METHOD = REQUEST_METHOD
    URL_SUFFIX = URL_SUFFIX
    SECURITY = {'oauth': {'scopes': ['read']}}

    @pytest.mark.django_db
    def test_case(self, setup, snapshot):
        body = {}
        path_params = {}
        query_params = {'offset': 0, 'limit': 5}
        headers = {}
        self.make_api_call(body=body,
                           path_params=path_params,
                           query_params=query_params,
                           headers=headers,
                           snapshot=snapshot)

    @pytest.fixture
    def setup(self, api_user):
        from ib_iam.tests.factories.models import (
            ProjectFactory, TeamFactory, ProjectTeamFactory,
            ProjectRoleFactory, UserDetailsFactory
        )
        user_id = api_user.user_id
        UserDetailsFactory.reset_sequence(0)
        user_object = UserDetailsFactory.create(user_id=user_id, is_admin=True)
        ProjectFactory.reset_sequence(1)
        TeamFactory.reset_sequence(1)
        ProjectRoleFactory.reset_sequence(1)
        project_id = "641bfcc5-e1ea-4231-b482-f7f34fb5c7c4"
        team_id = "641bfcc5-e1ea-4231-b482-f7f34fb5c7c5"
        role_id = "641bfcc5-e1ea-4231-b482-f7f34fb5c7c6"
        project_object = ProjectFactory(project_id=project_id)
        team_object = TeamFactory(team_id=team_id)
        project_teams = [
            ProjectTeamFactory(
                project=project_object, team=team_object
            )
        ]
        project_roles = [
            ProjectRoleFactory(role_id=role_id, project=project_object)
        ]
        return team_object, project_teams, project_roles, user_object
