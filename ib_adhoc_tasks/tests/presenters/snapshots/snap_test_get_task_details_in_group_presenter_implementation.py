# -*- coding: utf-8 -*-
# snapshottest: v1 - https://goo.gl/zC4yUc
from __future__ import unicode_literals

from snapshottest import Snapshot


snapshots = Snapshot()

snapshots['TestGetTaskDetailsInGroupPresenterImplementation.test_get_task_details_in_group_response get_task_details_in_group_response'] = {
    'tasks': [
        {
            'description': 'description_1',
            'due_date': '2020-10-10 05:30:00',
            'priority': 'LOW',
            'stage_with_actions': {
                'actions': [
                    {
                        'action_id': 'action0',
                        'action_type': 'NO_VALIDATIONS',
                        'button_color': 'button_color0',
                        'button_text': 'button_text0'
                    }
                ],
                'assignee': {
                    'assignee_id': 'assignee_1',
                    'name': 'name_1',
                    'profile_pic_url': 'profile_pic_1',
                    'team_info': {
                        'team_id': 'team_1',
                        'team_name': 'name_1'
                    }
                },
                'stage_color': 'stage_color1',
                'stage_display_name': 'stage_name1',
                'stage_id': 1
            },
            'start_date': '2020-09-10 05:30:00',
            'task_id': 'task_display1',
            'task_overview_fields': [
                {
                    'field_display_name': 'key_0',
                    'field_id': 'field_0',
                    'field_response': 'value_0',
                    'field_type': 'field_type0'
                },
                {
                    'field_display_name': 'key_1',
                    'field_id': 'field_1',
                    'field_response': 'value_1',
                    'field_type': 'field_type1'
                },
                {
                    'field_display_name': 'key_2',
                    'field_id': 'field_2',
                    'field_response': 'value_2',
                    'field_type': 'field_type2'
                }
            ],
            'title': 'title_1'
        },
        {
            'description': 'description_2',
            'due_date': '2020-10-10 05:30:00',
            'priority': 'MEDIUM',
            'stage_with_actions': {
                'actions': [
                    {
                        'action_id': 'action0',
                        'action_type': 'NO_VALIDATIONS',
                        'button_color': 'button_color0',
                        'button_text': 'button_text0'
                    }
                ],
                'assignee': {
                    'assignee_id': 'assignee_2',
                    'name': 'name_2',
                    'profile_pic_url': 'profile_pic_2',
                    'team_info': {
                        'team_id': 'team_2',
                        'team_name': 'name_2'
                    }
                },
                'stage_color': 'stage_color2',
                'stage_display_name': 'stage_name2',
                'stage_id': 2
            },
            'start_date': '2020-09-10 05:30:00',
            'task_id': 'task_display2',
            'task_overview_fields': [
                {
                    'field_display_name': 'key_0',
                    'field_id': 'field_0',
                    'field_response': 'value_0',
                    'field_type': 'field_type0'
                },
                {
                    'field_display_name': 'key_1',
                    'field_id': 'field_1',
                    'field_response': 'value_1',
                    'field_type': 'field_type1'
                },
                {
                    'field_display_name': 'key_2',
                    'field_id': 'field_2',
                    'field_response': 'value_2',
                    'field_type': 'field_type2'
                }
            ],
            'title': 'title_2'
        },
        {
            'description': 'description_3',
            'due_date': '2020-10-10 05:30:00',
            'priority': 'HIGH',
            'stage_with_actions': {
                'actions': [
                    {
                        'action_id': 'action0',
                        'action_type': 'NO_VALIDATIONS',
                        'button_color': 'button_color0',
                        'button_text': 'button_text0'
                    }
                ],
                'assignee': {
                    'assignee_id': 'assignee_3',
                    'name': 'name_3',
                    'profile_pic_url': 'profile_pic_3',
                    'team_info': {
                        'team_id': 'team_3',
                        'team_name': 'name_3'
                    }
                },
                'stage_color': 'stage_color3',
                'stage_display_name': 'stage_name3',
                'stage_id': 3
            },
            'start_date': '2020-09-10 05:30:00',
            'task_id': 'task_display3',
            'task_overview_fields': [
                {
                    'field_display_name': 'key_0',
                    'field_id': 'field_0',
                    'field_response': 'value_0',
                    'field_type': 'field_type0'
                },
                {
                    'field_display_name': 'key_1',
                    'field_id': 'field_1',
                    'field_response': 'value_1',
                    'field_type': 'field_type1'
                },
                {
                    'field_display_name': 'key_2',
                    'field_id': 'field_2',
                    'field_response': 'value_2',
                    'field_type': 'field_type2'
                }
            ],
            'title': 'title_3'
        },
        {
            'description': 'description_4',
            'due_date': '2020-10-10 05:30:00',
            'priority': 'LOW',
            'stage_with_actions': {
                'actions': [
                    {
                        'action_id': 'action0',
                        'action_type': 'NO_VALIDATIONS',
                        'button_color': 'button_color0',
                        'button_text': 'button_text0'
                    }
                ],
                'assignee': {
                    'assignee_id': 'assignee_4',
                    'name': 'name_4',
                    'profile_pic_url': 'profile_pic_4',
                    'team_info': {
                        'team_id': 'team_4',
                        'team_name': 'name_4'
                    }
                },
                'stage_color': 'stage_color4',
                'stage_display_name': 'stage_name4',
                'stage_id': 4
            },
            'start_date': '2020-09-10 05:30:00',
            'task_id': 'task_display4',
            'task_overview_fields': [
                {
                    'field_display_name': 'key_0',
                    'field_id': 'field_0',
                    'field_response': 'value_0',
                    'field_type': 'field_type0'
                },
                {
                    'field_display_name': 'key_1',
                    'field_id': 'field_1',
                    'field_response': 'value_1',
                    'field_type': 'field_type1'
                },
                {
                    'field_display_name': 'key_2',
                    'field_id': 'field_2',
                    'field_response': 'value_2',
                    'field_type': 'field_type2'
                }
            ],
            'title': 'title_4'
        }
    ],
    'total_tasks': 10
}
