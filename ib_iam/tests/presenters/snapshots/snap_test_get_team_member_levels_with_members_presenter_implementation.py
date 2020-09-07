# -*- coding: utf-8 -*-
# snapshottest: v1 - https://goo.gl/zC4yUc
from __future__ import unicode_literals

from snapshottest import Snapshot


snapshots = Snapshot()

snapshots['TestGetTeamMemberLevelsWithMembersPresenterImplementation.test_prepare_success_response_for_team_member_levels_with_members complete_team_member_levels_details'] = {
    'team_member_levels_with_members': [
        {
            'level_details': {
                'level_hierarchy': 0,
                'team_member_level_id': 'd6264b89-df8d-4b08-9ce1-f61004a0fbcc',
                'team_member_level_name': 'Developer'
            },
            'level_members': [
                {
                    'immediate_subordinate_team_members': [
                    ],
                    'immediate_superior_team_user_id': 'bc96292f-0e09-46ec-b90f-bf28c09e9365',
                    'member_id': '2b8f68ed-82cb-47ea-bf92-5a970d0c1109',
                    'name': 'user_1',
                    'profile_pic_url': 'https://picsum.photos/200'
                },
                {
                    'immediate_subordinate_team_members': [
                    ],
                    'immediate_superior_team_user_id': 'bc96292f-0e09-46ec-b90f-bf28c09e9365',
                    'member_id': 'e5fd217b-a1c6-4b43-aea0-6e9cf17117a4',
                    'name': 'user_2',
                    'profile_pic_url': 'https://picsum.photos/200'
                },
                {
                    'immediate_subordinate_team_members': [
                    ],
                    'immediate_superior_team_user_id': '86de39e4-e85d-4650-b78e-65f9bdc69719',
                    'member_id': '216cc13f-5446-493b-a2f7-90aaaeecaef1',
                    'name': 'user_3',
                    'profile_pic_url': 'https://picsum.photos/200'
                }
            ]
        },
        {
            'level_details': {
                'level_hierarchy': 1,
                'team_member_level_id': '55b28aac-db47-44b4-a76a-c42084979a83',
                'team_member_level_name': 'SDL'
            },
            'level_members': [
                {
                    'immediate_subordinate_team_members': [
                        {
                            'member_id': '2b8f68ed-82cb-47ea-bf92-5a970d0c1109',
                            'name': 'user_1',
                            'profile_pic_url': 'https://picsum.photos/200'
                        },
                        {
                            'member_id': 'e5fd217b-a1c6-4b43-aea0-6e9cf17117a4',
                            'name': 'user_2',
                            'profile_pic_url': 'https://picsum.photos/200'
                        }
                    ],
                    'immediate_superior_team_user_id': '4b5fd9ba-64a2-4ee2-8868-5e1d00bd83c8',
                    'member_id': 'bc96292f-0e09-46ec-b90f-bf28c09e9365',
                    'name': 'user_4',
                    'profile_pic_url': 'https://picsum.photos/200'
                },
                {
                    'immediate_subordinate_team_members': [
                        {
                            'member_id': '216cc13f-5446-493b-a2f7-90aaaeecaef1',
                            'name': 'user_3',
                            'profile_pic_url': 'https://picsum.photos/200'
                        }
                    ],
                    'immediate_superior_team_user_id': '4b5fd9ba-64a2-4ee2-8868-5e1d00bd83c8',
                    'member_id': '86de39e4-e85d-4650-b78e-65f9bdc69719',
                    'name': 'user_5',
                    'profile_pic_url': 'https://picsum.photos/200'
                },
                {
                    'immediate_subordinate_team_members': [
                    ],
                    'immediate_superior_team_user_id': '4b5fd9ba-64a2-4ee2-8868-5e1d00bd83c8',
                    'member_id': 'a7178219-7559-45c4-8c90-d25807820f20',
                    'name': 'user_6',
                    'profile_pic_url': 'https://picsum.photos/200'
                }
            ]
        },
        {
            'level_details': {
                'level_hierarchy': 2,
                'team_member_level_id': 'a762f699-a9b4-42c7-82b8-b702296ff764',
                'team_member_level_name': 'PM'
            },
            'level_members': [
                {
                    'immediate_subordinate_team_members': [
                        {
                            'member_id': 'bc96292f-0e09-46ec-b90f-bf28c09e9365',
                            'name': 'user_4',
                            'profile_pic_url': 'https://picsum.photos/200'
                        },
                        {
                            'member_id': '86de39e4-e85d-4650-b78e-65f9bdc69719',
                            'name': 'user_5',
                            'profile_pic_url': 'https://picsum.photos/200'
                        },
                        {
                            'member_id': 'a7178219-7559-45c4-8c90-d25807820f20',
                            'name': 'user_6',
                            'profile_pic_url': 'https://picsum.photos/200'
                        }
                    ],
                    'immediate_superior_team_user_id': None,
                    'member_id': '4b5fd9ba-64a2-4ee2-8868-5e1d00bd83c8',
                    'name': 'user_6',
                    'profile_pic_url': 'https://picsum.photos/200'
                }
            ]
        }
    ]
}
