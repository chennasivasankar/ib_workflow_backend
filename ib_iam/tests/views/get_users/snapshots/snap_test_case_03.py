# -*- coding: utf-8 -*-
# snapshottest: v1 - https://goo.gl/zC4yUc
from __future__ import unicode_literals

from snapshottest import Snapshot


snapshots = Snapshot()

snapshots['TestCase03GetUsersAPITestCase.test_case status_code'] = '200'

snapshots['TestCase03GetUsersAPITestCase.test_case body'] = {
    'total': 1,
    'users': [
        {
            'company': {
                'company_id': 'b9d000c7-c14f-4909-8c5a-6a6c02abb222',
                'company_name': 'company 0'
            },
            'email': 'name0@gmail.com',
            'name': 'name0',
            'roles': [
                {
                    'role_id': 'b9d000c7-c14f-4909-8c5a-6a6c02abb226',
                    'role_name': 'role 0'
                }
            ],
            'teams': [
                {
                    'team_id': '6ce31e92-f188-4019-b295-2e5ddc9c7a17',
                    'team_name': 'team 0'
                }
            ],
            'user_id': '7e39bf1c-f9a5-4e76-8451-b962ddd520fc'
        }
    ]
}
