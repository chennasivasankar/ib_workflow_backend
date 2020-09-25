# -*- coding: utf-8 -*-
# snapshottest: v1 - https://goo.gl/zC4yUc
from __future__ import unicode_literals

from snapshottest import Snapshot


snapshots = Snapshot()

snapshots['TestCase01GetAdhocTaskTemplateFieldsAndGroupByAPITestCase.test_case status_code'] = '200'

snapshots['TestCase01GetAdhocTaskTemplateFieldsAndGroupByAPITestCase.test_case body'] = {
    'all_fields': [
        {
            'display_name': 'field_display_name0',
            'group_by_key': 'field_0'
        },
        {
            'display_name': 'field_display_name1',
            'group_by_key': 'field_1'
        }
    ],
    'group_by_fields': [
        {
            'display_name': 'ASSIGNEE',
            'group_by_id': 0,
            'group_by_key': 'ASSIGNEE',
            'order': 1
        },
        {
            'display_name': 'STAGE',
            'group_by_id': 1,
            'group_by_key': 'STAGE',
            'order': 2
        }
    ]
}
