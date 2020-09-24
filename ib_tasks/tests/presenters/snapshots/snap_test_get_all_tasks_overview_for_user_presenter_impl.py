# -*- coding: utf-8 -*-
# snapshottest: v1 - https://goo.gl/zC4yUc
from __future__ import unicode_literals

from snapshottest import Snapshot


snapshots = Snapshot()

snapshots['TestGetAllTasksOverviewForUserPresenterImpl.test_given_valid_details_get_all_tasks_overview_details_response response'] = {
    'tasks': [
        {
            'stage_with_actions': {
                'actions': [
                    {
                        'action_id': 1,
                        'action_type': 'action_type_1',
                        'button_color': None,
                        'button_text': 'button_text_1',
                        'transition_template_id': 'template_id_1'
                    },
                    {
                        'action_id': 2,
                        'action_type': 'action_type_2',
                        'button_color': None,
                        'button_text': 'button_text_2',
                        'transition_template_id': 'template_id_2'
                    }
                ],
                'assignee': {
                    'assignee_id': '123e4567-e89b-12d3-a456-426614174000',
                    'name': 'name_0',
                    'profile_pic_url': 'https://www.google.com/search?q=ibhubs&client=ubuntu&hs=DI7&channel=fs&source=lnms&tbm=isch&sa=X&ved=2ahUKEwjZqYjthYfrAhUF4zgGHevjDZUQ_AUoA3oECAsQBQ&biw=1848&bih=913#imgrc=Kg3TRY0jmx3udM'
                },
                'stage_color': 'color_1',
                'stage_display_name': 'stage_display_1',
                'stage_id': 1
            },
            'task_id': 'iBWF-1',
            'task_overview_fields': [
                {
                    'field_display_name': 'key',
                    'field_response': 'value',
                    'field_type': 'Drop down'
                }
            ]
        },
        {
            'stage_with_actions': {
                'actions': [
                    {
                        'action_id': 1,
                        'action_type': 'action_type_1',
                        'button_color': None,
                        'button_text': 'button_text_1',
                        'transition_template_id': 'template_id_1'
                    },
                    {
                        'action_id': 2,
                        'action_type': 'action_type_2',
                        'button_color': None,
                        'button_text': 'button_text_2',
                        'transition_template_id': 'template_id_2'
                    }
                ],
                'assignee': {
                    'assignee_id': '123e4567-e89b-12d3-a456-426614174000',
                    'name': 'name_0',
                    'profile_pic_url': 'https://www.google.com/search?q=ibhubs&client=ubuntu&hs=DI7&channel=fs&source=lnms&tbm=isch&sa=X&ved=2ahUKEwjZqYjthYfrAhUF4zgGHevjDZUQ_AUoA3oECAsQBQ&biw=1848&bih=913#imgrc=Kg3TRY0jmx3udM'
                },
                'stage_color': 'color_2',
                'stage_display_name': 'stage_display_2',
                'stage_id': 2
            },
            'task_id': 'iBWF-2',
            'task_overview_fields': [
                {
                    'field_display_name': 'key',
                    'field_response': 'value',
                    'field_type': 'Drop down'
                }
            ]
        }
    ],
    'total_tasks': 2
}
