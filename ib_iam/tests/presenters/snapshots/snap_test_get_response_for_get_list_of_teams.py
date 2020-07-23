# -*- coding: utf-8 -*-
# snapshottest: v1 - https://goo.gl/zC4yUc
from __future__ import unicode_literals

from snapshottest import Snapshot


snapshots = Snapshot()

snapshots['TestGetResponseForGetListOfTeams.test_given_valid_team_with_members_details_dto_returns_http_response response'] = {
    'teams': [
        {
            'description': 'team_description1',
            'members': [
                {
                    'member_id': '548a803c-7b48-47ba-a700-24f2ea0d1280',
                    'name': 'user2',
                    'profile_pic_url': 'url2'
                },
                {
                    'member_id': '4b8fb6eb-fa7d-47c1-8726-cd917901104e',
                    'name': 'user3',
                    'profile_pic_url': 'url3'
                }
            ],
            'name': 'team1',
            'no_of_members': 2,
            'team_id': 'f2c02d98-f311-4ab2-8673-3daa00757002'
        },
        {
            'description': 'team_description2',
            'members': [
                {
                    'member_id': '2bdb417e-4632-419a-8ddd-085ea272c6eb',
                    'name': 'user1',
                    'profile_pic_url': 'url1'
                },
                {
                    'member_id': '548a803c-7b48-47ba-a700-24f2ea0d1280',
                    'name': 'user2',
                    'profile_pic_url': 'url2'
                }
            ],
            'name': 'team2',
            'no_of_members': 2,
            'team_id': 'aa66c40f-6d93-484a-b418-984716514c7b'
        },
        {
            'description': 'team_description3',
            'members': [
                {
                    'member_id': '2bdb417e-4632-419a-8ddd-085ea272c6eb',
                    'name': 'user1',
                    'profile_pic_url': 'url1'
                },
                {
                    'member_id': '4b8fb6eb-fa7d-47c1-8726-cd917901104e',
                    'name': 'user3',
                    'profile_pic_url': 'url3'
                }
            ],
            'name': 'team3',
            'no_of_members': 2,
            'team_id': 'c982032b-53a7-4dfa-a627-4701a5230765'
        }
    ],
    'total_teams_count': 3
}
