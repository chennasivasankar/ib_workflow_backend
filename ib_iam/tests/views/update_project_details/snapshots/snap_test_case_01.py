# -*- coding: utf-8 -*-
# snapshottest: v1 - https://goo.gl/zC4yUc
from __future__ import unicode_literals

from snapshottest import Snapshot


snapshots = Snapshot()

snapshots['TestCase01UpdateProjectDetailsAPITestCase.test_case status_code'] = '200'

snapshots['TestCase01UpdateProjectDetailsAPITestCase.test_case body'] = {
}

snapshots['TestCase01UpdateProjectDetailsAPITestCase.test_case project_details'] = [
    {
        'description': None,
        'display_id': 'display_id 1',
        'logo_url': None,
        'name': 'payment_project',
        'project_id': 'project_1'
    }
]

snapshots['TestCase01UpdateProjectDetailsAPITestCase.test_case project_team_ids'] = [
    '89d96f4b-c19d-4e69-8eae-e818f3123b09',
    '89d96f4b-c19d-4e69-8eae-e818f3123b00'
]

snapshots['TestCase01UpdateProjectDetailsAPITestCase.test_case project_roles'] = [
    {
        'description': 'pay_1',
        'name': 'Payment_RP',
        'role_id': 'pay_role'
    },
    {
        'description': None,
        'name': 'finance_advisor',
        'role_id': 'role_7eb737be-810f-4580-83ea-ff4fa67edd22'
    }
]
