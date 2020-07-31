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

snapshots['TestCreateOrUpdateTaskPresenterImplementation.test_get_response_for_user_action_on_task task_complete_details'] = {
    'current_board_details': {
        'board_id': 'board__1',
        'board_name': 'name_1',
        'column_details': [
            {
                'actions': [
                    {
                        'action_id': '1',
                        'button_color': None,
                        'button_text': 'button_text_1',
                        'name': 'name_1'
                    }
                ],
                'column_id': 'column_1',
                'column_name': 'name_1',
                'fields': [
                    {
                        'field_type': 'field_type_1',
                        'key': 'key_1',
                        'value': 'value_1'
                    }
                ]
            },
            {
                'actions': [
                    {
                        'action_id': '2',
                        'button_color': None,
                        'button_text': 'button_text_2',
                        'name': 'name_2'
                    }
                ],
                'column_id': 'column_2',
                'column_name': 'name_2',
                'fields': [
                    {
                        'field_type': 'field_type_2',
                        'key': 'key_2',
                        'value': 'value_2'
                    }
                ]
            },
            {
                'actions': [
                    {
                        'action_id': '3',
                        'button_color': None,
                        'button_text': 'button_text_3',
                        'name': 'name_3'
                    }
                ],
                'column_id': 'column_3',
                'column_name': 'name_3',
                'fields': [
                    {
                        'field_type': 'field_type_3',
                        'key': 'key_3',
                        'value': 'value_3'
                    }
                ]
            }
        ]
    },
    'other_board_details': [
    ],
    'task_id': '1'
}

snapshots['TestCreateOrUpdateTaskPresenterImplementation.test_raise_exception_for_invalid_task invalid_task'] = {
    'http_status_code': 404,
    'res_status': 'INVALID_TASK_ID',
    'response': '1 is an invalid task id'
}
