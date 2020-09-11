"""
success case of update project
"""
from uuid import UUID

import pytest
from django_swagger_utils.utils.test_utils import TestUtils

from . import APP_NAME, OPERATION_NAME, REQUEST_METHOD, URL_SUFFIX


class TestCase01UpdateProjectDetailsAPITestCase(TestUtils):
    APP_NAME = APP_NAME
    OPERATION_NAME = OPERATION_NAME
    REQUEST_METHOD = REQUEST_METHOD
    URL_SUFFIX = URL_SUFFIX
    SECURITY = {'oauth': {'scopes': ['write']}}

    @pytest.mark.django_db
    def test_case(self, setup, api_user, mocker, snapshot):
        user_id = str(api_user.user_id)
        from ib_iam.tests.factories.models import UserDetailsFactory
        UserDetailsFactory(user_id=user_id, is_admin=True)
        from ib_iam.tests.common_fixtures.adapters.uuid_mock import \
            uuid_mock
        mock = uuid_mock(mocker)
        # below uuid is for role creation
        mock.return_value = UUID("7eb737be-810f-4580-83ea-ff4fa67edd22")
        body = {
            'name': 'payment_project',
            'description': None,
            'logo_url': None,
            'team_ids': ['89d96f4b-c19d-4e69-8eae-e818f3123b09',
                         '89d96f4b-c19d-4e69-8eae-e818f3123b00'],
            'roles': [
                {
                    'role_name': 'Payment_RP',
                    'description': "pay_1",
                    'role_id': 'pay_role'
                },
                {
                    'role_name': 'finance_advisor',
                    'description': None,
                    'role_id': None
                }
            ]
        }
        path_params = {"project_id": "project_1"}
        query_params = {}
        headers = {}
        self.make_api_call(body=body,
                           path_params=path_params,
                           query_params=query_params,
                           headers=headers,
                           snapshot=snapshot)
        self._additional_checks(snapshot)

    @staticmethod
    def _additional_checks(snapshot):
        from ib_iam.models import Project, ProjectTeam, ProjectRole
        project_id = "project_1"
        project_details = Project.objects.filter(project_id=project_id) \
            .values()
        snapshot.assert_match(list(project_details), "project_details")
        project_team_ids = ProjectTeam.objects.filter(project=project_id) \
            .values_list("team_id", flat=True)
        project_team_ids = list(map(str, project_team_ids))
        snapshot.assert_match(project_team_ids, "project_team_ids")
        project_roles = ProjectRole.objects.filter(project_id=project_id) \
            .values("role_id", "name", "description")
        snapshot.assert_match(list(project_roles), "project_roles")
        # todo after merging add-validations-pr-of-update-project write a test
        #  to show the user roles left after deleting some teams

    @pytest.fixture
    def setup(self):
        project_id = "project_1"
        team_ids = ['89d96f4b-c19d-4e69-8eae-e818f3123b09',
                    '89d96f4b-c19d-4e69-8eae-e818f3123b08',
                    '89d96f4b-c19d-4e69-8eae-e818f3123b00']
        role_ids = ["pay_role", "allocation_role"]
        from ib_iam.tests.factories.models import (
            ProjectFactory, TeamFactory, ProjectTeamFactory, ProjectRoleFactory
        )
        ProjectFactory.reset_sequence(1)
        project_object = ProjectFactory(project_id=project_id)
        team_objects = [TeamFactory(team_id=team_id) for team_id in team_ids]
        team_objects_for_project = team_objects[0:2]
        project_team_objects = [
            ProjectTeamFactory(project=project_object, team=team_object)
            for team_object in team_objects
        ]
        project_role_objects = [ProjectRoleFactory(project=project_object,
                                                   role_id=role_id)
                                for role_id in role_ids]
