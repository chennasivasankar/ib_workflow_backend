# -*- coding: utf-8 -*-
# snapshottest: v1 - https://goo.gl/zC4yUc
from __future__ import unicode_literals

from snapshottest import Snapshot


snapshots = Snapshot()

snapshots['TestCase40CreateTaskAPITestCase.test_case status_code'] = '201'

snapshots['TestCase40CreateTaskAPITestCase.test_case body'] = {
    'task_current_stages_details': {
        'stages': [
            {
                'stage_display_name': 'name_0',
                'stage_id': 'stage_1'
            }
        ],
        'task_id': 'IBWF-1',
        'user_has_permission': True
    },
    'task_details': {
        'stage_with_actions': {
            'actions': [
                {
                    'action_id': 1,
                    'action_type': 'NO_VALIDATIONS',
                    'button_color': '#fafafa',
                    'button_text': 'hey',
                    'transition_template_id': 'template_2'
                }
            ],
            'assignee': None,
            'stage_color': 'blue',
            'stage_display_name': 'name_0',
            'stage_id': 1
        },
        'task_id': 'IBWF-1',
        'task_overview_fields': [
        ]
    }
}
