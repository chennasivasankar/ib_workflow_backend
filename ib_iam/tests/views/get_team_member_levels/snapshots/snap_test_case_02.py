# -*- coding: utf-8 -*-
# snapshottest: v1 - https://goo.gl/zC4yUc
from __future__ import unicode_literals

from snapshottest import Snapshot


snapshots = Snapshot()

snapshots['TestCase02GetTeamMemberLevelsAPITestCase.test_invalid_team_id_return_response status_code'] = '400'

snapshots['TestCase02GetTeamMemberLevelsAPITestCase.test_invalid_team_id_return_response body'] = {
    'http_status_code': 400,
    'res_status': 'INVALID_TEAM_ID',
    'response': 'Please send valid team id to get team member level details'
}

snapshots['TestCase02GetTeamMemberLevelsAPITestCase.test_with_user_not_admin_return_response status_code'] = '403'

snapshots['TestCase02GetTeamMemberLevelsAPITestCase.test_with_user_not_admin_return_response body'] = {
    'http_status_code': 403,
    'res_status': 'USER_DOES_NOT_HAVE_ACCESS',
    'response': 'User does not have provision to access'
}
