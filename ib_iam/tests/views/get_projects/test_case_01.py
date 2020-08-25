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
    def setup(self):
        from ib_iam.tests.factories.models import \
            ProjectFactory, TeamFactory, ProjectTeamFactory
        ProjectFactory.reset_sequence(1)
        TeamFactory.reset_sequence(1)
        project_id = "641bfcc5-e1ea-4231-b482-f7f34fb5c7c4"
        team_id = "641bfcc5-e1ea-4231-b482-f7f34fb5c7c5"
        project_object = ProjectFactory(project_id=project_id)
        team_object = TeamFactory(team_id=team_id)
        project_teams = [ProjectTeamFactory(project=project_object,
                                            team=team_object)]
