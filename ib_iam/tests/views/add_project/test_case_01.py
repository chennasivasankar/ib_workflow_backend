"""
success case of add project
"""
from uuid import UUID

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
        from ib_iam.tests.common_fixtures.adapters.uuid_mock import \
            prepare_uuid_mock
        mock = prepare_uuid_mock(mocker)
        mock.return_value = UUID("7eb737be-810f-4580-83ea-ff4fa67edd22")
        body = {
            'name': 'project_1',
            'description': 'project_description',
            'logo_url': 'https://logo.com',
            'team_ids': setup,
            "project_display_id": "display_id 1",
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
        self._additional_checks(snapshot)

    @staticmethod
    def _additional_checks(snapshot):
        from ib_iam.models import Project, ProjectTeam, ProjectRole
        project_id = "project_7eb737be810f458083eaff4fa67edd22"
        project_details = Project.objects.filter(
            project_id=project_id).values()
        snapshot.assert_match(list(project_details), "project_details")
        project_team_ids = ProjectTeam.objects.filter(project=project_id) \
            .values_list("team_id", flat=True)
        project_team_ids = list(map(str, project_team_ids))
        snapshot.assert_match(project_team_ids, "project_team_ids")
        project_roles = ProjectRole.objects.filter(project_id=project_id) \
            .values("role_id", "name", "description")
        snapshot.assert_match(list(project_roles), "project_roles")

    # TODO: Don't use underscore readability is missing.
    @pytest.fixture
    def setup(self, api_user):
        from ib_iam.tests.factories.models import \
            UserDetailsFactory, TeamFactory
        UserDetailsFactory(user_id=str(api_user.user_id), is_admin=True)
        team_ids = ['f2c02d98-f311-4ab2-8673-3daa00757003']
        _ = [TeamFactory(team_id=team_id) for team_id in team_ids]
        return team_ids
