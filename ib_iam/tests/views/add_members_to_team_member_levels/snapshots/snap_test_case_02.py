# -*- coding: utf-8 -*-
# snapshottest: v1 - https://goo.gl/zC4yUc
from __future__ import unicode_literals

from snapshottest import Snapshot


snapshots = Snapshot()

snapshots['TestCase02AddMembersToLevelsAPITestCase.test_team_member_level_ids_not_found_return_response status_code'] = '404'

snapshots['TestCase02AddMembersToLevelsAPITestCase.test_team_member_level_ids_not_found_return_response body'] = {
    'http_status_code': 404,
    'res_status': 'TEAM_MEMBER_LEVEL_IDS_NOT_FOUND',
    'response': "Please send valid team member level ids, invalid team member level ids are ['91be920b-7b4c-49e7-8adb-41a0c18da848', '92be920b-7b4c-49e7-8adb-41a0c18da848']"
}

snapshots['TestCase02AddMembersToLevelsAPITestCase.test_invalid_team_id_return_response status_code'] = '400'

snapshots['TestCase02AddMembersToLevelsAPITestCase.test_invalid_team_id_return_response body'] = {
    'http_status_code': 400,
    'res_status': 'INVALID_TEAM_ID',
    'response': 'Please send valid team id to add members to team member levels'
}

snapshots['TestCase02AddMembersToLevelsAPITestCase.test_team_member_ids_not_found_return_response status_code'] = '404'

snapshots['TestCase02AddMembersToLevelsAPITestCase.test_team_member_ids_not_found_return_response body'] = {
    'http_status_code': 404,
    'res_status': 'TEAM_MEMBER_IDS_NOT_FOUND',
    'response': "Please send valid team member ids, invalid team member ids are ['97be920b-7b4c-49e7-8adb-41a0c18da848', '97be920b-7b4c-49e7-8adb-41a0c18da848']"
}

snapshots['TestCase02AddMembersToLevelsAPITestCase.test_with_user_is_not_admin_return_response status_code'] = '403'

snapshots['TestCase02AddMembersToLevelsAPITestCase.test_with_user_is_not_admin_return_response body'] = {
    'http_status_code': 403,
    'res_status': 'USER_DOES_NOT_HAVE_ACCESS',
    'response': 'User does not have provision to access'
}
