# -*- coding: utf-8 -*-
# snapshottest: v1 - https://goo.gl/zC4yUc
from __future__ import unicode_literals

from snapshottest import Snapshot


snapshots = Snapshot()

snapshots['TestCase02GetTaskAPITestCase.test_case status_code'] = '200'

snapshots['TestCase02GetTaskAPITestCase.test_case body'] = {
    'gofs': [
        {
            'gof_fields': [
                {
                    'field_id': 'FIELD_ID-0',
                    'field_response': 'response'
                },
                {
                    'field_id': 'FIELD_ID-3',
                    'field_response': 'response'
                },
                {
                    'field_id': 'FIELD_ID-6',
                    'field_response': 'response'
                },
                {
                    'field_id': 'FIELD_ID-9',
                    'field_response': 'response'
                }
            ],
            'gof_id': 'gof_1',
            'same_gof_order': 1.0
        },
        {
            'gof_fields': [
                {
                    'field_id': 'FIELD_ID-1',
                    'field_response': 'response'
                },
                {
                    'field_id': 'FIELD_ID-4',
                    'field_response': 'response'
                },
                {
                    'field_id': 'FIELD_ID-7',
                    'field_response': 'response'
                }
            ],
            'gof_id': 'gof_2',
            'same_gof_order': 1.0
        }
    ],
    'stages_with_actions': [
        {
            'actions': [
                {
                    'action_id': '1',
                    'button_color': '#fafafa',
                    'button_text': 'hey'
                },
                {
                    'action_id': '11',
                    'button_color': '#fafafa',
                    'button_text': 'hey'
                }
            ],
            'stage_display_name': 'name_0',
            'stage_id': 'stage_id_0'
        },
        {
            'actions': [
                {
                    'action_id': '2',
                    'button_color': '#fafafa',
                    'button_text': 'hey'
                },
                {
                    'action_id': '12',
                    'button_color': '#fafafa',
                    'button_text': 'hey'
                }
            ],
            'stage_display_name': 'name_1',
            'stage_id': 'stage_id_1'
        },
        {
            'actions': [
                {
                    'action_id': '3',
                    'button_color': '#fafafa',
                    'button_text': 'hey'
                },
                {
                    'action_id': '13',
                    'button_color': '#fafafa',
                    'button_text': 'hey'
                }
            ],
            'stage_display_name': 'name_2',
            'stage_id': 'stage_id_2'
        }
    ],
    'task_id': '1',
    'template_id': 'task_template_id_1'
}
