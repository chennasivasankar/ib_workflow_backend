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
                'condition_id': 1,
                'field_id': 'FIELD_ID-1',
                'field_name': 'DISPLAY_NAME-1',
                'operator': 'GTE',
                'value': 'value_1'
            }
        ],
        'filter_id': 1,
        'name': 'filter_name_1',
        'status': 'ENABLED',
        'template_id': 'template_1',
        'template_name': 'Template 1'
    }
]
