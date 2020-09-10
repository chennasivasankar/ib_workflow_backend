# -*- coding: utf-8 -*-
# snapshottest: v1 - https://goo.gl/zC4yUc
from __future__ import unicode_literals

from snapshottest import Snapshot


snapshots = Snapshot()

snapshots['TestCase02AssignUserRolesForGivenProjectBulkAPITestCase.test_with_invalid_user_ids_for_project status_code'] = '400'

snapshots['TestCase02AssignUserRolesForGivenProjectBulkAPITestCase.test_with_invalid_user_ids_for_project body'] = {
    'http_status_code': 400,
    'res_status': 'INVALID_USER_IDS_FOR_PROJECT',
    'response': "Please send valid user ids for project, invalid user ids are ['11be920b-7b4c-49e7-8adb-41a0c18da848', '01be920b-7b4c-49e7-8adb-41a0c18da848', '77be920b-7b4c-49e7-8adb-41a0c18da848']"
}

snapshots['TestCase02AssignUserRolesForGivenProjectBulkAPITestCase.test_with_invalid_project_id_return_response status_code'] = '400'

snapshots['TestCase02AssignUserRolesForGivenProjectBulkAPITestCase.test_with_invalid_project_id_return_response body'] = {
    'http_status_code': 400,
    'res_status': 'INVALID_PROJECT_ID',
    'response': 'Please send valid project id'
}

snapshots['TestCase02AssignUserRolesForGivenProjectBulkAPITestCase.test_with_invalid_role_ids_for_project status_code'] = '400'

snapshots['TestCase02AssignUserRolesForGivenProjectBulkAPITestCase.test_with_invalid_role_ids_for_project body'] = {
    'http_status_code': 400,
    'res_status': 'INVALID_ROLE_IDS_FOR_PROJECT',
    'response': "Please send valid role ids for project, invalid role ids are ['ROLE_10']"
}

snapshots['TestCase02AssignUserRolesForGivenProjectBulkAPITestCase.test_with_user_is_not_admin_return_response status_code'] = '403'

snapshots['TestCase02AssignUserRolesForGivenProjectBulkAPITestCase.test_with_user_is_not_admin_return_response body'] = {
    'http_status_code': 400,
    'res_status': 'USER_DOES_NOT_HAVE_ACCESS',
    'response': 'User does not have provision to access'
}
