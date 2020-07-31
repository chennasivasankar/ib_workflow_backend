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
                    'action_id': 1,
                    'button_color': '#fafafa',
                    'button_text': 'hey'
                },
                {
                    'action_id': 3,
                    'button_color': '#fafafa',
                    'button_text': 'hey'
                }
            ],
            'group_of_fields': [
                {
                    'enable_add_another': True,
                    'fields': [
                        {
                            'allowed_formats': None,
                            'display_name': 'DISPLAY_NAME-0',
                            'error_msg': None,
                            'field_id': 'FIELD_ID-0',
                            'field_type': 'PLAIN_TEXT',
                            'field_values': None,
                            'help_text': None,
                            'is_field_readable': True,
                            'is_field_required': True,
                            'is_field_writable': False,
                            'placeholder_text': None,
                            'tooltip': None,
                            'validation_regex': None
                        },
                        {
                            'allowed_formats': None,
                            'display_name': 'DISPLAY_NAME-4',
                            'error_msg': None,
                            'field_id': 'FIELD_ID-4',
                            'field_type': 'PLAIN_TEXT',
                            'field_values': None,
                            'help_text': None,
                            'is_field_readable': True,
                            'is_field_required': True,
                            'is_field_writable': False,
                            'placeholder_text': None,
                            'tooltip': None,
                            'validation_regex': None
                        }
                    ],
                    'gof_display_name': 'GOF_DISPLAY_NAME-0',
                    'gof_id': 'gof_1',
                    'max_columns': 2,
                    'order': 6
                },
                {
                    'enable_add_another': True,
                    'fields': [
                        {
                            'allowed_formats': None,
                            'display_name': 'DISPLAY_NAME-0',
                            'error_msg': None,
                            'field_id': 'FIELD_ID-0',
                            'field_type': 'PLAIN_TEXT',
                            'field_values': None,
                            'help_text': None,
                            'is_field_readable': True,
                            'is_field_required': True,
                            'is_field_writable': False,
                            'placeholder_text': None,
                            'tooltip': None,
                            'validation_regex': None
                        },
                        {
                            'allowed_formats': None,
                            'display_name': 'DISPLAY_NAME-4',
                            'error_msg': None,
                            'field_id': 'FIELD_ID-4',
                            'field_type': 'PLAIN_TEXT',
                            'field_values': None,
                            'help_text': None,
                            'is_field_readable': True,
                            'is_field_required': True,
                            'is_field_writable': False,
                            'placeholder_text': None,
                            'tooltip': None,
                            'validation_regex': None
                        }
                    ],
                    'gof_display_name': 'GOF_DISPLAY_NAME-0',
                    'gof_id': 'gof_1',
                    'max_columns': 2,
                    'order': 10
                },
                {
                    'enable_add_another': True,
                    'fields': [
                        {
                            'allowed_formats': None,
                            'display_name': 'DISPLAY_NAME-2',
                            'error_msg': None,
                            'field_id': 'FIELD_ID-2',
                            'field_type': 'PLAIN_TEXT',
                            'field_values': None,
                            'help_text': None,
                            'is_field_readable': True,
                            'is_field_required': True,
                            'is_field_writable': False,
                            'placeholder_text': None,
                            'tooltip': None,
                            'validation_regex': None
                        }
                    ],
                    'gof_display_name': 'GOF_DISPLAY_NAME-2',
                    'gof_id': 'gof_3',
                    'max_columns': 2,
                    'order': 8
                }
            ],
            'template_id': 'template_1',
            'template_name': 'Template 1'
        },
        {
            'actions': [
                {
                    'action_id': 2,
                    'button_color': '#fafafa',
                    'button_text': 'hey'
                },
                {
                    'action_id': 4,
                    'button_color': '#fafafa',
                    'button_text': 'hey'
                }
            ],
            'group_of_fields': [
                {
                    'enable_add_another': False,
                    'fields': [
                        {
                            'allowed_formats': None,
                            'display_name': 'DISPLAY_NAME-1',
                            'error_msg': None,
                            'field_id': 'FIELD_ID-1',
                            'field_type': 'PLAIN_TEXT',
                            'field_values': None,
                            'help_text': None,
                            'is_field_readable': False,
                            'is_field_required': True,
                            'is_field_writable': False,
                            'placeholder_text': None,
                            'tooltip': None,
                            'validation_regex': None
                        },
                        {
                            'allowed_formats': None,
                            'display_name': 'DISPLAY_NAME-5',
                            'error_msg': None,
                            'field_id': 'FIELD_ID-5',
                            'field_type': 'PLAIN_TEXT',
                            'field_values': None,
                            'help_text': None,
                            'is_field_readable': False,
                            'is_field_required': True,
                            'is_field_writable': False,
                            'placeholder_text': None,
                            'tooltip': None,
                            'validation_regex': None
                        }
                    ],
                    'gof_display_name': 'GOF_DISPLAY_NAME-1',
                    'gof_id': 'gof_2',
                    'max_columns': 2,
                    'order': 7
                },
                {
                    'enable_add_another': False,
                    'fields': [
                        {
                            'allowed_formats': None,
                            'display_name': 'DISPLAY_NAME-1',
                            'error_msg': None,
                            'field_id': 'FIELD_ID-1',
                            'field_type': 'PLAIN_TEXT',
                            'field_values': None,
                            'help_text': None,
                            'is_field_readable': False,
                            'is_field_required': True,
                            'is_field_writable': False,
                            'placeholder_text': None,
                            'tooltip': None,
                            'validation_regex': None
                        },
                        {
                            'allowed_formats': None,
                            'display_name': 'DISPLAY_NAME-5',
                            'error_msg': None,
                            'field_id': 'FIELD_ID-5',
                            'field_type': 'PLAIN_TEXT',
                            'field_values': None,
                            'help_text': None,
                            'is_field_readable': False,
                            'is_field_required': True,
                            'is_field_writable': False,
                            'placeholder_text': None,
                            'tooltip': None,
                            'validation_regex': None
                        }
                    ],
                    'gof_display_name': 'GOF_DISPLAY_NAME-1',
                    'gof_id': 'gof_2',
                    'max_columns': 2,
                    'order': 11
                },
                {
                    'enable_add_another': False,
                    'fields': [
                        {
                            'allowed_formats': None,
                            'display_name': 'DISPLAY_NAME-3',
                            'error_msg': None,
                            'field_id': 'FIELD_ID-3',
                            'field_type': 'PLAIN_TEXT',
                            'field_values': None,
                            'help_text': None,
                            'is_field_readable': False,
                            'is_field_required': True,
                            'is_field_writable': False,
                            'placeholder_text': None,
                            'tooltip': None,
                            'validation_regex': None
                        }
                    ],
                    'gof_display_name': 'GOF_DISPLAY_NAME-3',
                    'gof_id': 'gof_4',
                    'max_columns': 2,
                    'order': 9
                }
            ],
            'template_id': 'template_2',
            'template_name': 'Template 2'
        }
    ]
}