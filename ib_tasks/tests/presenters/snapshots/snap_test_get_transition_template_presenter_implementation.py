# -*- coding: utf-8 -*-
# snapshottest: v1 - https://goo.gl/zC4yUc
from __future__ import unicode_literals

from snapshottest import Snapshot


snapshots = Snapshot()

snapshots['TestGetTransitionTemplatePresenterImplementation.test_raise_transition_template_does_not_exists_exception http_status_code'] = 404

snapshots['TestGetTransitionTemplatePresenterImplementation.test_raise_transition_template_does_not_exists_exception res_status'] = 'TRANSITION_TEMPLATE_DOES_NOT_EXISTS'

snapshots['TestGetTransitionTemplatePresenterImplementation.test_raise_transition_template_does_not_exists_exception response'] = 'Given invalid transition template Id: template_1, that does not exists'

snapshots['TestGetTransitionTemplatePresenterImplementation.test_when_complete_transition_template_details_exists transition_template'] = {
    'group_of_fields': [
        {
            'enable_add_another': True,
            'fields': [
                {
                    'allowed_formats': None,
                    'display_name': 'field name',
                    'error_msg': None,
                    'field_id': 'field_1',
                    'field_order': 1,
                    'field_type': 'DROPDOWN',
                    'field_values': [
                        'Mr',
                        'Mrs',
                        'Ms'
                    ],
                    'help_text': None,
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
                    'field_id': 'field_3',
                    'field_order': 3,
                    'field_type': 'DROPDOWN',
                    'field_values': [
                        'Mr',
                        'Mrs',
                        'Ms'
                    ],
                    'help_text': None,
                    'is_field_required': True,
                    'is_field_writable': True,
                    'placeholder_text': None,
                    'tooltip': None,
                    'validation_regex': None
                }
            ],
            'gof_display_name': 'GOF_DISPLAY_NAME-1',
            'gof_id': 'gof_1',
            'max_columns': 2,
            'order': 0
        },
        {
            'enable_add_another': False,
            'fields': [
                {
                    'allowed_formats': None,
                    'display_name': 'field name',
                    'error_msg': None,
                    'field_id': 'field_2',
                    'field_order': 2,
                    'field_type': 'DROPDOWN',
                    'field_values': [
                        'Mr',
                        'Mrs',
                        'Ms'
                    ],
                    'help_text': None,
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
                    'field_order': 4,
                    'field_type': 'DROPDOWN',
                    'field_values': [
                        'Mr',
                        'Mrs',
                        'Ms'
                    ],
                    'help_text': None,
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
    'transition_template_id': 'template_1',
    'transition_template_name': 'Task Template 1'
}

snapshots['TestGetTransitionTemplatePresenterImplementation.test_when_no_gofs_exists_returns_empty_gofs_list transition_template'] = {
    'group_of_fields': [
    ],
    'transition_template_id': 'template_1',
    'transition_template_name': 'Task Template 1'
}

snapshots['TestGetTransitionTemplatePresenterImplementation.test_when_no_fields_exists_returns_empty_fields_list transition_template'] = {
    'group_of_fields': [
        {
            'enable_add_another': True,
            'fields': [
            ],
            'gof_display_name': 'GOF_DISPLAY_NAME-1',
            'gof_id': 'gof_1',
            'max_columns': 2,
            'order': 0
        },
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
    'transition_template_id': 'template_1',
    'transition_template_name': 'Task Template 1'
}
