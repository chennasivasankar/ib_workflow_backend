# -*- coding: utf-8 -*-
# snapshottest: v1 - https://goo.gl/zC4yUc
from __future__ import unicode_literals

from snapshottest import Snapshot


snapshots = Snapshot()

snapshots['TestGetTaskDetailsInGroupPresenterImplementation.test_get_task_details_in_group_response get_task_details_in_group_response'] = {
    'tasks': [
        {
            'completed_sub_tasks_count': 2,
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
                    'assignee_id': 'assignee_16',
                    'name': 'name_16',
                    'profile_pic_url': 'profile_pic_16',
                    'team_info': {
                        'team_id': 'team_16',
                        'team_name': 'name_16'
                    }
                },
                'stage_color': 'stage_color1',
                'stage_display_name': 'stage_name1',
                'stage_id': 1
            },
            'start_date': '2020-09-10 05:30:00',
            'sub_tasks_count': 2,
            'task_id': 'task_display1',
            'task_overview_fields': [
                {
                    'field_display_name': 'key_3',
                    'field_id': 'field_3',
                    'field_response': 'value_3',
                    'field_type': 'field_type3'
                },
                {
                    'field_display_name': 'key_4',
                    'field_id': 'field_4',
                    'field_response': 'value_4',
                    'field_type': 'field_type4'
                },
                {
                    'field_display_name': 'key_5',
                    'field_id': 'field_5',
                    'field_response': 'value_5',
                    'field_type': 'field_type5'
                }
            ],
            'title': 'title_1'
        },
        {
            'completed_sub_tasks_count': 3,
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
                    'assignee_id': 'assignee_17',
                    'name': 'name_17',
                    'profile_pic_url': 'profile_pic_17',
                    'team_info': {
                        'team_id': 'team_17',
                        'team_name': 'name_17'
                    }
                },
                'stage_color': 'stage_color2',
                'stage_display_name': 'stage_name2',
                'stage_id': 2
            },
            'start_date': '2020-09-10 05:30:00',
            'sub_tasks_count': 3,
            'task_id': 'task_display2',
            'task_overview_fields': [
                {
                    'field_display_name': 'key_3',
                    'field_id': 'field_3',
                    'field_response': 'value_3',
                    'field_type': 'field_type3'
                },
                {
                    'field_display_name': 'key_4',
                    'field_id': 'field_4',
                    'field_response': 'value_4',
                    'field_type': 'field_type4'
                },
                {
                    'field_display_name': 'key_5',
                    'field_id': 'field_5',
                    'field_response': 'value_5',
                    'field_type': 'field_type5'
                }
            ],
            'title': 'title_2'
        },
        {
            'completed_sub_tasks_count': 0,
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
                    'assignee_id': 'assignee_18',
                    'name': 'name_18',
                    'profile_pic_url': 'profile_pic_18',
                    'team_info': {
                        'team_id': 'team_18',
                        'team_name': 'name_18'
                    }
                },
                'stage_color': 'stage_color3',
                'stage_display_name': 'stage_name3',
                'stage_id': 3
            },
            'start_date': '2020-09-10 05:30:00',
            'sub_tasks_count': 0,
            'task_id': 'task_display3',
            'task_overview_fields': [
                {
                    'field_display_name': 'key_3',
                    'field_id': 'field_3',
                    'field_response': 'value_3',
                    'field_type': 'field_type3'
                },
                {
                    'field_display_name': 'key_4',
                    'field_id': 'field_4',
                    'field_response': 'value_4',
                    'field_type': 'field_type4'
                },
                {
                    'field_display_name': 'key_5',
                    'field_id': 'field_5',
                    'field_response': 'value_5',
                    'field_type': 'field_type5'
                }
            ],
            'title': 'title_3'
        },
        {
            'completed_sub_tasks_count': 1,
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
                    'assignee_id': 'assignee_19',
                    'name': 'name_19',
                    'profile_pic_url': 'profile_pic_19',
                    'team_info': {
                        'team_id': 'team_19',
                        'team_name': 'name_19'
                    }
                },
                'stage_color': 'stage_color4',
                'stage_display_name': 'stage_name4',
                'stage_id': 4
            },
            'start_date': '2020-09-10 05:30:00',
            'sub_tasks_count': 1,
            'task_id': 'task_display4',
            'task_overview_fields': [
                {
                    'field_display_name': 'key_3',
                    'field_id': 'field_3',
                    'field_response': 'value_3',
                    'field_type': 'field_type3'
                },
                {
                    'field_display_name': 'key_4',
                    'field_id': 'field_4',
                    'field_response': 'value_4',
                    'field_type': 'field_type4'
                },
                {
                    'field_display_name': 'key_5',
                    'field_id': 'field_5',
                    'field_response': 'value_5',
                    'field_type': 'field_type5'
                }
            ],
            'title': 'title_4'
        }
    ],
    'total_tasks': 10
}
