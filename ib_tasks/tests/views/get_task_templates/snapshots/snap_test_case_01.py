# -*- coding: utf-8 -*-
# snapshottest: v1 - https://goo.gl/zC4yUc
from __future__ import unicode_literals

from snapshottest import Snapshot


snapshots = Snapshot()

snapshots['TestCase01GetTaskTemplatesAPITestCase.test_case status_code'] = '200'

snapshots['TestCase01GetTaskTemplatesAPITestCase.test_case body'] = {
    'task_templates': [
        {
            'actions': [
                {
                    'action_id': 'string',
                    'button_color': 'string',
                    'button_text': 'string'
                }
            ],
            'group_of_fields': [
                {
                    'enable_add_another': True,
                    'fields': [
                        {
                            'allowed_formats': 'string',
                            'display_name': 'string',
                            'error_msg': 'string',
                            'field_id': 'string',
                            'field_type': 'PLAIN_TEXT',
                            'field_values': 'string',
                            'help_text': 'string',
                            'is_field_readable': True,
                            'is_field_required': True,
                            'is_field_writable': True,
                            'placeholder_text': 'string',
                            'tooltip': 'string',
                            'validation_regex': 'string'
                        }
                    ],
                    'gof_display_name': 'string',
                    'gof_id': 'string',
                    'max_columns': 1,
                    'order': 1
                }
            ],
            'template_id': 'string',
            'template_name': 'string'
        }
    ]
}
