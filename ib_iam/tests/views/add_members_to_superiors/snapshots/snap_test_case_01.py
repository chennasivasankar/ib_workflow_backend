# -*- coding: utf-8 -*-
# snapshottest: v1 - https://goo.gl/zC4yUc
from __future__ import unicode_literals

from snapshottest import Snapshot


snapshots = Snapshot()

snapshots['TestCase01AddMembersToSuperiorsAPITestCase.test_case status_code'] = '201'

snapshots['TestCase01AddMembersToSuperiorsAPITestCase.test_case body'] = {
}

snapshots['TestCase01AddMembersToSuperiorsAPITestCase.test_case user_team'] = [
    {
        'id': 1,
        'immediate_superior_team_user_id': None,
        'team_member_level_id': '00be920b-7b4c-49e7-8adb-41a0c18da848',
        'user_id': '10be920b-7b4c-49e7-8adb-41a0c18da848'
    },
    {
        'id': 2,
        'immediate_superior_team_user_id': None,
        'team_member_level_id': '00be920b-7b4c-49e7-8adb-41a0c18da848',
        'user_id': '20be920b-7b4c-49e7-8adb-41a0c18da848'
    },
    {
        'id': 3,
        'immediate_superior_team_user_id': None,
        'team_member_level_id': '00be920b-7b4c-49e7-8adb-41a0c18da848',
        'user_id': '30be920b-7b4c-49e7-8adb-41a0c18da848'
    },
    {
        'id': 4,
        'immediate_superior_team_user_id': 1,
        'team_member_level_id': '10be920b-7b4c-49e7-8adb-41a0c18da848',
        'user_id': '40be920b-7b4c-49e7-8adb-41a0c18da848'
    },
    {
        'id': 5,
        'immediate_superior_team_user_id': 1,
        'team_member_level_id': '10be920b-7b4c-49e7-8adb-41a0c18da848',
        'user_id': '50be920b-7b4c-49e7-8adb-41a0c18da848'
    },
    {
        'id': 6,
        'immediate_superior_team_user_id': 2,
        'team_member_level_id': '10be920b-7b4c-49e7-8adb-41a0c18da848',
        'user_id': '60be920b-7b4c-49e7-8adb-41a0c18da848'
    }
]
