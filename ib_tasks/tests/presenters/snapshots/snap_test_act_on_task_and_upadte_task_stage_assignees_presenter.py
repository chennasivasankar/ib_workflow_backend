# -*- coding: utf-8 -*-
# snapshottest: v1 - https://goo.gl/zC4yUc
from __future__ import unicode_literals

from snapshottest import Snapshot


snapshots = Snapshot()

snapshots['TestActOnTaskAndUpdateTaskStageAssigneesPresenterImplementation.test_raise_exception_for_invalid_task_display_id invalid_task'] = {
    'http_status_code': 404,
    'res_status': 'INVALID_TASK_ID',
    'response': 'IBWF_1 is invalid task_id send valid task_id'
}

snapshots['TestActOnTaskAndUpdateTaskStageAssigneesPresenterImplementation.test_raise_exception_for_invalid_board invalid_board'] = {
    'http_status_code': 404,
    'res_status': 'INVALID_BOARD_ID',
    'response': 'invalid board id is: board_1, please send valid board id'
}

snapshots['TestActOnTaskAndUpdateTaskStageAssigneesPresenterImplementation.test_raise_exception_for_invalid_action invalid_action'] = {
    'http_status_code': 404,
    'res_status': 'INVALID_ACTION_ID',
    'response': 'invalid action id is: 1, please send valid action id'
}

snapshots['TestActOnTaskAndUpdateTaskStageAssigneesPresenterImplementation.test_raise_exception_for_invalid_user_permission invalid_user_permission'] = {
    'http_status_code': 403,
    'res_status': 'USER_DO_NOT_HAVE_ACCESS',
    'response': 'User do not have access to the action: 1'
}

snapshots['TestActOnTaskAndUpdateTaskStageAssigneesPresenterImplementation.test_raise_exception_for_reason_is_not_added_to_task reason is not added to task delay'] = {
    'http_status_code': 404,
    'res_status': 'REASON_NOT_ADDED_FOR_TASK_DELAY',
    'response': '''Task IBWF-1 in Stage PR APPROVALS has missed the
                                  due date'''
}

snapshots['TestActOnTaskAndUpdateTaskStageAssigneesPresenterImplementation.test_raise_user_did_not_fill_required_fields required fields are not filled by user'] = {
    'http_status_code': 400,
    'res_status': 'USER_DID_NOT_FILL_REQUIRED_FIELDS',
    'response': "user did not fill required fields: ['field_display_1']"
}

snapshots['TestActOnTaskAndUpdateTaskStageAssigneesPresenterImplementation.test_raise_exception_for_invalid_present_actions invalid present stage action'] = {
    'http_status_code': 403,
    'res_status': 'INVALID_PRESENT_STAGE_ACTION',
    'response': '1 is invalid present stage action'
}

snapshots['TestActOnTaskAndUpdateTaskStageAssigneesPresenterImplementation.test_raise_user_not_in_project user not in project'] = {
    'http_status_code': 403,
    'res_status': 'USER_NOT_IN_PROJECT',
    'response': 'User Not a part of the Project'
}

snapshots['TestActOnTaskAndUpdateTaskStageAssigneesPresenterImplementation.test_with_duplicate_stage_ids duplicate stage ids'] = {
    'http_status_code': 400,
    'res_status': 'DUPLICATE_STAGE_IDS',
    'response': 'Duplicate stage ids that you have sent are: [2, 2],please send unique stage ids'
}

snapshots['TestActOnTaskAndUpdateTaskStageAssigneesPresenterImplementation.test_given_invalid_stage_ids_raise_exception invalid stage ids'] = {
    'http_status_code': 400,
    'res_status': 'INVALID_STAGE_IDS',
    'response': 'Invalid stage ids that you have sent are: [1, 2],please send valid stage ids'
}

snapshots['TestActOnTaskAndUpdateTaskStageAssigneesPresenterImplementation.test_given_virtual_stage_ids_raise_exception virtual stage ids'] = {
    'http_status_code': 400,
    'res_status': 'VIRTUAL_STAGE_IDS',
    'response': 'Invalid stage ids that you have sent are: [1, 2],please send valid stage ids'
}

snapshots['TestActOnTaskAndUpdateTaskStageAssigneesPresenterImplementation.test_raise_stage_ids_with_invalid_permission_for_assignee_exception stage ids with invalid permission for assignee'] = {
    'http_status_code': 400,
    'res_status': 'STAGE_IDS_WITH_INVALID_PERMISSION_OF_ASSIGNEE',
    'response': 'Stage ids with invalid permission of assignees that you have sent are: [1, 2],please assign valid assignees for stages'
}

snapshots['TestActOnTaskAndUpdateTaskStageAssigneesPresenterImplementation.test_get_response_for_user_action_on_task task_complete_details'] = {
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
