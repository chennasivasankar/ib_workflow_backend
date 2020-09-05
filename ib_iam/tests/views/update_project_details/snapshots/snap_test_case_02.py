# -*- coding: utf-8 -*-
# snapshottest: v1 - https://goo.gl/zC4yUc
from __future__ import unicode_literals

from snapshottest import Snapshot


snapshots = Snapshot()

snapshots['TestCase02UpdateProjectDetailsAPITestCase.test_given_user_is_not_admin_returns_user_has_no_access_response status_code'] = '401'

snapshots['TestCase02UpdateProjectDetailsAPITestCase.test_given_user_is_not_admin_returns_user_has_no_access_response body'] = {
    'http_status_code': 401,
    'res_status': 'USER_HAS_NO_ACCESS',
    'response': 'User has no access to add project'
}

snapshots['TestCase02UpdateProjectDetailsAPITestCase.test_given_project_name_already_exists_returns_name_already_exists_response status_code'] = '400'

snapshots['TestCase02UpdateProjectDetailsAPITestCase.test_given_project_name_already_exists_returns_name_already_exists_response body'] = {
    'http_status_code': 400,
    'res_status': 'PROJECT_NAME_ALREADY_EXISTS',
    'response': 'Given project name already exists, choose another'
}

snapshots['TestCase02UpdateProjectDetailsAPITestCase.test_given_duplicate_team_ids_returns_duplicate_team_ids_response status_code'] = '400'

snapshots['TestCase02UpdateProjectDetailsAPITestCase.test_given_duplicate_team_ids_returns_duplicate_team_ids_response body'] = {
    'http_status_code': 400,
    'res_status': 'DUPLICATE_TEAM_IDS',
    'response': 'Given team ids has duplicate entries'
}

snapshots['TestCase02UpdateProjectDetailsAPITestCase.test_given_invalid_team_ids_returns_invalid_team_ids_response status_code'] = '404'

snapshots['TestCase02UpdateProjectDetailsAPITestCase.test_given_invalid_team_ids_returns_invalid_team_ids_response body'] = {
    'http_status_code': 404,
    'res_status': 'INVALID_TEAM_IDS',
    'response': 'given team ids are invalid'
}

snapshots['TestCase02UpdateProjectDetailsAPITestCase.test_given_duplicate_role_ids_returns_duplicate_role_ids_response status_code'] = '400'

snapshots['TestCase02UpdateProjectDetailsAPITestCase.test_given_duplicate_role_ids_returns_duplicate_role_ids_response body'] = {
    'http_status_code': 400,
    'res_status': 'DUPLICATE_ROLE_IDS',
    'response': 'Duplicate roles has been given'
}

snapshots['TestCase02UpdateProjectDetailsAPITestCase.test_given_invalid_role_ids_returns_invalid_role_ids_response status_code'] = '404'

snapshots['TestCase02UpdateProjectDetailsAPITestCase.test_given_invalid_role_ids_returns_invalid_role_ids_response body'] = {
    'http_status_code': 404,
    'res_status': 'INVALID_ROLE_IDS',
    'response': 'given role ids are invalid'
}

snapshots['TestCase02UpdateProjectDetailsAPITestCase.test_given_duplicate_role_names_returns_duplicate_role_names_response status_code'] = '400'

snapshots['TestCase02UpdateProjectDetailsAPITestCase.test_given_duplicate_role_names_returns_duplicate_role_names_response body'] = {
    'http_status_code': 400,
    'res_status': 'DUPLICATE_ROLE_NAMES',
    'response': 'Duplicate role names has been given'
}

snapshots['TestCase02UpdateProjectDetailsAPITestCase.test_given_role_names_already_exists_returns_role_names_already_exists_response status_code'] = '400'

snapshots['TestCase02UpdateProjectDetailsAPITestCase.test_given_role_names_already_exists_returns_role_names_already_exists_response body'] = {
    'http_status_code': 400,
    'res_status': 'ROLE_NAMES_ALREADY_EXISTS',
    'response': "Role names ['role 2'] already exist"
}
