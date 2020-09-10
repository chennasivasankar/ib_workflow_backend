# -*- coding: utf-8 -*-
# snapshottest: v1 - https://goo.gl/zC4yUc
from __future__ import unicode_literals

from snapshottest import Snapshot


snapshots = Snapshot()

snapshots['TestCase02AddTeamMemberLevelsAPITestCase.test_with_invalid_team_id_return_response status_code'] = '400'

snapshots['TestCase02AddTeamMemberLevelsAPITestCase.test_with_invalid_team_id_return_response body'] = {
    'http_status_code': 400,
    'res_status': 'INVALID_TEAM_ID',
    'response': 'Please send valid team id to add team member levels'
}

snapshots['TestCase02AddTeamMemberLevelsAPITestCase.test_with_duplicate_level_hierarchies_return_response status_code'] = '400'

snapshots['TestCase02AddTeamMemberLevelsAPITestCase.test_with_duplicate_level_hierarchies_return_response body'] = {
    'http_status_code': 400,
    'res_status': 'DUPLICATE_LEVEL_HIERARCHIES',
    'response': 'Please send unique level hierarchies, duplicate level hierarchies are [0, 2]'
}

snapshots['TestCase02AddTeamMemberLevelsAPITestCase.test_with_negative_level_hierarchies_return_response status_code'] = '400'

snapshots['TestCase02AddTeamMemberLevelsAPITestCase.test_with_negative_level_hierarchies_return_response body'] = {
    'http_status_code': 400,
    'res_status': 'NEGATIVE_LEVEL_HIERARCHIES',
    'response': 'Please send positive level hierarchies, negative level hierarchies are [-1, -2]'
}

snapshots['TestCase02AddTeamMemberLevelsAPITestCase.test_with_duplicate_level_names_return_response status_code'] = '400'

snapshots['TestCase02AddTeamMemberLevelsAPITestCase.test_with_duplicate_level_names_return_response body'] = {
    'http_status_code': 400,
    'res_status': 'DUPLICATE_TEAM_MEMBER_LEVEL_NAMES',
    'response': "Please send unique level names, duplicate team member level names are ['Developer']"
}

snapshots['TestCase02AddTeamMemberLevelsAPITestCase.test_with_user_is_not_admin_return_response status_code'] = '403'

snapshots['TestCase02AddTeamMemberLevelsAPITestCase.test_with_user_is_not_admin_return_response body'] = {
    'http_status_code': 403,
    'res_status': 'USER_DOES_NOT_HAVE_ACCESS',
    'response': 'User does not have provision to access'
}
