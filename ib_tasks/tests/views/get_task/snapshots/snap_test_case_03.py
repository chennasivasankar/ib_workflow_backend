# -*- coding: utf-8 -*-
# snapshottest: v1 - https://goo.gl/zC4yUc
from __future__ import unicode_literals

from snapshottest import Snapshot


snapshots = Snapshot()

snapshots['TestCase03GetTaskAPITestCase.test_case status_code'] = '200'

snapshots['TestCase03GetTaskAPITestCase.test_case body'] = {
    'description': 'description_0',
    'due_date': '2020-10-22 04:40:00',
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
            'same_gof_order': 1
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
            'same_gof_order': 1
        }
    ],
    'priority': 'HIGH',
    'stages_with_actions': [
    ],
    'start_date': '2020-10-12 04:40:00',
    'task_id': 'IBWF-1',
    'template_id': 'template_0',
    'title': 'title_0'
}
