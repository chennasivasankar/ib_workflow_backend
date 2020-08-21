# -*- coding: utf-8 -*-
# snapshottest: v1 - https://goo.gl/zC4yUc
from __future__ import unicode_literals

from snapshottest import Snapshot


snapshots = Snapshot()

snapshots['TestCase01GetTeamMembersOfLevelHierarchyAPITestCase.test_with_members_in_a_team status_code'] = '200'

snapshots['TestCase01GetTeamMembersOfLevelHierarchyAPITestCase.test_with_members_in_a_team body'] = {
    'members': [
        {
            'immediate_superior_team_user_id': None,
            'member_id': '40be920b-7b4c-49e7-8adb-41a0c18da848',
            'name': 'name',
            'profile_pic_url': 'https://graph.ib_users.com/'
        },
        {
            'immediate_superior_team_user_id': None,
            'member_id': '50be920b-7b4c-49e7-8adb-41a0c18da848',
            'name': 'name',
            'profile_pic_url': 'https://graph.ib_users.com/'
        },
        {
            'immediate_superior_team_user_id': None,
            'member_id': '60be920b-7b4c-49e7-8adb-41a0c18da848',
            'name': 'name',
            'profile_pic_url': 'https://graph.ib_users.com/'
        }
    ]
}
