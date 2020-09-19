# -*- coding: utf-8 -*-
# snapshottest: v1 - https://goo.gl/zC4yUc
from __future__ import unicode_literals

from snapshottest import Snapshot

snapshots = Snapshot()

snapshots['TestCase02GetConfigurationDetailsAPITestCase.test_given_valid_details_returns_configuration_details_of_user status_code'] = '200'

snapshots['TestCase02GetConfigurationDetailsAPITestCase.test_given_valid_details_returns_configuration_details_of_user body'] = {
    'companies': [
        {
            'company_id': 'b9d000c7-c14f-4909-8c5a-6a6c02abb200',
            'company_name': 'company 0'
        }
    ],
    'roles': [
        {
            'role_id': 'b9d000c7-c14f-4909-8c5a-6a6c02abb211',
            'role_name': 'role 0'
        },
        {
            'role_id': 'b9d000c7-c14f-4909-8c5a-6a6c02abb222',
            'role_name': 'role 1'
        },
        {
            'role_id': 'b9d000c7-c14f-4909-8c5a-6a6c02abb233',
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
