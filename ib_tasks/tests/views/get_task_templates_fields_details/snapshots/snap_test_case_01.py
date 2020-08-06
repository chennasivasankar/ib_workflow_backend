# -*- coding: utf-8 -*-
# snapshottest: v1 - https://goo.gl/zC4yUc
from __future__ import unicode_literals

from snapshottest import Snapshot

snapshots = Snapshot()

snapshots['TestCase01GetTaskTemplatesFieldsDetailsAPITestCase.test_case status_code'] = '200'

snapshots['TestCase01GetTaskTemplatesFieldsDetailsAPITestCase.test_case body'] = {
    'operators': [
        'GTE'
    ],
    'task_template_fields_details': [
        {
            'fields': [
                {
                    'field_id': 'string',
                    'name': 'string'
                }
            ],
            'name': 'string',
            'task_template_id': 'string'
        }
    ]
}
