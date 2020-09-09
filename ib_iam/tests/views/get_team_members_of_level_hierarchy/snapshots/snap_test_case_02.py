# -*- coding: utf-8 -*-
# snapshottest: v1 - https://goo.gl/zC4yUc
from __future__ import unicode_literals

from snapshottest import Snapshot


snapshots = Snapshot()

snapshots['TestCase02GetTeamMembersOfLevelHierarchyAPITestCase.test_invalid_team_id_return_response status_code'] = '400'

snapshots['TestCase02GetTeamMembersOfLevelHierarchyAPITestCase.test_invalid_team_id_return_response body'] = {
    'http_status_code': 400,
    'res_status': 'INVALID_TEAM_ID',
    'response': 'Please send valid team id to get team members of level hierarchy'
}

snapshots['TestCase02GetTeamMembersOfLevelHierarchyAPITestCase.test_invalid_level_hierarchy_of_team_return_response status_code'] = '400'

snapshots['TestCase02GetTeamMembersOfLevelHierarchyAPITestCase.test_invalid_level_hierarchy_of_team_return_response body'] = {
    'http_status_code': 400,
    'res_status': 'INVALID_LEVEL_HIERARCHY',
    'response': 'Please send valid level hierarchy to get team members of level hierarchy'
}

snapshots['TestCase02GetTeamMembersOfLevelHierarchyAPITestCase.test_with_user_not_admin_return_response status_code'] = '400'

snapshots['TestCase02GetTeamMembersOfLevelHierarchyAPITestCase.test_with_user_not_admin_return_response body'] = {
    'http_status_code': 400,
    'res_status': 'USER_DOES_NOT_HAVE_ACCESS',
    'response': 'User does not have provision to access'
}
