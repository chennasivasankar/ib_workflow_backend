"""
success case of update project
"""

import pytest
from django_swagger_utils.utils.test_utils import TestUtils

from ib_iam.tests.factories.models import (
    UserDetailsFactory, ProjectFactory, ProjectRoleFactory, TeamFactory,
    ProjectTeamFactory)
from . import APP_NAME, OPERATION_NAME, REQUEST_METHOD, URL_SUFFIX


class TestCase02UpdateProjectDetailsAPITestCase(TestUtils):
    APP_NAME = APP_NAME
    OPERATION_NAME = OPERATION_NAME
    REQUEST_METHOD = REQUEST_METHOD
    URL_SUFFIX = URL_SUFFIX
    SECURITY = {'oauth': {'scopes': ['write']}}

    @pytest.mark.django_db
    def test_given_user_is_not_admin_returns_user_has_no_access_response(
            self, api_user, snapshot):
        UserDetailsFactory(user_id=str(api_user.user_id))
        project_id = "project_1"
        ProjectFactory(project_id=project_id)
        body = {
            'name': 'payment_project',
            'description': None,
            'logo_url': None,
            'team_ids': [],
            'roles': [
                {
                    'role_name': 'Payment_RP',
                    'description': "pay_1",
                    'role_id': 'pay_role'
                }
            ]
        }
        path_params = {"project_id": project_id}
        query_params = {}
        headers = {}
        self.make_api_call(body=body,
                           path_params=path_params,
                           query_params=query_params,
                           headers=headers,
                           snapshot=snapshot)

    @pytest.mark.django_db
    def test_given_project_name_already_exists_returns_name_already_exists_response(
            self, api_user, snapshot):
        UserDetailsFactory(user_id=str(api_user.user_id), is_admin=True)
        project_id = "project_1"
        name = "project 1"
        ProjectFactory.reset_sequence()
        ProjectFactory.create(project_id=project_id)
        ProjectFactory.create(name=name)
        body = {
            'name': name,
            'description': None,
            'logo_url': None,
            'team_ids': [],
            'roles': []
        }
        path_params = {"project_id": project_id}
        query_params = {}
        headers = {}
        self.make_api_call(body=body,
                           path_params=path_params,
                           query_params=query_params,
                           headers=headers,
                           snapshot=snapshot)

    @pytest.mark.django_db
    def test_given_duplicate_team_ids_returns_duplicate_team_ids_response(
            self, api_user, setup, snapshot):
        body = {
            'name': "project_1",
            'description': 'project_description',
            'logo_url': 'https://logo.com',
            'team_ids': [setup["team_id"], setup["team_id"]],
            'roles': []
        }
        path_params = {"project_id": setup["project_id"]}
        query_params = {}
        headers = {}
        self.make_api_call(body=body,
                           path_params=path_params,
                           query_params=query_params,
                           headers=headers,
                           snapshot=snapshot)

    @pytest.mark.django_db
    def test_given_invalid_team_ids_returns_invalid_team_ids_response(
            self, api_user, setup, snapshot):
        body = {
            'name': "project_1",
            'description': 'project_description',
            'logo_url': 'https://logo.com',
            'team_ids': ["123e4567-e89b-12d3-a456-426614174001"],
            'roles': []
        }
        path_params = {"project_id": setup["project_id"]}
        query_params = {}
        headers = {}
        self.make_api_call(body=body,
                           path_params=path_params,
                           query_params=query_params,
                           headers=headers,
                           snapshot=snapshot)

    @pytest.mark.django_db
    def test_given_duplicate_role_ids_returns_duplicate_role_ids_response(
            self, api_user, setup, snapshot):
        body = {
            'name': "project_1",
            'description': 'project_description',
            'logo_url': 'https://logo.com',
            'team_ids': [],
            'roles': [
                {
                    'role_name': 'Payment_RP',
                    'description': "pay_1",
                    'role_id': setup["role_id"]
                },
                {
                    'role_name': 'Payment',
                    'description': "pay_2",
                    'role_id': setup["role_id"]
                }
            ]
        }
        path_params = {"project_id": setup["project_id"]}
        query_params = {}
        headers = {}
        self.make_api_call(body=body,
                           path_params=path_params,
                           query_params=query_params,
                           headers=headers,
                           snapshot=snapshot)

    @pytest.mark.django_db
    def test_given_invalid_role_ids_returns_invalid_role_ids_response(
            self, setup, snapshot):
        body = {
            'name': "project_1",
            'description': 'project_description',
            'logo_url': 'https://logo.com',
            'team_ids': [],
            'roles': [{
                'role_name': 'Payment_RP',
                'description': "pay_1",
                'role_id': 'finance_role'
            }]
        }
        path_params = {"project_id": setup["project_id"]}
        query_params = {}
        headers = {}
        self.make_api_call(body=body,
                           path_params=path_params,
                           query_params=query_params,
                           headers=headers,
                           snapshot=snapshot)

    @pytest.fixture
    def setup(self, api_user):
        UserDetailsFactory(user_id=str(api_user.user_id), is_admin=True)
        project_id = "project_1"
        team_id = "123e4567-e89b-12d3-a456-426614174000"
        project_object = ProjectFactory(project_id=project_id)
        team_object = TeamFactory(team_id=team_id)
        ProjectTeamFactory(project=project_object, team=team_object)
        role_id = 'pay_role'
        ProjectRoleFactory.create(project_id=project_id, role_id=role_id)
        return {"project_id": project_id,
                "team_id": team_id,
                "role_id": role_id}
