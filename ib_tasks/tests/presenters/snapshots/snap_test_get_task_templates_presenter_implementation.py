# -*- coding: utf-8 -*-
# snapshottest: v1 - https://goo.gl/zC4yUc
from __future__ import unicode_literals

from snapshottest import Snapshot


snapshots = Snapshot()

snapshots['TestGetTaskTemplatesPresenterImplementation.test_when_complete_task_template_details_exists task_template_1'] = {
    'actions': [
        {
            'action_id': 1,
            'action_type': 'NO_VALIDATIONS',
            'button_color': 'button_color_1',
            'button_text': 'button_text__1',
            'transition_template_id': 'transition_template_1'
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
                    'field_order': 1,
                    'field_type': 'DROPDOWN',
                    'field_values': [
                        'Mr',
                        'Mrs',
                        'Ms'
                    ],
                    'help_text': None,
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
    'project_id': 'project_1',
    'stage_gofs': [
        {
            'gof_ids': [
                'gof_1'
            ],
            'stage_id': 3
        }
    ],
    'task_creation_gof_ids': [
        'gof_1'
    ],
    'template_id': 'template_1',
    'template_name': 'Task Template 1',
    'title': {
        'display_name': 'title_display_name_1',
        'placeholder_text': 'title_placeholder_text_1'
    }
}

snapshots['TestGetTaskTemplatesPresenterImplementation.test_when_complete_task_template_details_exists task_template_2'] = {
    'actions': [
        {
            'action_id': 2,
            'action_type': 'NO_VALIDATIONS',
            'button_color': 'button_color_2',
            'button_text': 'button_text__2',
            'transition_template_id': 'transition_template_2'
        }
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
                }
            ],
            'gof_display_name': 'GOF_DISPLAY_NAME-2',
            'gof_id': 'gof_2',
            'max_columns': 2,
            'order': 1
        }
    ],
    'project_id': 'project_2',
    'stage_gofs': [
        {
            'gof_ids': [
                'gof_2'
            ],
            'stage_id': 4
        }
    ],
    'task_creation_gof_ids': [
        'gof_2'
    ],
    'template_id': 'template_2',
    'template_name': 'Task Template 2',
    'title': {
        'display_name': 'title_display_name_2',
        'placeholder_text': 'title_placeholder_text_2'
    }
}

snapshots['TestGetTaskTemplatesPresenterImplementation.test_raise_task_templates_does_not_exists_exception http_status_code'] = 404

snapshots['TestGetTaskTemplatesPresenterImplementation.test_raise_task_templates_does_not_exists_exception res_status'] = 'TASK_TEMPLATES_DOES_NOT_EXISTS'

snapshots['TestGetTaskTemplatesPresenterImplementation.test_raise_task_templates_does_not_exists_exception response'] = 'No Task Templates are exists'

snapshots['TestGetTaskTemplatesPresenterImplementation.test_when_no_task_templates_exists_returns_empty_list task_templates'] = [
]

