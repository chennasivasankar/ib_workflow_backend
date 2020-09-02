"""
test all exception cases of add_project
"""

import pytest
from django_swagger_utils.utils.test_utils import TestUtils

from ib_iam.tests.factories.models import ProjectFactory
from . import APP_NAME, OPERATION_NAME, REQUEST_METHOD, URL_SUFFIX


class TestCase02AddProjectAPITestCase(TestUtils):
    APP_NAME = APP_NAME
    OPERATION_NAME = OPERATION_NAME
    REQUEST_METHOD = REQUEST_METHOD
    URL_SUFFIX = URL_SUFFIX
    SECURITY = {'oauth': {'scopes': ['write']}}

    @pytest.mark.django_db
    def test_given_project_name_already_exists_returns_name_already_exists_response(
            self, snapshot):
        name = "project_1"
        ProjectFactory.create(name=name)
        body = {
            'name': name,
            'description': 'project_description',
            'logo_url': 'https://logo.com',
            'team_ids': [],
            "project_display_id": "display_id 1",
            'roles': [{
                'role_name': 'role1',
                'description': 'description1'
            }]
        }
        path_params = {}
        query_params = {}
        headers = {}
        self.make_api_call(body=body,
                           path_params=path_params,
                           query_params=query_params,
                           headers=headers,
                           snapshot=snapshot)

    @pytest.mark.django_db
    def test_given_project_display_id_already_exists_returns_display_id_already_exists_response(
            self, snapshot):
        display_id = "display_id 1"
        ProjectFactory.create(display_id=display_id)
        body = {
            'name': "project_1",
            'description': 'project_description',
            'logo_url': 'https://logo.com',
            'team_ids': [],
            "project_display_id": display_id,
            'roles': [{
                'role_name': 'role1',
                'description': 'description1'
            }]
        }
        path_params = {}
        query_params = {}
        headers = {}
        self.make_api_call(body=body,
                           path_params=path_params,
                           query_params=query_params,
                           headers=headers,
                           snapshot=snapshot)

    @pytest.mark.django_db
    def test_given_duplicate_team_ids_returns_duplicate_team_ids_response(
            self, snapshot):
        body = {
            'name': "project_1",
            'description': 'project_description',
            'logo_url': 'https://logo.com',
            'team_ids': ["123e4567-e89b-12d3-a456-426614174000",
                         "123e4567-e89b-12d3-a456-426614174000"],
            "project_display_id": "display_id 1",
            'roles': [{
                'role_name': 'role1',
                'description': 'description1'
            }]
        }
        path_params = {}
        query_params = {}
        headers = {}
        self.make_api_call(body=body,
                           path_params=path_params,
                           query_params=query_params,
                           headers=headers,
                           snapshot=snapshot)

    @pytest.mark.django_db
    def test_given_invalid_team_ids_returns_invalid_team_ids_response(
            self, snapshot):
        body = {
            'name': "project_1",
            'description': 'project_description',
            'logo_url': 'https://logo.com',
            'team_ids': ["123e4567-e89b-12d3-a456-426614174000"],
            "project_display_id": "display_id 1",
            'roles': [{
                'role_name': 'role1',
                'description': 'description1'
            }]
        }
        path_params = {}
        query_params = {}
        headers = {}
        self.make_api_call(body=body,
                           path_params=path_params,
                           query_params=query_params,
                           headers=headers,
                           snapshot=snapshot)
