# -*- coding: utf-8 -*-
# snapshottest: v1 - https://goo.gl/zC4yUc
from __future__ import unicode_literals

from snapshottest import Snapshot


snapshots = Snapshot()

snapshots['TestGetColumnDetails.test_get_response_for_column_details_with_duplicate_tasks_in_same_column column_details_with_duplicates'] = {
    'tasks': [
        {
            'stage_with_actions': {
                'actions': [
                    {
                        'action_id': 'action_id_0',
                        'action_type': 'action_type_0',
                        'button_color': None,
                        'button_text': 'button_text_0',
                        'transition_template_id': 'template_0'
                    },
                    {
                        'action_id': 'action_id_3',
                        'action_type': 'action_type_3',
                        'button_color': None,
                        'button_text': 'button_text_3',
                        'transition_template_id': 'template_3'
                    }
                ],
                'assignee': {
                    'assignee_id': '123e4567-e89b-12d3-a456-4266141740016',
                    'name': 'name_16',
                    'profile_pic_url': 'https://www.google.com/search?q=ibhubs&client=ubuntu&hs=DI7&channel=fs&source=lnms&tbm=isch&sa=X&ved=2ahUKEwjZqYjthYfrAhUF4zgGHevjDZUQ_AUoA3oECAsQBQ&biw=1848&bih=913#imgrc=Kg3TRY0jmx3udM'
                },
                'stage_color': 'blue',
                'stage_display_name': 'stage',
                'stage_id': 0
            },
            'task_id': 'task_id_0',
            'task_overview_fields': [
                {
                    'field_display_name': 'key_0',
                    'field_response': 'value_0'
                },
                {
                    'field_display_name': 'key_3',
                    'field_response': 'value_3'
                }
            ]
        },
        {
            'stage_with_actions': {
                'actions': [
                    {
                        'action_id': 'action_id_1',
                        'action_type': 'action_type_1',
                        'button_color': None,
                        'button_text': 'button_text_1',
                        'transition_template_id': 'template_1'
                    }
                ],
                'assignee': {
                    'assignee_id': '123e4567-e89b-12d3-a456-4266141740017',
                    'name': 'name_17',
                    'profile_pic_url': 'https://www.google.com/search?q=ibhubs&client=ubuntu&hs=DI7&channel=fs&source=lnms&tbm=isch&sa=X&ved=2ahUKEwjZqYjthYfrAhUF4zgGHevjDZUQ_AUoA3oECAsQBQ&biw=1848&bih=913#imgrc=Kg3TRY0jmx3udM'
                },
                'stage_color': 'orange',
                'stage_display_name': 'stage',
                'stage_id': 1
            },
            'task_id': 'task_id_1',
            'task_overview_fields': [
                {
                    'field_display_name': 'key_1',
                    'field_response': 'value_1'
                }
            ]
        },
        {
            'stage_with_actions': {
                'actions': [
                    {
                        'action_id': 'action_id_2',
                        'action_type': 'action_type_2',
                        'button_color': None,
                        'button_text': 'button_text_2',
                        'transition_template_id': 'template_2'
                    }
                ],
                'assignee': {
                    'assignee_id': '123e4567-e89b-12d3-a456-4266141740018',
                    'name': 'name_18',
                    'profile_pic_url': 'https://www.google.com/search?q=ibhubs&client=ubuntu&hs=DI7&channel=fs&source=lnms&tbm=isch&sa=X&ved=2ahUKEwjZqYjthYfrAhUF4zgGHevjDZUQ_AUoA3oECAsQBQ&biw=1848&bih=913#imgrc=Kg3TRY0jmx3udM'
                },
                'stage_color': 'green',
                'stage_display_name': 'stage',
                'stage_id': 2
            },
            'task_id': 'task_id_2',
            'task_overview_fields': [
                {
                    'field_display_name': 'key_2',
                    'field_response': 'value_2'
                }
            ]
        }
    ],
    'total_tasks': 10
}

