# -*- coding: utf-8 -*-
# snapshottest: v1 - https://goo.gl/zC4yUc
from __future__ import unicode_literals

from snapshottest import Snapshot


snapshots = Snapshot()

snapshots['TestCase01AddMembersToLevelsAPITestCase.test_add_members_to_team_member_levels status_code'] = '500'

snapshots['TestCase01AddMembersToLevelsAPITestCase.test_add_members_to_team_member_levels body'] = {
    'res_status': [
        '"l" is not a valid choice.'
    ]
}

snapshots['TestCase01AddMembersToLevelsAPITestCase.test_add_members_to_team_member_levels user_team_details'] = [
    {
        'team_member_level_id': 'None',
        'user_id': '31be920b-7b4c-49e7-8adb-41a0c18da848'
    },
    {
        'team_member_level_id': 'None',
        'user_id': '01be920b-7b4c-49e7-8adb-41a0c18da848'
    },
    {
        'team_member_level_id': 'None',
        'user_id': '77be920b-7b4c-49e7-8adb-41a0c18da848'
    },
    {
        'team_member_level_id': 'None',
        'user_id': '17be920b-7b4c-49e7-8adb-41a0c18da848'
    },
    {
        'team_member_level_id': 'None',
        'user_id': '27be920b-7b4c-49e7-8adb-41a0c18da848'
    },
    {
        'team_member_level_id': 'None',
        'user_id': '37be920b-7b4c-49e7-8adb-41a0c18da848'
    }
]
