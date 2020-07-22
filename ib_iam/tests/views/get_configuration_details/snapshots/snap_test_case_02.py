# -*- coding: utf-8 -*-
# snapshottest: v1 - https://goo.gl/zC4yUc
from __future__ import unicode_literals

from snapshottest import Snapshot


snapshots = Snapshot()

snapshots['TestCase02GetConfigurationDetailsAPITestCase.test_case status_code'] = '200'

snapshots['TestCase02GetConfigurationDetailsAPITestCase.test_case body'] = {
    'companies': [
        {
            'company_id': 'b9d000c7-c14f-4909-8c5a-6a6c02abb200',
            'company_name': 'company 0'
        },
        {
            'company_id': '0092d4c1-7a54-42d7-8b2c-b67ebd288c22',
            'company_name': 'company 0'
        },
        {
            'company_id': '1f497aa8-8855-47d5-9b75-3e8139e6f94e',
            'company_name': 'company 1'
        },
        {
            'company_id': '780bd052-5b9a-440c-a576-3f75f653f3bf',
            'company_name': 'company 2'
        },
        {
            'company_id': '4df60c98-529c-4117-b339-bdbbeec159fe',
            'company_name': 'company 3'
        },
        {
            'company_id': 'c301dcb7-2c64-40d1-ac24-46743bf63eea',
            'company_name': 'company 4'
        }
    ],
    'roles': [
        {
            'role_id': 'ROLE_0',
            'role_name': 'role 0'
        },
        {
            'role_id': 'ROLE_1',
            'role_name': 'role 1'
        },
        {
            'role_id': 'ROLE_2',
            'role_name': 'role 2'
        }
    ],
    'teams': [
        {
            'team_id': '6ce31e92-f188-4019-b295-2e5ddc9c7a11',
            'team_name': 'team 0'
        },
        {
            'team_id': '6ce31e92-f188-4019-b295-2e5ddc9c7a22',
            'team_name': 'team 1'
        },
        {
            'team_id': '6ce31e92-f188-4019-b295-2e5ddc9c7a33',
            'team_name': 'team 2'
        }
    ]
}