snapshots['TestGetColumnDetails.test_with_duplicate_tasks_in_same_column_and_duplicate_fields column_details_with_duplicates_fields'] = {
    'tasks': [
        {
            'stage_with_actions': {
                'actions': [
                    {
                        'action_id': 'action_id_0',
                        'action_type': 'action_type_0',
                        'button_color': None,
                        'button_text': 'button_text_0',
                        'transition_template_id': 'template_0'
                    }
                ],
                'assignee': {
                    'assignee_id': '123e4567-e89b-12d3-a456-4266141740020',
                    'name': 'name_20',
                    'profile_pic_url': 'https://www.google.com/search?q=ibhubs&client=ubuntu&hs=DI7&channel=fs&source=lnms&tbm=isch&sa=X&ved=2ahUKEwjZqYjthYfrAhUF4zgGHevjDZUQ_AUoA3oECAsQBQ&biw=1848&bih=913#imgrc=Kg3TRY0jmx3udM'
                },
                'stage_color': 'blue',
                'stage_display_name': 'stage',
                'stage_id': 0
            },
            'task_id': 'task_id_0',
            'task_overview_fields': [
                {
                    'field_display_name': 'key_0',
                    'field_response': 'value_0'
                }
            ]
        },
        {
            'stage_with_actions': {
                'actions': [
                    {
                        'action_id': 'action_id_1',
                        'action_type': 'action_type_1',
                        'button_color': None,
                        'button_text': 'button_text_1',
                        'transition_template_id': 'template_1'
                    }
                ],
                'assignee': {
                    'assignee_id': '123e4567-e89b-12d3-a456-4266141740021',
                    'name': 'name_21',
                    'profile_pic_url': 'https://www.google.com/search?q=ibhubs&client=ubuntu&hs=DI7&channel=fs&source=lnms&tbm=isch&sa=X&ved=2ahUKEwjZqYjthYfrAhUF4zgGHevjDZUQ_AUoA3oECAsQBQ&biw=1848&bih=913#imgrc=Kg3TRY0jmx3udM'
                },
                'stage_color': 'orange',
                'stage_display_name': 'stage',
                'stage_id': 1
            },
            'task_id': 'task_id_1',
            'task_overview_fields': [
                {
                    'field_display_name': 'key_1',
                    'field_response': 'value_1'
                }
            ]
        },
        {
            'stage_with_actions': {
                'actions': [
                    {
                        'action_id': 'action_id_2',
                        'action_type': 'action_type_2',
                        'button_color': None,
                        'button_text': 'button_text_2',
                        'transition_template_id': 'template_2'
                    }
                ],
                'assignee': {
                    'assignee_id': '123e4567-e89b-12d3-a456-4266141740022',
                    'name': 'name_22',
                    'profile_pic_url': 'https://www.google.com/search?q=ibhubs&client=ubuntu&hs=DI7&channel=fs&source=lnms&tbm=isch&sa=X&ved=2ahUKEwjZqYjthYfrAhUF4zgGHevjDZUQ_AUoA3oECAsQBQ&biw=1848&bih=913#imgrc=Kg3TRY0jmx3udM'
                },
                'stage_color': 'green',
                'stage_display_name': 'stage',
                'stage_id': 2
            },
            'task_id': 'task_id_2',
            'task_overview_fields': [
                {
                    'field_display_name': 'key_2',
                    'field_response': 'value_2'
                }
            ]
        }
    ],
    'total_tasks': 10
}

snapshots['TestGetColumnDetails.test_get_response_for_column_details_with_proper_data column_details_with_proper_data'] = {
    'tasks': [
        {
            'stage_with_actions': {
                'actions': [
                    {
                        'action_id': 'action_id_0',
                        'action_type': 'action_type_0',
                        'button_color': None,
                        'button_text': 'button_text_0',
                        'transition_template_id': 'template_0'
                    }
                ],
                'assignee': {
                    'assignee_id': '123e4567-e89b-12d3-a456-4266141740024',
                    'name': 'name_24',
                    'profile_pic_url': 'https://www.google.com/search?q=ibhubs&client=ubuntu&hs=DI7&channel=fs&source=lnms&tbm=isch&sa=X&ved=2ahUKEwjZqYjthYfrAhUF4zgGHevjDZUQ_AUoA3oECAsQBQ&biw=1848&bih=913#imgrc=Kg3TRY0jmx3udM'
                },
                'stage_color': 'blue',
                'stage_display_name': 'stage',
                'stage_id': 0
            },
            'task_id': 'task_id_0',
            'task_overview_fields': [
                {
                    'field_display_name': 'key_0',
                    'field_response': 'value_0'
                }
            ]
        },
        {
            'stage_with_actions': {
                'actions': [
                    {
                        'action_id': 'action_id_1',
                        'action_type': 'action_type_1',
                        'button_color': None,
                        'button_text': 'button_text_1',
                        'transition_template_id': 'template_1'
                    }
                ],
                'assignee': {
                    'assignee_id': '123e4567-e89b-12d3-a456-4266141740025',
                    'name': 'name_25',
                    'profile_pic_url': 'https://www.google.com/search?q=ibhubs&client=ubuntu&hs=DI7&channel=fs&source=lnms&tbm=isch&sa=X&ved=2ahUKEwjZqYjthYfrAhUF4zgGHevjDZUQ_AUoA3oECAsQBQ&biw=1848&bih=913#imgrc=Kg3TRY0jmx3udM'
                },
                'stage_color': 'orange',
                'stage_display_name': 'stage',
                'stage_id': 1
            },
            'task_id': 'task_id_1',
            'task_overview_fields': [
                {
                    'field_display_name': 'key_1',
                    'field_response': 'value_1'
                }
            ]
        },
        {
            'stage_with_actions': {
                'actions': [
                    {
                        'action_id': 'action_id_2',
                        'action_type': 'action_type_2',
                        'button_color': None,
                        'button_text': 'button_text_2',
                        'transition_template_id': 'template_2'
                    }
                ],
                'assignee': {
                    'assignee_id': '123e4567-e89b-12d3-a456-4266141740026',
                    'name': 'name_26',
                    'profile_pic_url': 'https://www.google.com/search?q=ibhubs&client=ubuntu&hs=DI7&channel=fs&source=lnms&tbm=isch&sa=X&ved=2ahUKEwjZqYjthYfrAhUF4zgGHevjDZUQ_AUoA3oECAsQBQ&biw=1848&bih=913#imgrc=Kg3TRY0jmx3udM'
                },
                'stage_color': 'green',
                'stage_display_name': 'stage',
                'stage_id': 2
            },
            'task_id': 'task_id_2',
            'task_overview_fields': [
                {
                    'field_display_name': 'key_2',
                    'field_response': 'value_2'
                }
            ]
        }
    ],
    'total_tasks': 10
}
