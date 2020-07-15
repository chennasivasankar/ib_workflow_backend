# -*- coding: utf-8 -*-
# snapshottest: v1 - https://goo.gl/zC4yUc
from __future__ import unicode_literals

from snapshottest import Snapshot


snapshots = Snapshot()

snapshots['TestGetResponseForGetListOfTeams.test_whether_it_returns_list_of_team_details_dict list_of_teams_details_dict'] = [
    {
        'description': 'team_desc1',
        'members': [
            {
                'member_id': '2bdb417e-4632-419a-8ddd-085ea272c6eb',
                'name': 'user1',
                'profile_pic_url': 'profile_pic_url1'
            },
            {
                'member_id': '548a803c-7b48-47ba-a700-24f2ea0d1280',
                'name': 'user2',
                'profile_pic_url': 'profile_pic_url2'
            },
            {
                'member_id': '4b8fb6eb-fa7d-47c1-8726-cd917901104e',
                'name': 'user3',
                'profile_pic_url': 'profile_pic_url3'
            }
        ],
        'name': 'team1',
        'no_of_members': 3,
        'team_id': 'f2c02d98-f311-4ab2-8673-3daa00757002'
    },
    {
        'description': 'team_desc2',
        'members': [
            {
                'member_id': '7ee2c7b4-34c8-4d65-a83a-f87da75db24e',
                'name': 'user4',
                'profile_pic_url': 'profile_pic_url4'
            },
            {
                'member_id': '2bdb417e-4632-419a-8ddd-085ea272c6eb',
                'name': 'user1',
                'profile_pic_url': 'profile_pic_url1'
            }
        ],
        'name': 'team2',
        'no_of_members': 2,
        'team_id': 'aa66c40f-6d93-484a-b418-984716514c7b'
    },
    {
        'description': 'team_desc3',
        'members': [
            {
                'member_id': '548a803c-7b48-47ba-a700-24f2ea0d1280',
                'name': 'user2',
                'profile_pic_url': 'profile_pic_url2'
            },
            {
                'member_id': '4b8fb6eb-fa7d-47c1-8726-cd917901104e',
                'name': 'user3',
                'profile_pic_url': 'profile_pic_url3'
            },
            {
                'member_id': '7ee2c7b4-34c8-4d65-a83a-f87da75db24e',
                'name': 'user4',
                'profile_pic_url': 'profile_pic_url4'
            }
        ],
        'name': 'team3',
        'no_of_members': 3,
        'team_id': 'c982032b-53a7-4dfa-a627-4701a5230765'
    }
]
