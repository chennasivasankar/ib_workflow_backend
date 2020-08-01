# -*- coding: utf-8 -*-
# snapshottest: v1 - https://goo.gl/zC4yUc
from __future__ import unicode_literals

from snapshottest import Snapshot


snapshots = Snapshot()

snapshots['TestCase04GetAllTasksOverviewAPITestCase.test_case status_code'] = '200'

snapshots['TestCase04GetAllTasksOverviewAPITestCase.test_case body'] = {
    'tasks': [
        {
            'stage_with_actions': {
                'actions': [
                    {
                        'action_id': 1,
                        'button_color': '#fafafa',
                        'button_text': 'hey'
                    }
                ],
                'stage_display_name': 'name_2',
                'stage_id': 'stage_id_2'
            },
            'task_id': '1',
            'task_overview_fields': [
                {
                    'field_display_name': 'DISPLAY_NAME-1',
                    'field_response': 'field_response_1',
                    'field_type': 'PLAIN_TEXT'
                },
                {
                    'field_display_name': 'DISPLAY_NAME-2',
                    'field_response': 'field_response_2',
                    'field_type': 'PLAIN_TEXT'
                }
            ]
        },
        {
            'stage_with_actions': {
                'actions': [
                    {
                        'action_id': 2,
                        'button_color': '#fafafa',
                        'button_text': 'hey'
                    }
                ],
                'stage_display_name': 'name_3',
                'stage_id': 'stage_id_3'
            },
            'task_id': '2',
            'task_overview_fields': [
                {
                    'field_display_name': 'DISPLAY_NAME-1',
                    'field_response': 'field_response_1',
                    'field_type': 'PLAIN_TEXT'
                },
                {
                    'field_display_name': 'DISPLAY_NAME-2',
                    'field_response': 'field_response_2',
                    'field_type': 'PLAIN_TEXT'
                }
            ]
        },
        {
            'stage_with_actions': {
                'actions': [
                    {
                        'action_id': 3,
                        'button_color': '#fafafa',
                        'button_text': 'hey'
                    }
                ],
                'stage_display_name': 'name_4',
                'stage_id': 'stage_id_4'
            },
            'task_id': '3',
            'task_overview_fields': [
                {
                    'field_display_name': 'DISPLAY_NAME-1',
                    'field_response': 'field_response_1',
                    'field_type': 'PLAIN_TEXT'
                },
                {
                    'field_display_name': 'DISPLAY_NAME-2',
                    'field_response': 'field_response_2',
                    'field_type': 'PLAIN_TEXT'
                }
            ]
        }
    ],
    'total_tasks': 3
}
