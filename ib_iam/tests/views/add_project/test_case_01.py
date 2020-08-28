"""
success case of add project
"""
import pytest
from django_swagger_utils.utils.test_utils import TestUtils
from . import APP_NAME, OPERATION_NAME, REQUEST_METHOD, URL_SUFFIX


class TestCase01AddProjectAPITestCase(TestUtils):
    APP_NAME = APP_NAME
    OPERATION_NAME = OPERATION_NAME
    REQUEST_METHOD = REQUEST_METHOD
    URL_SUFFIX = URL_SUFFIX
    SECURITY = {'oauth': {'scopes': ['write']}}

    @pytest.mark.django_db
    def test_case(self, setup, mocker, snapshot):
        body = {
            'name': 'project_1',
            'description': 'project_description',
            'logo_url': 'https://logo.com',
            'team_ids': setup,
            'roles': [{
                'role_name': 'role1',
                'description': 'description1'
            }]
        }
        path_params = {}
        query_params = {}
        headers = {}
        response = self.make_api_call(body=body,
                                      path_params=path_params,
                                      query_params=query_params,
                                      headers=headers,
                                      snapshot=snapshot)

    @pytest.fixture
    def setup(self):
        team_ids = ['f2c02d98-f311-4ab2-8673-3daa00757003']
        from ib_iam.tests.factories.models import TeamFactory
        _ = [TeamFactory(team_id=team_id) for team_id in team_ids]
        return team_ids
