# -*- coding: utf-8 -*-
# snapshottest: v1 - https://goo.gl/zC4yUc
from __future__ import unicode_literals

from snapshottest import Snapshot


snapshots = Snapshot()

snapshots['TestCase04GetUsersAPITestCase.test_case status_code'] = '200'

snapshots['TestCase04GetUsersAPITestCase.test_case body'] = {
    'total': 5,
    'users': [
        {
            'company': {
                'company_id': 'b9d000c7-c14f-4909-8c5a-6a6c02abb200',
                'company_name': 'company 0'
            },
            'email': 'name0@gmail.com',
            'name': 'name0',
            'roles': [
                {
                    'role_id': 'ROLE_0',
                    'role_name': 'role 0'
                }
            ],
            'teams': [
                {
                    'team_id': '6ce31e92-f188-4019-b295-2e5ddc9c7a11',
                    'team_name': 'team 0'
                }
            ],
            'user_id': '7e39bf1c-f9a5-4e76-8451-b962ddd52011'
        },
        {
            'company': {
                'company_id': 'b9d000c7-c14f-4909-8c5a-6a6c02abb200',
                'company_name': 'company 0'
            },
            'email': 'name1@gmail.com',
            'name': 'name1',
            'roles': [
            ],
            'teams': [
            ],
            'user_id': '7e39bf1c-f9a5-4e76-8451-b962ddd52122'
        },
        {
            'company': {
                'company_id': 'b9d000c7-c14f-4909-8c5a-6a6c02abb200',
                'company_name': 'company 0'
            },
            'email': 'name2@gmail.com',
            'name': 'name2',
            'roles': [
            ],
            'teams': [
                {
                    'team_id': '6ce31e92-f188-4019-b295-2e5ddc9c7a22',
                    'team_name': 'team 1'
                }
            ],
            'user_id': '7e39bf1c-f9a5-4e76-8451-b962ddd52033'
        },
        {
            'company': {
                'company_id': '',
                'company_name': ''
            },
            'email': 'name3@gmail.com',
            'name': 'name3',
            'roles': [
            ],
            'teams': [
            ],
            'user_id': 'b9d000c7-c14f-4909-8c5a-6a6c02abb300'
        },
        {
            'company': {
                'company_id': '',
                'company_name': ''
            },
            'email': 'name4@gmail.com',
            'name': 'name4',
            'roles': [
                {
                    'role_id': 'ROLE_0',
                    'role_name': 'role 0'
                }
            ],
            'teams': [
                {
                    'team_id': '6ce31e92-f188-4019-b295-2e5ddc9c7a11',
                    'team_name': 'team 0'
                }
            ],
            'user_id': 'b9d000c7-c14f-4909-8c5a-6a6c02abb600'
        }
    ]
}
