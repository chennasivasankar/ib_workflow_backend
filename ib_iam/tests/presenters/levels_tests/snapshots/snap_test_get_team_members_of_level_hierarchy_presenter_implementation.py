# -*- coding: utf-8 -*-
# snapshottest: v1 - https://goo.gl/zC4yUc
from __future__ import unicode_literals

from snapshottest import Snapshot


snapshots = Snapshot()

snapshots['TestGetTeamMembersOfLevelHierarchyPresenterImplementation.test_prepare_success_response_for_get_team_members_of_level_hierarchy get_team_members'] = {
    'members': [
        {
            'immediate_superior_team_user_id': 'eabada6d-0f17-4638-af2e-abd2f4d11462',
            'member_id': 'e326eb71-0a81-4015-b7d0-caa2cccd338d',
            'name': 'user_1',
            'profile_pic_url': 'https://picsum.photos/200'
        },
        {
            'immediate_superior_team_user_id': '967c596a-3a2c-4de7-a09d-7d28a0796f2e',
            'member_id': 'f420d920-0393-4759-bf67-8e10bb7c44bf',
            'name': 'user_2',
            'profile_pic_url': 'https://picsum.photos/200'
        },
        {
            'immediate_superior_team_user_id': None,
            'member_id': '239b29fd-446a-450c-bf9d-f8c1e744ad58',
            'name': 'user_3',
            'profile_pic_url': 'https://picsum.photos/200'
        }
    ]
}
