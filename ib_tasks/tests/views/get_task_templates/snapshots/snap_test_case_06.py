# -*- coding: utf-8 -*-
# snapshottest: v1 - https://goo.gl/zC4yUc
from __future__ import unicode_literals

from snapshottest import Snapshot

snapshots = Snapshot()

snapshots['TestCase06GetTaskTemplatesAPITestCase.test_case status_code'] = '200'

snapshots['TestCase06GetTaskTemplatesAPITestCase.test_case body'] = [
    {
        'actions': [
            {
                'action_id': 1,
                'action_type': 'NO_VALIDATIONS',
                'button_color': '#fafafa',
                'button_text': 'hey',
                'transition_template_id': None
            },
            {
                'action_id': 3,
                'action_type': 'NO_VALIDATIONS',
                'button_color': '#fafafa',
                'button_text': 'hey',
                'transition_template_id': None
            }
        ],
        'group_of_fields': [
        ],
        'project_id': 'project_1',
        'stage_gofs': [
        ],
        'task_creation_gof_ids': [
        ],
        'template_id': 'template_1',
        'template_name': 'Template 1'
    },
    {
        'actions': [
            {
                'action_id': 2,
                'action_type': 'NO_VALIDATIONS',
                'button_color': '#fafafa',
                'button_text': 'hey',
                'transition_template_id': None
            },
            {
                'action_id': 4,
                'action_type': 'NO_VALIDATIONS',
                'button_color': '#fafafa',
                'button_text': 'hey',
                'transition_template_id': None
            }
        ],
        'group_of_fields': [
        ],
        'project_id': 'project_2',
        'stage_gofs': [
        ],
        'task_creation_gof_ids': [
        ],
        'template_id': 'template_2',
        'template_name': 'Template 2'
    }
]
