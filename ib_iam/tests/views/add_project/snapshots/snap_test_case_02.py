# -*- coding: utf-8 -*-
# snapshottest: v1 - https://goo.gl/zC4yUc
from __future__ import unicode_literals

from snapshottest import Snapshot


snapshots = Snapshot()

snapshots['TestCase02AddProjectAPITestCase.test_given_project_name_already_exists_returns_name_already_exists_response status_code'] = '400'

snapshots['TestCase02AddProjectAPITestCase.test_given_project_name_already_exists_returns_name_already_exists_response body'] = {
    'http_status_code': 400,
    'res_status': 'PROJECT_NAME_ALREADY_EXISTS',
    'response': 'Given project name already exists, choose another'
}

snapshots['TestCase02AddProjectAPITestCase.test_given_project_display_id_already_exists_returns_display_id_already_exists_response status_code'] = '400'

snapshots['TestCase02AddProjectAPITestCase.test_given_project_display_id_already_exists_returns_display_id_already_exists_response body'] = {
    'http_status_code': 400,
    'res_status': 'PROJECT_DISPLAY_ID_ALREADY_EXISTS',
    'response': 'Given project display id already exists, choose another'
}

snapshots['TestCase02AddProjectAPITestCase.test_given_duplicate_team_ids_returns_duplicate_team_ids_response status_code'] = '400'

snapshots['TestCase02AddProjectAPITestCase.test_given_duplicate_team_ids_returns_duplicate_team_ids_response body'] = {
    'http_status_code': 400,
    'res_status': 'DUPLICATE_TEAM_IDS',
    'response': 'Given team ids has duplicate entries'
}

snapshots['TestCase02AddProjectAPITestCase.test_given_invalid_team_ids_returns_invalid_team_ids_response status_code'] = '404'

snapshots['TestCase02AddProjectAPITestCase.test_given_invalid_team_ids_returns_invalid_team_ids_response body'] = {
    'http_status_code': 404,
    'res_status': 'INVALID_TEAM_IDS',
    'response': 'given team ids are invalid'
}
