# -*- coding: utf-8 -*-
# snapshottest: v1 - https://goo.gl/zC4yUc
from __future__ import unicode_literals

from snapshottest import Snapshot


snapshots = Snapshot()

snapshots['TestCase04GetUsersAPITestCase.test_case status_code'] = '500'

snapshots['TestCase04GetUsersAPITestCase.test_case body'] = {
    'users': [
        {
        },
        {
        },
        {
        },
        {
            'company': {
                'company_id': [
                    'Must be a valid UUID.'
                ]
            }
        },
        {
            'company': {
                'company_id': [
                    'Must be a valid UUID.'
                ]
            }
        }
    ]
}
