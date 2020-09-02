# -*- coding: utf-8 -*-
# snapshottest: v1 - https://goo.gl/zC4yUc
from __future__ import unicode_literals

from snapshottest import Snapshot


snapshots = Snapshot()

snapshots['TestCase01GetStageSearchablePossibleAssigneesOfATaskAPITestCase.test_case status_code'] = '200'

snapshots['TestCase01GetStageSearchablePossibleAssigneesOfATaskAPITestCase.test_case body'] = [
    {
        'id': 'user_1',
        'name': 'user_name_1',
        'profile_pic_url': 'profile_pic_1',
        'team_info': [
            {
                'team_id': 'team_1',
                'team_name': 'team_name1'
            },
            {
                'team_id': 'team_2',
                'team_name': 'team_name2'
            }
        ]
    },
    {
        'id': 'user_2',
        'name': 'user_name_2',
        'profile_pic_url': 'profile_pic_2',
        'team_info': [
            {
                'team_id': 'team_3',
                'team_name': 'team_name3'
            },
            {
                'team_id': 'team_4',
                'team_name': 'team_name4'
            }
        ]
    }
]
