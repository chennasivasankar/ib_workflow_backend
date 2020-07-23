# -*- coding: utf-8 -*-
# snapshottest: v1 - https://goo.gl/zC4yUc
from __future__ import unicode_literals

from snapshottest import Snapshot

snapshots = Snapshot()

snapshots[
    'TestGetUserOptionsDetailsResponse.test_response_for_get_configuration_details user_options_details'] = {
    'companies': [
        {
            'company_id': 'Company0',
            'company_name': 'company 0'
        },
        {
            'company_id': 'Company1',
            'company_name': 'company 1'
        },
        {
            'company_id': 'Company2',
            'company_name': 'company 2'
        }
    ],
    'roles': [
        {
            'role_id': 'PAYMENT0',
            'role_name': 'payment0'
        },
        {
            'role_id': 'PAYMENT1',
            'role_name': 'payment1'
        },
        {
            'role_id': 'PAYMENT2',
            'role_name': 'payment2'
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
        },
        {
            'team_id': 'team2',
            'team_name': 'team 2'
        }
    ]
}
