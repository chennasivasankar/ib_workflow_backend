# -*- coding: utf-8 -*-
# snapshottest: v1 - https://goo.gl/zC4yUc
from __future__ import unicode_literals

from snapshottest import Snapshot


snapshots = Snapshot()

snapshots['TestCase08GetTransitionTemplateAPITestCase.test_case status_code'] = '200'

snapshots['TestCase08GetTransitionTemplateAPITestCase.test_case body'] = {
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
                    'is_field_required': True,
                    'is_field_writable': True,
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
                    'is_field_required': True,
                    'is_field_writable': True,
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
                    'is_field_required': True,
                    'is_field_writable': True,
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
                    'is_field_required': True,
                    'is_field_writable': True,
                    'placeholder_text': None,
                    'tooltip': None,
                    'validation_regex': None
                }
            ],
            'gof_display_name': 'GOF_DISPLAY_NAME-1',
            'gof_id': 'gof_2',
            'max_columns': 2,
            'order': 1
        }
    ],
    'transition_template_id': 'template_1',
    'transition_template_name': 'Template 1'
}
