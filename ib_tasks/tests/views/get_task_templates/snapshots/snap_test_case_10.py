# -*- coding: utf-8 -*-
# snapshottest: v1 - https://goo.gl/zC4yUc
from __future__ import unicode_literals

from snapshottest import Snapshot


snapshots = Snapshot()

snapshots['TestCase10GetTaskTemplatesAPITestCase.test_case status_code'] = '200'

snapshots['TestCase10GetTaskTemplatesAPITestCase.test_case body'] = [
    {
        'actions': [
            {
                'action_id': 1,
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
                    {
                        'allowed_formats': None,
                        'display_name': 'DISPLAY_NAME-0',
                        'error_msg': None,
                        'field_id': 'FIELD_ID-0',
                        'field_order': 0,
                        'field_type': 'PLAIN_TEXT',
                        'field_values': None,
                        'help_text': None,
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
                        'field_order': 4,
                        'field_type': 'PLAIN_TEXT',
                        'field_values': None,
                        'help_text': None,
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
                'order': 0
            },
            {
                'enable_add_another': True,
                'fields': [
                    {
                        'allowed_formats': None,
                        'display_name': 'DISPLAY_NAME-0',
                        'error_msg': None,
                        'field_id': 'FIELD_ID-0',
                        'field_order': 0,
                        'field_type': 'PLAIN_TEXT',
                        'field_values': None,
                        'help_text': None,
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
                        'field_order': 4,
                        'field_type': 'PLAIN_TEXT',
                        'field_values': None,
                        'help_text': None,
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
                'order': 4
            },
            {
                'enable_add_another': True,
                'fields': [
                    {
                        'allowed_formats': None,
                        'display_name': 'DISPLAY_NAME-2',
                        'error_msg': None,
                        'field_id': 'FIELD_ID-2',
                        'field_order': 2,
                        'field_type': 'PLAIN_TEXT',
                        'field_values': None,
                        'help_text': None,
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
                'order': 2
            }
        ],
        'project_id': None,
        'stage_gofs': [
            {
                'gof_ids': [
                    'gof_3'
                ],
                'stage_id': 3
            }
        ],
        'task_creation_gof_ids': [
            'gof_1'
        ],
        'template_id': 'template_1',
        'template_name': 'Template 1',
        'title_configuration': {
            'display_name': 'Title',
            'placeholder_text': 'Title'
        }
    },
    {
        'actions': [
            {
                'action_id': 2,
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
                    {
                        'allowed_formats': None,
                        'display_name': 'DISPLAY_NAME-1',
                        'error_msg': None,
                        'field_id': 'FIELD_ID-1',
                        'field_order': 1,
                        'field_type': 'PLAIN_TEXT',
                        'field_values': None,
                        'help_text': None,
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
                        'field_order': 5,
                        'field_type': 'PLAIN_TEXT',
                        'field_values': None,
                        'help_text': None,
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
                'order': 1
            },
            {
                'enable_add_another': False,
                'fields': [
                    {
                        'allowed_formats': None,
                        'display_name': 'DISPLAY_NAME-1',
                        'error_msg': None,
                        'field_id': 'FIELD_ID-1',
                        'field_order': 1,
                        'field_type': 'PLAIN_TEXT',
                        'field_values': None,
                        'help_text': None,
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
                        'field_order': 5,
                        'field_type': 'PLAIN_TEXT',
                        'field_values': None,
                        'help_text': None,
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
                'order': 5
            },
            {
                'enable_add_another': False,
                'fields': [
                    {
                        'allowed_formats': None,
                        'display_name': 'DISPLAY_NAME-3',
                        'error_msg': None,
                        'field_id': 'FIELD_ID-3',
                        'field_order': 3,
                        'field_type': 'PLAIN_TEXT',
                        'field_values': None,
                        'help_text': None,
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
                'order': 3
            }
        ],
        'project_id': None,
        'stage_gofs': [
            {
                'gof_ids': [
                    'gof_4'
                ],
                'stage_id': 4
            }
        ],
        'task_creation_gof_ids': [
            'gof_2'
        ],
        'template_id': 'template_2',
        'template_name': 'Template 2',
        'title_configuration': {
            'display_name': 'Title',
            'placeholder_text': 'Title'
        }
    }
]