snapshots['TestGetTaskTemplatesPresenterImplementation.test_when_no_gofs_exists_returns_empty_gofs_list task_template_1'] = {
    'actions': [
        {
            'action_id': 1,
            'action_type': 'NO_VALIDATIONS',
            'button_color': 'button_color_1',
            'button_text': 'button_text__1',
            'transition_template_id': 'transition_template_1'
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
    'template_name': 'Task Template 1',
    'title': {
        'display_name': 'title_display_name_1',
        'placeholder_text': 'title_placeholder_text_1'
    }
}

snapshots['TestGetTaskTemplatesPresenterImplementation.test_when_no_gofs_exists_returns_empty_gofs_list task_template_2'] = {
    'actions': [
        {
            'action_id': 2,
            'action_type': 'NO_VALIDATIONS',
            'button_color': 'button_color_2',
            'button_text': 'button_text__2',
            'transition_template_id': 'transition_template_2'
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
    'template_name': 'Task Template 2',
    'title': {
        'display_name': 'title_display_name_2',
        'placeholder_text': 'title_placeholder_text_2'
    }
}

snapshots['TestGetTaskTemplatesPresenterImplementation.test_when_no_fields_exists_returns_empty_fields_list task_template_1'] = {
    'actions': [
        {
            'action_id': 1,
            'action_type': 'NO_VALIDATIONS',
            'button_color': 'button_color_1',
            'button_text': 'button_text__1',
            'transition_template_id': 'transition_template_1'
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
    'project_id': 'project_1',
    'stage_gofs': [
        {
            'gof_ids': [
                'gof_1'
            ],
            'stage_id': 3
        }
    ],
    'task_creation_gof_ids': [
        'gof_1'
    ],
    'template_id': 'template_1',
    'template_name': 'Task Template 1',
    'title': {
        'display_name': 'title_display_name_1',
        'placeholder_text': 'title_placeholder_text_1'
    }
}

snapshots['TestGetTaskTemplatesPresenterImplementation.test_when_no_fields_exists_returns_empty_fields_list task_template_2'] = {
    'actions': [
        {
            'action_id': 2,
            'action_type': 'NO_VALIDATIONS',
            'button_color': 'button_color_2',
            'button_text': 'button_text__2',
            'transition_template_id': 'transition_template_2'
        }
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
    'project_id': 'project_2',
    'stage_gofs': [
        {
            'gof_ids': [
                'gof_2'
            ],
            'stage_id': 4
        }
    ],
    'task_creation_gof_ids': [
        'gof_2'
    ],
    'template_id': 'template_2',
    'template_name': 'Task Template 2',
    'title': {
        'display_name': 'title_display_name_2',
        'placeholder_text': 'title_placeholder_text_2'
    }
}

snapshots['TestGetTaskTemplatesPresenterImplementation.test_when_no_project_templates_exists_returns_project_id_none task_template_1'] = {
    'actions': [
        {
            'action_id': 1,
            'action_type': 'NO_VALIDATIONS',
            'button_color': 'button_color_1',
            'button_text': 'button_text__1',
            'transition_template_id': 'transition_template_1'
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
    'project_id': None,
    'stage_gofs': [
        {
            'gof_ids': [
                'gof_1'
            ],
            'stage_id': 3
        }
    ],
    'task_creation_gof_ids': [
        'gof_1'
    ],
    'template_id': 'template_1',
    'template_name': 'Task Template 1',
    'title': {
        'display_name': 'title_display_name_1',
        'placeholder_text': 'title_placeholder_text_1'
    }
}

snapshots['TestGetTaskTemplatesPresenterImplementation.test_when_no_project_templates_exists_returns_project_id_none task_template_2'] = {
    'actions': [
        {
            'action_id': 2,
            'action_type': 'NO_VALIDATIONS',
            'button_color': 'button_color_2',
            'button_text': 'button_text__2',
            'transition_template_id': 'transition_template_2'
        }
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
    'project_id': None,
    'stage_gofs': [
        {
            'gof_ids': [
                'gof_2'
            ],
            'stage_id': 4
        }
    ],
    'task_creation_gof_ids': [
        'gof_2'
    ],
    'template_id': 'template_2',
    'template_name': 'Task Template 2',
    'title': {
        'display_name': 'title_display_name_2',
        'placeholder_text': 'title_placeholder_text_2'
    }
}

snapshots['TestGetTaskTemplatesPresenterImplementation.test_when_no_actions_for_user_exists_returns_empty_actions_list task_template_1'] = {
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
                    'field_order': 1,
                    'field_type': 'DROPDOWN',
                    'field_values': [
                        'Mr',
                        'Mrs',
                        'Ms'
                    ],
                    'help_text': None,
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
    'project_id': 'project_1',
    'stage_gofs': [
        {
            'gof_ids': [
                'gof_1'
            ],
            'stage_id': 3
        }
    ],
    'task_creation_gof_ids': [
        'gof_1'
    ],
    'template_id': 'template_1',
    'template_name': 'Task Template 1',
    'title': {
        'display_name': 'title_display_name_1',
        'placeholder_text': 'title_placeholder_text_1'
    }
}

snapshots['TestGetTaskTemplatesPresenterImplementation.test_when_no_actions_for_user_exists_returns_empty_actions_list task_template_2'] = {
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
                }
            ],
            'gof_display_name': 'GOF_DISPLAY_NAME-2',
            'gof_id': 'gof_2',
            'max_columns': 2,
            'order': 1
        }
    ],
    'project_id': 'project_2',
    'stage_gofs': [
        {
            'gof_ids': [
                'gof_2'
            ],
            'stage_id': 4
        }
    ],
    'task_creation_gof_ids': [
        'gof_2'
    ],
    'template_id': 'template_2',
    'template_name': 'Task Template 2',
    'title': {
        'display_name': 'title_display_name_2',
        'placeholder_text': 'title_placeholder_text_2'
    }
}

snapshots['TestGetTaskTemplatesPresenterImplementation.test_when_no_task_creation_gofs_exists_returns_empty_list task_template_1'] = {
    'actions': [
        {
            'action_id': 1,
            'action_type': 'NO_VALIDATIONS',
            'button_color': 'button_color_1',
            'button_text': 'button_text__1',
            'transition_template_id': 'transition_template_1'
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
                    'field_order': 1,
                    'field_type': 'DROPDOWN',
                    'field_values': [
                        'Mr',
                        'Mrs',
                        'Ms'
                    ],
                    'help_text': None,
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
    'project_id': 'project_1',
    'stage_gofs': [
        {
            'gof_ids': [
                'gof_1',
                'gof_1'
            ],
            'stage_id': 3
        }
    ],
    'task_creation_gof_ids': [
    ],
    'template_id': 'template_1',
    'template_name': 'Task Template 1',
    'title': {
        'display_name': 'title_display_name_1',
        'placeholder_text': 'title_placeholder_text_1'
    }
}

snapshots['TestGetTaskTemplatesPresenterImplementation.test_when_no_task_creation_gofs_exists_returns_empty_list task_template_2'] = {
    'actions': [
        {
            'action_id': 2,
            'action_type': 'NO_VALIDATIONS',
            'button_color': 'button_color_2',
            'button_text': 'button_text__2',
            'transition_template_id': 'transition_template_2'
        }
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
                }
            ],
            'gof_display_name': 'GOF_DISPLAY_NAME-2',
            'gof_id': 'gof_2',
            'max_columns': 2,
            'order': 1
        }
    ],
    'project_id': 'project_2',
    'stage_gofs': [
        {
            'gof_ids': [
                'gof_2',
                'gof_2'
            ],
            'stage_id': 4
        }
    ],
    'task_creation_gof_ids': [
    ],
    'template_id': 'template_2',
    'template_name': 'Task Template 2',
    'title': {
        'display_name': 'title_display_name_2',
        'placeholder_text': 'title_placeholder_text_2'
    }
}

snapshots['TestGetTaskTemplatesPresenterImplementation.test_when_no_stage_gofs_returns_empty_list task_template_1'] = {
    'actions': [
        {
            'action_id': 1,
            'action_type': 'NO_VALIDATIONS',
            'button_color': 'button_color_1',
            'button_text': 'button_text__1',
            'transition_template_id': 'transition_template_1'
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
                    'field_order': 1,
                    'field_type': 'DROPDOWN',
                    'field_values': [
                        'Mr',
                        'Mrs',
                        'Ms'
                    ],
                    'help_text': None,
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
    'project_id': 'project_1',
    'stage_gofs': [
    ],
    'task_creation_gof_ids': [
        'gof_1'
    ],
    'template_id': 'template_1',
    'template_name': 'Task Template 1',
    'title': {
        'display_name': 'title_display_name_1',
        'placeholder_text': 'title_placeholder_text_1'
    }
}

snapshots['TestGetTaskTemplatesPresenterImplementation.test_when_no_stage_gofs_returns_empty_list task_template_2'] = {
    'actions': [
        {
            'action_id': 2,
            'action_type': 'NO_VALIDATIONS',
            'button_color': 'button_color_2',
            'button_text': 'button_text__2',
            'transition_template_id': 'transition_template_2'
        }
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
                }
            ],
            'gof_display_name': 'GOF_DISPLAY_NAME-2',
            'gof_id': 'gof_2',
            'max_columns': 2,
            'order': 1
        }
    ],
    'project_id': 'project_2',
    'stage_gofs': [
    ],
    'task_creation_gof_ids': [
        'gof_2'
    ],
    'template_id': 'template_2',
    'template_name': 'Task Template 2',
    'title': {
        'display_name': 'title_display_name_2',
        'placeholder_text': 'title_placeholder_text_2'
    }
}
