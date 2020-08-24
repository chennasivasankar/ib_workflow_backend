# -*- coding: utf-8 -*-
# snapshottest: v1 - https://goo.gl/zC4yUc
from __future__ import unicode_literals

from snapshottest import Snapshot


snapshots = Snapshot()

snapshots['TestGetUsersListPresenter.test_response_for_get_users get_users_response'] = {
    'total': 3,
    'users': [
        {
            'company': {
                'company_id': 'company1',
                'company_name': 'company 0'
            },
            'email': 'name0@gmail.com',
            'name': 'name0',
            'teams': [
                {
                    'team_id': 'team0',
                    'team_name': 'team 0'
                },
                {
                    'team_id': 'team1',
                    'team_name': 'team 1'
                }
            ],
            'user_id': 'user1'
        },
        {
            'company': {
                'company_id': 'company2',
                'company_name': 'company 1'
            },
            'email': 'name1@gmail.com',
            'name': 'name1',
            'teams': [
                {
                    'team_id': 'team2',
                    'team_name': 'team 2'
                },
                {
                    'team_id': 'team3',
                    'team_name': 'team 3'
                }
            ],
            'user_id': 'user2'
        },
        {
            'company': {
                'company_id': 'company3',
                'company_name': 'company 2'
            },
            'email': 'name2@gmail.com',
            'name': 'name2',
            'teams': [
                {
                    'team_id': 'team4',
                    'team_name': 'team 4'
                },
                {
                    'team_id': 'team5',
                    'team_name': 'team 5'
                }
            ],
            'user_id': 'user3'
        }
    ]
}
