# -*- coding: utf-8 -*-
# snapshottest: v1 - https://goo.gl/zC4yUc
from __future__ import unicode_literals

from snapshottest import Snapshot


snapshots = Snapshot()

snapshots['TestCase01GetTaskAPITestCase.test_case status_code'] = '200'

snapshots['TestCase01GetTaskAPITestCase.test_case body'] = {
    'gofs': [
        {
            'gof_fields': [
                {
                    'field_id': 'string',
                    'field_response_multiple_values': [
                        'string'
                    ],
                    'field_response_single_value': 'string',
                    'is_readable': True,
                    'is_writable': True
                }
            ],
            'gof_id': 'string'
        }
    ],
    'stages_with_actions': [
        {
            'actions': [
                {
                    'action_id': 'string',
                    'button_color': 'string',
                    'button_text': 'string'
                }
            ],
            'stage_display_name': 'string',
            'stage_id': 'string'
        }
    ],
    'task_id': 'string',
    'template_id': 'string'
}
