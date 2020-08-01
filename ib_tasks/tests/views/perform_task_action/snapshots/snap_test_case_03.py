# -*- coding: utf-8 -*-
# snapshottest: v1 - https://goo.gl/zC4yUc
from __future__ import unicode_literals

from snapshottest import Snapshot


snapshots = Snapshot()

snapshots['TestCase03PerformTaskActionAPITestCase.test_case status_code'] = '200'

snapshots['TestCase03PerformTaskActionAPITestCase.test_case body'] = {
    'current_board_details': {
        'board_id': 'board__1',
        'board_name': 'name_1',
        'column_details': [
            {
                'actions': [
                ],
                'column_id': 'column_1',
                'column_name': 'name_1',
                'fields': [
                ]
            },
            {
                'actions': [
                    {
                        'action_id': '4',
                        'button_color': '#fafafa',
                        'button_text': 'hey',
                        'name': 'name_3'
                    },
                    {
                        'action_id': '7',
                        'button_color': '#fafafa',
                        'button_text': 'hey',
                        'name': 'name_6'
                    }
                ],
                'column_id': 'column_2',
                'column_name': 'name_2',
                'fields': [
                    {
                        'field_type': 'PLAIN_TEXT',
                        'key': 'DISPLAY_NAME-1',
                        'value': 'field_response_1'
                    },
                    {
                        'field_type': 'PLAIN_TEXT',
                        'key': 'DISPLAY_NAME-2',
                        'value': 'field_response_2'
                    }
                ]
            }
        ]
    },
    'other_board_details': [
    ],
    'task_id': '1'
}

snapshots['TestCase03PerformTaskActionAPITestCase.test_case deleted task stages'] = False

snapshots['TestCase03PerformTaskActionAPITestCase.test_case stage_id_0'] = 'stage_id_0'

snapshots['TestCase03PerformTaskActionAPITestCase.test_case stage_id_2'] = 'stage_id_2'
