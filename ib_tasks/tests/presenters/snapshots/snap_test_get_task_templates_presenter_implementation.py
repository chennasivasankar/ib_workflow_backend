# -*- coding: utf-8 -*-
# snapshottest: v1 - https://goo.gl/zC4yUc
from __future__ import unicode_literals

from snapshottest import Snapshot


snapshots = Snapshot()

snapshots['TestGetTaskPresenterImplementation.test_when_complete_task_template_details_exists task_template_1'] = {
    'actions': [
        {
            'action_id': 'action_1',
            'button_color': 'button_color_1',
            'button_text': 'button_text__1'
        },
        {
            'action_id': 'action_2',
            'button_color': 'button_color_2',
            'button_text': 'button_text__2'
        }
    ],
    'group_of_fields': [
        {
            'enable_add_another': True,
            'fields': [
                {
                    'allowed_formats': None,
                    'display_name': 'field name',
                    'error_msg': None,
                    'field_id': 'field_1',
                    'field_type': 'DROPDOWN',
                    'field_values': [
                        'Mr',
                        'Mrs',
                        'Ms'
                    ],
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
                    'display_name': 'field name',
                    'error_msg': None,
                    'field_id': 'field_3',
                    'field_type': 'DROPDOWN',
                    'field_values': [
                        'Mr',
                        'Mrs',
                        'Ms'
                    ],
                    'help_text': None,
                    'is_field_readable': True,
                    'is_field_required': True,
                    'is_field_writable': False,
                    'placeholder_text': None,
                    'tooltip': None,
                    'validation_regex': None
                }
            ],
            'gof_display_name': 'GOF_DISPLAY_NAME-1',
            'gof_id': 'gof_1',
            'max_columns': 2,
            'order': 0
        }
    ],
    'template_id': 'template_1',
    'template_name': 'Task Template 1'
}

snapshots['TestGetTaskPresenterImplementation.test_when_complete_task_template_details_exists task_template_2'] = {
    'actions': [
    ],
    'group_of_fields': [
        {
            'enable_add_another': False,
            'fields': [
                {
                    'allowed_formats': None,
                    'display_name': 'field name',
                    'error_msg': None,
                    'field_id': 'field_2',
                    'field_type': 'DROPDOWN',
                    'field_values': [
                        'Mr',
                        'Mrs',
                        'Ms'
                    ],
                    'help_text': None,
                    'is_field_readable': True,
                    'is_field_required': True,
                    'is_field_writable': True,
                    'placeholder_text': None,
                    'tooltip': None,
                    'validation_regex': None
                },
                {
                    'allowed_formats': None,
                    'display_name': 'field name',
                    'error_msg': None,
                    'field_id': 'field_4',
                    'field_type': 'DROPDOWN',
                    'field_values': [
                        'Mr',
                        'Mrs',
                        'Ms'
                    ],
                    'help_text': None,
                    'is_field_readable': True,
                    'is_field_required': True,
                    'is_field_writable': True,
                    'placeholder_text': None,
                    'tooltip': None,
                    'validation_regex': None
                }
            ],
            'gof_display_name': 'GOF_DISPLAY_NAME-2',
            'gof_id': 'gof_2',
            'max_columns': 2,
            'order': 1
        }
    ],
    'template_id': 'template_2',
    'template_name': 'Task Template 2'
}

snapshots['TestGetTaskPresenterImplementation.test_when_no_task_templates_exists_returns_empty_list task_templates'] = {
    'task_templates': [
    ]
}

snapshots['TestGetTaskPresenterImplementation.test_when_no_gofs_exists_returns_empty_gofs_list task_template_1'] = {
    'actions': [
        {
            'action_id': 'action_1',
            'button_color': 'button_color_1',
            'button_text': 'button_text__1'
        },
        {
            'action_id': 'action_2',
            'button_color': 'button_color_2',
            'button_text': 'button_text__2'
        }
    ],
    'group_of_fields': [
    ],
    'template_id': 'template_1',
    'template_name': 'Task Template 1'
}

snapshots['TestGetTaskPresenterImplementation.test_when_no_gofs_exists_returns_empty_gofs_list task_template_2'] = {
    'actions': [
    ],
    'group_of_fields': [
    ],
    'template_id': 'template_2',
    'template_name': 'Task Template 2'
}

