# -*- coding: utf-8 -*-
# snapshottest: v1 - https://goo.gl/zC4yUc
from __future__ import unicode_literals

from snapshottest import Snapshot


snapshots = Snapshot()

snapshots['TestGetUsersPresenter.test_response_for_get_users get_users_response'] = {
    'total': 3,
    'users': [
        {
            'company': {
                'company_id': 'company 0',
                'company_name': 'company1'
            },
            'email': 'name0@gmail.com',
            'name': 'name0',
            'roles': [
                {
                    'role_id': 'PAYMENT0',
                    'role_name': 'payment 0'
                },
                {
                    'role_id': 'PAYMENT1',
                    'role_name': 'payment 1'
                }
            ],
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
                'company_id': 'company 1',
                'company_name': 'company2'
            },
            'email': 'name1@gmail.com',
            'name': 'name1',
            'roles': [
                {
                    'role_id': 'PAYMENT2',
                    'role_name': 'payment 2'
                },
                {
                    'role_id': 'PAYMENT3',
                    'role_name': 'payment 3'
                }
            ],
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
                'company_id': 'company 2',
                'company_name': 'company3'
            },
            'email': 'name2@gmail.com',
            'name': 'name2',
            'roles': [
                {
                    'role_id': 'PAYMENT4',
                    'role_name': 'payment 4'
                },
                {
                    'role_id': 'PAYMENT5',
                    'role_name': 'payment 5'
                }
            ],
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
