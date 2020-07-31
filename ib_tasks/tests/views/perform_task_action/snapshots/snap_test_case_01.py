# -*- coding: utf-8 -*-
# snapshottest: v1 - https://goo.gl/zC4yUc
from __future__ import unicode_literals

from snapshottest import Snapshot


snapshots = Snapshot()

snapshots['TestCase01PerformTaskActionAPITestCase.test_case status_code'] = '200'

snapshots['TestCase01PerformTaskActionAPITestCase.test_case body'] = {
    'current_board_details': {
        'board_id': 'string',
        'board_name': 'string',
        'column_details': [
            {
                'actions': [
                    {
                        'action_id': 'string',
                        'button_color': 'string',
                        'button_text': 'string',
                        'name': 'string'
                    }
                ],
                'column_id': 'string',
                'column_name': 'string',
                'fields': [
                    {
                        'field_type': 'string',
                        'key': 'string',
                        'value': 'string'
                    }
                ]
            }
        ]
    },
    'other_board_details': [
        {
            'board_id': 'string',
            'board_name': 'string',
            'column_details': [
                {
                    'column_id': 'string',
                    'column_name': 'string'
                }
            ]
        }
    ],
    'task_id': 'string'
}