snapshots['TestGetTaskPresenterImplementation.test_when_no_actions_for_user_exists_returns_empty_actions_list task_template_1'] = {
    'actions': [
    ],
    'group_of_fields': [
        {
            'enable_add_another': True,
            'fields': [
                {
                    'allowed_formats': None,
                    'display_name': 'field name',
                    'error_msg': None,
                    'field_id': 'field_1',
                    'field_type': 'DROPDOWN',
                    'field_values': [
                        'Mr',
                        'Mrs',
                        'Ms'
                    ],
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
                    'display_name': 'field name',
                    'error_msg': None,
                    'field_id': 'field_3',
                    'field_type': 'DROPDOWN',
                    'field_values': [
                        'Mr',
                        'Mrs',
                        'Ms'
                    ],
                    'help_text': None,
                    'is_field_readable': True,
                    'is_field_required': True,
                    'is_field_writable': False,
                    'placeholder_text': None,
                    'tooltip': None,
                    'validation_regex': None
                }
            ],
            'gof_display_name': 'GOF_DISPLAY_NAME-1',
            'gof_id': 'gof_1',
            'max_columns': 2,
            'order': 0
        }
    ],
    'template_id': 'template_1',
    'template_name': 'Task Template 1'
}

snapshots['TestGetTaskPresenterImplementation.test_when_no_actions_for_user_exists_returns_empty_actions_list task_template_2'] = {
    'actions': [
    ],
    'group_of_fields': [
        {
            'enable_add_another': False,
            'fields': [
                {
                    'allowed_formats': None,
                    'display_name': 'field name',
                    'error_msg': None,
                    'field_id': 'field_2',
                    'field_type': 'DROPDOWN',
                    'field_values': [
                        'Mr',
                        'Mrs',
                        'Ms'
                    ],
                    'help_text': None,
                    'is_field_readable': True,
                    'is_field_required': True,
                    'is_field_writable': True,
                    'placeholder_text': None,
                    'tooltip': None,
                    'validation_regex': None
                },
                {
                    'allowed_formats': None,
                    'display_name': 'field name',
                    'error_msg': None,
                    'field_id': 'field_4',
                    'field_type': 'DROPDOWN',
                    'field_values': [
                        'Mr',
                        'Mrs',
                        'Ms'
                    ],
                    'help_text': None,
                    'is_field_readable': True,
                    'is_field_required': True,
                    'is_field_writable': True,
                    'placeholder_text': None,
                    'tooltip': None,
                    'validation_regex': None
                }
            ],
            'gof_display_name': 'GOF_DISPLAY_NAME-2',
            'gof_id': 'gof_2',
            'max_columns': 2,
            'order': 1
        }
    ],
    'template_id': 'template_2',
    'template_name': 'Task Template 2'
}

snapshots['TestGetTaskPresenterImplementation.test_when_no_fields_exists_returns_empty_fields_list task_template_1'] = {
    'actions': [
        {
            'action_id': 'action_1',
            'button_color': 'button_color_1',
            'button_text': 'button_text__1'
        },
        {
            'action_id': 'action_2',
            'button_color': 'button_color_2',
            'button_text': 'button_text__2'
        }
    ],
    'group_of_fields': [
        {
            'enable_add_another': True,
            'fields': [
            ],
            'gof_display_name': 'GOF_DISPLAY_NAME-1',
            'gof_id': 'gof_1',
            'max_columns': 2,
            'order': 0
        }
    ],
    'template_id': 'template_1',
    'template_name': 'Task Template 1'
}

snapshots['TestGetTaskPresenterImplementation.test_when_no_fields_exists_returns_empty_fields_list task_template_2'] = {
    'actions': [
    ],
    'group_of_fields': [
        {
            'enable_add_another': False,
            'fields': [
            ],
            'gof_display_name': 'GOF_DISPLAY_NAME-2',
            'gof_id': 'gof_2',
            'max_columns': 2,
            'order': 1
        }
    ],
    'template_id': 'template_2',
    'template_name': 'Task Template 2'
}
