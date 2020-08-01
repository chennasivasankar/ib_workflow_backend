# -*- coding: utf-8 -*-
# snapshottest: v1 - https://goo.gl/zC4yUc
from __future__ import unicode_literals

from snapshottest import Snapshot


snapshots = Snapshot()

snapshots['TestCase03GetTaskAPITestCase.test_case status_code'] = '200'

snapshots['TestCase03GetTaskAPITestCase.test_case body'] = {
    'gofs': [
        {
            'gof_fields': [
                {
                    'field_id': 'FIELD_ID-0',
                    'field_response': 'field_response_0'
                },
                {
                    'field_id': 'FIELD_ID-3',
                    'field_response': 'field_response_3'
                },
                {
                    'field_id': 'FIELD_ID-6',
                    'field_response': 'field_response_6'
                },
                {
                    'field_id': 'FIELD_ID-9',
                    'field_response': 'field_response_9'
                }
            ],
            'gof_id': 'gof_1',
            'same_gof_order': 1.0
        },
        {
            'gof_fields': [
                {
                    'field_id': 'FIELD_ID-1',
                    'field_response': 'field_response_1'
                },
                {
                    'field_id': 'FIELD_ID-4',
                    'field_response': 'field_response_4'
                },
                {
                    'field_id': 'FIELD_ID-7',
                    'field_response': 'field_response_7'
                }
            ],
            'gof_id': 'gof_2',
            'same_gof_order': 1.0
        }
    ],
    'stages_with_actions': [
    ],
    'task_id': 1,
    'template_id': 'template_0'
}
