# -*- coding: utf-8 -*-
# snapshottest: v1 - https://goo.gl/zC4yUc
from __future__ import unicode_literals

from snapshottest import Snapshot


snapshots = Snapshot()

snapshots['TestCase04GetTaskTemplatesAPITestCase.test_case status_code'] = '200'

snapshots['TestCase04GetTaskTemplatesAPITestCase.test_case body'] = {
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
            'template_id': 'template_2',
            'template_name': 'Template 2'
        }
    ]
}
