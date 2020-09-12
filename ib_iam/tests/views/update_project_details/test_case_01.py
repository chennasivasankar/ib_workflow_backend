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
        from ib_iam.models import Project, ProjectTeam, ProjectRole, UserRole
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
        user_roles = UserRole.objects.filter(
            project_role__project_id=project_id
        ).values("user_id", "project_role_id")
        snapshot.assert_match(list(user_roles), "user_roles")

    @pytest.fixture
    def setup(self):
        project_id = "project_1"
        team_ids = ['89d96f4b-c19d-4e69-8eae-e818f3123b09',
                    '89d96f4b-c19d-4e69-8eae-e818f3123b08',
                    '89d96f4b-c19d-4e69-8eae-e818f3123b00']
        role_ids = ["pay_role", "allocation_role"]
        user_ids = ['89d96f4b-c19d-4e69-8eae-e818f3123b18',
                    '89d96f4b-c19d-4e69-8eae-e818f3123b19']
        from ib_iam.tests.factories.models import (
            ProjectFactory, TeamFactory, ProjectTeamFactory,
            ProjectRoleFactory, TeamUserFactory, UserRoleFactory
        )
        ProjectFactory.reset_sequence(1)
        project_object = ProjectFactory(project_id=project_id)
        team_objects = [TeamFactory(team_id=team_id) for team_id in team_ids]
        # team_objects_for_project = team_objects[0:2]
        for team_object in team_objects:
            ProjectTeamFactory(project=project_object, team=team_object)
        project_role_objects = [
            ProjectRoleFactory(project=project_object, role_id=role_id)
            for role_id in role_ids
        ]
        team_users_details = [
            {"team": team_objects[0], "user_id": user_ids[0]},
            {"team": team_objects[1], "user_id": user_ids[0]},
            {"team": team_objects[0], "user_id": user_ids[1]}
        ]
        for team_user in team_users_details:
            TeamUserFactory(
                team=team_user["team"], user_id=team_user["user_id"]
            )
        user_role_details = [
            {"user_id": user_ids[0], "project_role": project_role_objects[0]},
            {"user_id": user_ids[0], "project_role": project_role_objects[1]},
            {"user_id": user_ids[1], "project_role": project_role_objects[0]}
        ]
        for user_role in user_role_details:
            UserRoleFactory(
                user_id=user_role["user_id"],
                project_role=user_role["project_role"]
            )
