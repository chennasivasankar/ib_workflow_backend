# -*- coding: utf-8 -*-
# snapshottest: v1 - https://goo.gl/zC4yUc
from __future__ import unicode_literals

from snapshottest import Snapshot


snapshots = Snapshot()

snapshots['TestCase01GetTeamMemberLevelsAPITestCase.test_case status_code'] = '200'

snapshots['TestCase01GetTeamMemberLevelsAPITestCase.test_case body'] = {
    'levels': [
        {
            'level_hierarchy': 0,
            'team_member_level_id': '00be920b-7b4c-49e7-8adb-41a0c18da848',
            'team_member_level_name': 'Developer'
        },
        {
            'level_hierarchy': 1,
            'team_member_level_id': '01be920b-7b4c-49e7-8adb-41a0c18da848',
            'team_member_level_name': 'Software Developer Lead'
        },
        {
            'level_hierarchy': 2,
            'team_member_level_id': '02be920b-7b4c-49e7-8adb-41a0c18da848',
            'team_member_level_name': 'Engineer Manager'
        }
    ]
}
