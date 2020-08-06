# -*- coding: utf-8 -*-
# snapshottest: v1 - https://goo.gl/zC4yUc
from __future__ import unicode_literals

from snapshottest import Snapshot


snapshots = Snapshot()

snapshots['TestCase01CreateFilterAPITestCase.test_case status_code'] = '201'

snapshots['TestCase01CreateFilterAPITestCase.test_case body'] = {
    'conditions': [
        {
            'field_id': 'FIELD_ID-0',
            'field_name': 'DISPLAY_NAME-0',
            'operator': 'EQ',
            'value': 'pavan'
        }
    ],
    'filter_id': 1,
    'name': 'My filter',
    'status': 'ENABLED',
    'template_id': 'template_1',
    'template_name': 'Template 1'
}
