# -*- coding: utf-8 -*-
# snapshottest: v1 - https://goo.gl/zC4yUc
from __future__ import unicode_literals

from snapshottest import Snapshot

snapshots = Snapshot()

snapshots['TestCase01GetFiltersAPITestCase.test_case status_code'] = '200'

snapshots['TestCase01GetFiltersAPITestCase.test_case body'] = [
    {
        'conditions': [
            {
                'field_id': 'string',
                'field_name': 'string',
                'operator': 'EQ',
                'value': 'string'
            }
        ],
        'filter_id': 1,
        'name': 'string',
        'template_id': 'string',
        'template_name': 'string'
    }
]
