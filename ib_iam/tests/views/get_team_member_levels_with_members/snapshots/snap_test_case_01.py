# -*- coding: utf-8 -*-
# snapshottest: v1 - https://goo.gl/zC4yUc
from __future__ import unicode_literals

from snapshottest import Snapshot


snapshots = Snapshot()

snapshots['TestCase01GetTeamMemberLevelsWithMembersAPITestCase.test_with_valid_details_return_response status_code'] = '200'

snapshots['TestCase01GetTeamMemberLevelsWithMembersAPITestCase.test_with_valid_details_return_response body'] = {
    'team_member_levels_with_members': [
        {
            'level_details': {
                'level_hierarchy': 1,
                'team_member_level_id': '00be920b-7b4c-49e7-8adb-41a0c18da848',
                'team_member_level_name': 'SDL'
            },
            'level_members': [
                {
                    'immediate_subordinate_team_members': [
                        {
                            'member_id': '20be920b-7b4c-49e7-8adb-41a0c18da848',
                            'name': 'name',
                            'profile_pic_url': 'https://graph.ib_users.com/'
                        },
                        {
                            'member_id': '30be920b-7b4c-49e7-8adb-41a0c18da848',
                            'name': 'name',
                            'profile_pic_url': 'https://graph.ib_users.com/'
                        }
                    ],
                    'immediate_superior_team_user_id': None,
                    'member_id': '10be920b-7b4c-49e7-8adb-41a0c18da848',
                    'name': 'name',
                    'profile_pic_url': 'https://graph.ib_users.com/'
                },
                {
                    'immediate_subordinate_team_members': [
                        {
                            'member_id': '50be920b-7b4c-49e7-8adb-41a0c18da848',
                            'name': 'name',
                            'profile_pic_url': 'https://graph.ib_users.com/'
                        }
                    ],
                    'immediate_superior_team_user_id': '10be920b-7b4c-49e7-8adb-41a0c18da848',
                    'member_id': '20be920b-7b4c-49e7-8adb-41a0c18da848',
                    'name': 'name',
                    'profile_pic_url': 'https://graph.ib_users.com/'
                },
                {
                    'immediate_subordinate_team_members': [
                    ],
                    'immediate_superior_team_user_id': '10be920b-7b4c-49e7-8adb-41a0c18da848',
                    'member_id': '30be920b-7b4c-49e7-8adb-41a0c18da848',
                    'name': 'name',
                    'profile_pic_url': 'https://graph.ib_users.com/'
                }
            ]
        },
        {
            'level_details': {
                'level_hierarchy': 0,
                'team_member_level_id': '10be920b-7b4c-49e7-8adb-41a0c18da848',
                'team_member_level_name': 'Developer'
            },
            'level_members': [
                {
                    'immediate_subordinate_team_members': [
                    ],
                    'immediate_superior_team_user_id': None,
                    'member_id': '40be920b-7b4c-49e7-8adb-41a0c18da848',
                    'name': 'name',
                    'profile_pic_url': 'https://graph.ib_users.com/'
                },
                {
                    'immediate_subordinate_team_members': [
                    ],
                    'immediate_superior_team_user_id': '20be920b-7b4c-49e7-8adb-41a0c18da848',
                    'member_id': '50be920b-7b4c-49e7-8adb-41a0c18da848',
                    'name': 'name',
                    'profile_pic_url': 'https://graph.ib_users.com/'
                },
                {
                    'immediate_subordinate_team_members': [
                    ],
                    'immediate_superior_team_user_id': None,
                    'member_id': '60be920b-7b4c-49e7-8adb-41a0c18da848',
                    'name': 'name',
                    'profile_pic_url': 'https://graph.ib_users.com/'
                }
            ]
        }
    ]
}
