# -*- coding: utf-8 -*-
# snapshottest: v1 - https://goo.gl/zC4yUc
from __future__ import unicode_literals

from snapshottest import Snapshot


snapshots = Snapshot()

snapshots['TestGetNextStagesRandomAssigneesOfATaskPresenterImpl.test_with_invalid_task_display_id http_status_code'] = 400

snapshots['TestGetNextStagesRandomAssigneesOfATaskPresenterImpl.test_with_invalid_task_display_id res_status'] = 'INVALID_TASK_ID'

snapshots['TestGetNextStagesRandomAssigneesOfATaskPresenterImpl.test_with_invalid_task_display_id json_response'] = 'task_display_id is invalid task_id send valid task_id'

snapshots['TestGetNextStagesRandomAssigneesOfATaskPresenterImpl.test_raise_invalid_action_id http_status_code'] = 404

snapshots['TestGetNextStagesRandomAssigneesOfATaskPresenterImpl.test_raise_invalid_action_id res_status'] = 'INVALID_ACTION_ID'

snapshots['TestGetNextStagesRandomAssigneesOfATaskPresenterImpl.test_raise_invalid_action_id json_response'] = 'invalid action id is: 1, please send valid action id'

snapshots['TestGetNextStagesRandomAssigneesOfATaskPresenterImpl.test_raise_users_not_exists_for_given_projects http_status_code'] = 404

snapshots['TestGetNextStagesRandomAssigneesOfATaskPresenterImpl.test_raise_users_not_exists_for_given_projects res_status'] = 'USER_NOT_IN_ANY_TEAM_OF_PROJECT'

snapshots['TestGetNextStagesRandomAssigneesOfATaskPresenterImpl.test_raise_users_not_exists_for_given_projects json_response'] = "user id with ['user_1', 'user_2'] is not in any team of project"

snapshots['TestGetNextStagesRandomAssigneesOfATaskPresenterImpl.test_raise_invalid_key_error http_status_code'] = 400

snapshots['TestGetNextStagesRandomAssigneesOfATaskPresenterImpl.test_raise_invalid_key_error res_status'] = 'INVALID_KEY_ERROR'

snapshots['TestGetNextStagesRandomAssigneesOfATaskPresenterImpl.test_raise_invalid_key_error json_response'] = 'invalid key error'

snapshots['TestGetNextStagesRandomAssigneesOfATaskPresenterImpl.test_raise_invalid_custom_logic_function_exception http_status_code'] = 400

snapshots['TestGetNextStagesRandomAssigneesOfATaskPresenterImpl.test_raise_invalid_custom_logic_function_exception res_status'] = 'INVALID_CUSTOM_LOGIC'

snapshots['TestGetNextStagesRandomAssigneesOfATaskPresenterImpl.test_raise_invalid_custom_logic_function_exception json_response'] = 'invalid custom logic'

snapshots['TestGetNextStagesRandomAssigneesOfATaskPresenterImpl.test_raise_invalid_path_not_found_exception http_status_code'] = 400

snapshots['TestGetNextStagesRandomAssigneesOfATaskPresenterImpl.test_raise_invalid_path_not_found_exception res_status'] = 'PATH_NOT_FOUND'

snapshots['TestGetNextStagesRandomAssigneesOfATaskPresenterImpl.test_raise_invalid_path_not_found_exception json_response'] = 'path not found'

snapshots['TestGetNextStagesRandomAssigneesOfATaskPresenterImpl.test_raise_invalid_method_not_found_exception http_status_code'] = 400

snapshots['TestGetNextStagesRandomAssigneesOfATaskPresenterImpl.test_raise_invalid_method_not_found_exception res_status'] = 'METHOD_NOT_FOUND'

snapshots['TestGetNextStagesRandomAssigneesOfATaskPresenterImpl.test_raise_invalid_method_not_found_exception json_response'] = 'method not found'

snapshots['TestGetNextStagesRandomAssigneesOfATaskPresenterImpl.test_given_valid_details_get_expected_result json_response'] = {
    'stage_assignees': [
        {
            'assignee': {
                'assignee_id': '123e4567-e89b-12d3-a456-426614174000',
                'name': 'name_0',
                'profile_pic_url': 'https://www.google.com/search?q=ibhubs&client=ubuntu&hs=DI7&channel=fs&source=lnms&tbm=isch&sa=X&ved=2ahUKEwjZqYjthYfrAhUF4zgGHevjDZUQ_AUoA3oECAsQBQ&biw=1848&bih=913#imgrc=Kg3TRY0jmx3udM',
                'team_info': {
                    'team_id': 'team_1',
                    'team_name': 'team_name0'
                }
            },
            'stage_display_name': 'stage_1',
            'stage_id': 2
        },
        {
            'assignee': {
                'assignee_id': '123e4567-e89b-12d3-a456-426614174001',
                'name': 'name_1',
                'profile_pic_url': 'https://www.google.com/search?q=ibhubs&client=ubuntu&hs=DI7&channel=fs&source=lnms&tbm=isch&sa=X&ved=2ahUKEwjZqYjthYfrAhUF4zgGHevjDZUQ_AUoA3oECAsQBQ&biw=1848&bih=913#imgrc=Kg3TRY0jmx3udM',
                'team_info': {
                    'team_id': 'team_2',
                    'team_name': 'team_name1'
                }
            },
            'stage_display_name': 'stage_2',
            'stage_id': 3
        }
    ]
}
