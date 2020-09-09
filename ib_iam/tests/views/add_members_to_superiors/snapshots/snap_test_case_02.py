# -*- coding: utf-8 -*-
# snapshottest: v1 - https://goo.gl/zC4yUc
from __future__ import unicode_literals

from snapshottest import Snapshot


snapshots = Snapshot()

snapshots['TestCase02AddMembersToSuperiorsAPITestCase.test_with_invalid_team_id_return_response status_code'] = '400'

snapshots['TestCase02AddMembersToSuperiorsAPITestCase.test_with_invalid_team_id_return_response body'] = {
    'http_status_code': 400,
    'res_status': 'INVALID_TEAM_ID',
    'response': 'Please send valid team id, to add members to superiors'
}

snapshots['TestCase02AddMembersToSuperiorsAPITestCase.test_invalid_level_hierarchy_of_team_return_response status_code'] = '400'

snapshots['TestCase02AddMembersToSuperiorsAPITestCase.test_invalid_level_hierarchy_of_team_return_response body'] = {
    'http_status_code': 400,
    'res_status': 'INVALID_LEVEL_HIERARCHY',
    'response': 'Please send valid level hierarchy of a team'
}

snapshots['TestCase02AddMembersToSuperiorsAPITestCase.test_team_member_ids_not_found_return_response status_code'] = '404'

snapshots['TestCase02AddMembersToSuperiorsAPITestCase.test_team_member_ids_not_found_return_response body'] = {
    'http_status_code': 404,
    'res_status': 'TEAM_MEMBER_IDS_NOT_FOUND',
    'response': "Please send valid member ids, invalid member ids are ['70be920b-7b4c-49e7-8adb-41a0c18da848']"
}

snapshots['TestCase02AddMembersToSuperiorsAPITestCase.test_subordinate_users_not_belong_to_team_member_level_return_response status_code'] = '404'

snapshots['TestCase02AddMembersToSuperiorsAPITestCase.test_subordinate_users_not_belong_to_team_member_level_return_response body'] = {
    'http_status_code': 404,
    'res_status': 'USERS_NOT_BELONG_TO_TEAM_MEMBER_LEVEL',
    'response': "Please send valid user ids, invalid user ids are ['40be920b-7b4c-49e7-8adb-41a0c18da848', '50be920b-7b4c-49e7-8adb-41a0c18da848', '60be920b-7b4c-49e7-8adb-41a0c18da848'] for level hierarchy is 1"
}

snapshots['TestCase02AddMembersToSuperiorsAPITestCase.test_superior_users_not_belong_to_team_member_level_return_response status_code'] = '404'

snapshots['TestCase02AddMembersToSuperiorsAPITestCase.test_superior_users_not_belong_to_team_member_level_return_response body'] = {
    'http_status_code': 404,
    'res_status': 'USERS_NOT_BELONG_TO_TEAM_MEMBER_LEVEL',
    'response': "Please send valid user ids, invalid user ids are ['10be920b-7b4c-49e7-8adb-41a0c18da848', '20be920b-7b4c-49e7-8adb-41a0c18da848'] for level hierarchy is 1"
}
