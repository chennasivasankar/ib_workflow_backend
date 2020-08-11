# -*- coding: utf-8 -*-
# snapshottest: v1 - https://goo.gl/zC4yUc
from __future__ import unicode_literals

from snapshottest import Snapshot


snapshots = Snapshot()

snapshots['TestCase07GetTaskTemplatesAPITestCase.test_case status_code'] = '200'

snapshots['TestCase07GetTaskTemplatesAPITestCase.test_case body'] = {
    'task_templates': [
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
                {
                    'enable_add_another': True,
                    'fields': [
                    ],
                    'gof_display_name': 'GOF_DISPLAY_NAME-0',
                    'gof_id': 'gof_1',
                    'max_columns': 2,
                    'order': 0
                },
                {
                    'enable_add_another': True,
                    'fields': [
                    ],
                    'gof_display_name': 'GOF_DISPLAY_NAME-0',
                    'gof_id': 'gof_1',
                    'max_columns': 2,
                    'order': 4
                },
                {
                    'enable_add_another': True,
                    'fields': [
                    ],
                    'gof_display_name': 'GOF_DISPLAY_NAME-2',
                    'gof_id': 'gof_3',
                    'max_columns': 2,
                    'order': 2
                }
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
                {
                    'enable_add_another': False,
                    'fields': [
                    ],
                    'gof_display_name': 'GOF_DISPLAY_NAME-1',
                    'gof_id': 'gof_2',
                    'max_columns': 2,
                    'order': 1
                },
                {
                    'enable_add_another': False,
                    'fields': [
                    ],
                    'gof_display_name': 'GOF_DISPLAY_NAME-1',
                    'gof_id': 'gof_2',
                    'max_columns': 2,
                    'order': 5
                },
                {
                    'enable_add_another': False,
                    'fields': [
                    ],
                    'gof_display_name': 'GOF_DISPLAY_NAME-3',
                    'gof_id': 'gof_4',
                    'max_columns': 2,
                    'order': 3
                }
            ],
            'template_id': 'template_2',
            'template_name': 'Template 2'
        }
    ]
}
