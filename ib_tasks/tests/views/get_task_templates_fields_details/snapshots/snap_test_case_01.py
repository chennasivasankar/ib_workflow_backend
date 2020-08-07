# -*- coding: utf-8 -*-
# snapshottest: v1 - https://goo.gl/zC4yUc
from __future__ import unicode_literals

from snapshottest import Snapshot

snapshots = Snapshot()

snapshots['TestCase01GetTaskTemplatesFieldsDetailsAPITestCase.test_case status_code'] = '200'

snapshots['TestCase01GetTaskTemplatesFieldsDetailsAPITestCase.test_case body'] = {
    'operators': [
        'GTE',
        'LTE',
        'GT',
        'LE',
        'NE',
        'EQ',
        'CONTAINS'
    ],
    'task_template_fields_details': [
        {
            'fields': [
                {
                    'field_id': 'FIELD_ID-0',
                    'name': 'DISPLAY_NAME-0'
                },
                {
                    'field_id': 'FIELD_ID-4',
                    'name': 'DISPLAY_NAME-4'
                },
                {
                    'field_id': 'FIELD_ID-2',
                    'name': 'DISPLAY_NAME-2'
                }
            ],
            'name': 'Template 1',
            'task_template_id': 'template_1'
        },
        {
            'fields': [
                {
                    'field_id': 'FIELD_ID-1',
                    'name': 'DISPLAY_NAME-1'
                },
                {
                    'field_id': 'FIELD_ID-5',
                    'name': 'DISPLAY_NAME-5'
                },
                {
                    'field_id': 'FIELD_ID-3',
                    'name': 'DISPLAY_NAME-3'
                }
            ],
            'name': 'Template 2',
            'task_template_id': 'template_2'
        }
    ]
}
