# -*- coding: utf-8 -*-
# snapshottest: v1 - https://goo.gl/zC4yUc
from __future__ import unicode_literals

from snapshottest import Snapshot


snapshots = Snapshot()

snapshots['TestCreateOrUpdateTaskPresenterImplementation.test_raise_exception_for_invalid_board invalid_board'] = {
    'http_status_code': 404,
    'res_status': 'INVALID_BOARD_ID',
    'response': 'invalid board id is: board_1, please send valid board id'
}

snapshots['TestCreateOrUpdateTaskPresenterImplementation.test_raise_exception_for_invalid_action invalid_action'] = {
    'http_status_code': 404,
    'res_status': 'INVALID_ACTION_ID',
    'response': 'invalid action id is: 1, please send valid action id'
}

snapshots['TestCreateOrUpdateTaskPresenterImplementation.test_raise_exception_for_invalid_user_permission invalid_user_permission'] = {
    'http_status_code': 403,
    'res_status': 'USER_DO_NOT_HAVE_ACCESS',
    'response': 'User do not have access to the action: 1'
}

snapshots['TestCreateOrUpdateTaskPresenterImplementation.test_raise_exception_for_invalid_task invalid_task'] = {
    'http_status_code': 404,
    'res_status': 'INVALID_TASK_ID',
    'response': 'invalid task id is: 1, please send valid task id'
}

snapshots['TestCreateOrUpdateTaskPresenterImplementation.test_raise_exception_for_invalid_user_board_permission invalid_user_board_permission'] = {
    'http_status_code': 403,
    'res_status': 'USER_DO_NOT_HAVE_ACCESS',
    'response': 'User do not have access to the board: board_1'
}

snapshots['TestCreateOrUpdateTaskPresenterImplementation.test_get_response_for_user_action_on_task task_complete_details'] = {
    'current_board_details': {
        'board_id': 'board__1',
        'board_name': 'name_1',
        'column_details': [
            {
                'column_id': 'column_1',
                'column_name': 'name_1',
                'stage_with_actions': {
                    'actions': [
                    ],
                    'assignee': None,
                    'stage_color': 'stage_color_1',
                    'stage_display_name': 'display_name_1',
                    'stage_id': 'db_stage_1'
                },
                'task_overview_fields': [
                    {
                        'field_display_name': 'key_1',
                        'field_response': 'value_1',
                        'field_type': 'field_type_1'
                    }
                ]
            },
            {
                'column_id': 'column_2',
                'column_name': 'name_2',
                'stage_with_actions': {
                    'actions': [
                    ],
                    'assignee': None,
                    'stage_color': 'stage_color_2',
                    'stage_display_name': 'display_name_2',
                    'stage_id': 'db_stage_2'
                },
                'task_overview_fields': [
                    {
                        'field_display_name': 'key_2',
                        'field_response': 'value_2',
                        'field_type': 'field_type_2'
                    }
                ]
            },
            {
                'column_id': 'column_3',
                'column_name': 'name_3',
                'stage_with_actions': {
                    'actions': [
                    ],
                    'assignee': None,
                    'stage_color': 'stage_color_3',
                    'stage_display_name': 'display_name_3',
                    'stage_id': 'db_stage_3'
                },
                'task_overview_fields': [
                    {
                        'field_display_name': 'key_3',
                        'field_response': 'value_3',
                        'field_type': 'field_type_3'
                    }
                ]
            }
        ]
    },
    'other_board_details': [
    ],
    'task_current_stages_details': {
        'stages': [
            {
                'stage_display_name': 'stage_display_name_0',
                'stage_id': 'stage_0'
            },
            {
                'stage_display_name': 'stage_display_name_1',
                'stage_id': 'stage_1'
            }
        ],
        'task_id': 'task_display_1',
        'user_has_permission': True
    },
    'task_details': {
        'stage_with_actions': {
            'actions': [
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
        ]
    },
    'task_id': 'task_display_1'
}

snapshots['TestCreateOrUpdateTaskPresenterImplementation.test_raise_exception_for_reason_is_not_added_to_task reason is not added to task delay'] = {
    'http_status_code': 404,
    'res_status': 'REASON_NOT_ADDED_FOR_TASK_DELAY',
    'response': 'Task IBWF-1 in Stage PR APPROVALS has missed the due date'
}
