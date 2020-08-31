# -*- coding: utf-8 -*-
# snapshottest: v1 - https://goo.gl/zC4yUc
from __future__ import unicode_literals

from snapshottest import Snapshot


snapshots = Snapshot()

snapshots['TestGetTaskPresenterImplementation.test_raise_exception_for_invalid_task_id exception_object'] = b'{"response": "Invalid task id", "http_status_code": 404, "res_status": "INVALID_TASK_ID"}'

snapshots['TestGetTaskPresenterImplementation.test_raise_invalid_user exception_object'] = b'{"response": "invalid user", "http_status_code": 404, "res_status": "INVALID_USER"}'

snapshots['TestGetTaskPresenterImplementation.test_raise_invalid_project_id exception_object'] = b'{"response": "project1 is invalid project id, please send valid project id", "http_status_code": 404, "res_status": "INVALID_PROJECT_ID"}'

snapshots['TestGetTaskPresenterImplementation.test_raise_teams_does_not_exists_for_project exception_object'] = b'{"response": "invalid teams = [\'team1\', \'team2\'] for project", "http_status_code": 404, "res_status": "TEAMS_NOT_EXISTS_FOR_PROJECT"}'

snapshots['TestGetTaskPresenterImplementation.test_raise_users_not_exist_for_given_teams exception_object'] = b'{"response": "users = [\'user1\', \'user2\'] not exists for teams", "http_status_code": 404, "res_status": "USERS_NOT_EXISTS_FOR_TEAMS"}'

snapshots['TestGetTaskPresenterImplementation.test_raise_user_permission_denied exception_object'] = b'{"response": "user doesn\'t have permission", "http_status_code": 403, "res_status": "USER_PERMISSION_DENIED"}'

snapshots['TestGetTaskPresenterImplementation.test_raise_exception_for_invalid_task_display_id exception_object'] = b'{"response": "IBWF-10 is invalid task_id send valid task_id", "http_status_code": 404, "res_status": "INVALID_TASK_ID"}'

snapshots['TestGetTaskPresenterImplementation.test_raise_exception_for_raise_invalid_stage_ids_for_task exception_object'] = b'{"response": "invalid stages for task", "http_status_code": 404, "res_status": "INVALID_STAGE_IDS_FOR_TASK"}'

snapshots['TestGetTaskPresenterImplementation.test_raise_invalid_searchable_records_found exception_object'] = b'{"response": "Something went wrong contact Admin", "http_status_code": 404, "res_status": "SEARCHABLE_RECORDS_NOT_FOUND"}'

snapshots['TestGetTaskPresenterImplementation.test_given_task_complete_details_dto_returns_task_details task_details = '] = b'{"task_id": "IBWF-1", "project_info": {"project_id": "project0", "project_name": "project_name0", "project_logo_url": "logo_url0"}, "template_id": "template_0", "title": "title_0", "description": "description_0", "start_date": "2020-04-05 04:50:40", "due_date": "2020-04-15 04:50:40", "priority": "HIGH", "gofs": [{"gof_id": "gof0", "same_gof_order": 0, "gof_fields": [{"field_id": "field0", "field_response": "{\\"id\\": 1, \\"value\\": \\"Hyderabad\\"}"}]}, {"gof_id": "gof1", "same_gof_order": 0, "gof_fields": [{"field_id": "field2", "field_response": "response2"}, {"field_id": "field3", "field_response": "response3"}]}], "stages_with_actions": [{"stage_id": 1, "stage_display_name": "name1", "stage_color": "color1", "task_stage_id": 1, "assignee": {"assignee_id": "123e4567-e89b-12d3-a456-426614174000", "name": "name_0", "profile_pic_url": "https://www.google.com/search?q=ibhubs&client=ubuntu&hs=DI7&channel=fs&source=lnms&tbm=isch&sa=X&ved=2ahUKEwjZqYjthYfrAhUF4zgGHevjDZUQ_AUoA3oECAsQBQ&biw=1848&bih=913#imgrc=Kg3TRY0jmx3udM", "team_info": {"team_id": "team_0", "team_name": "team_name0"}}, "actions": [{"action_id": 1, "action_type": "NO_VALIDATIONS", "button_text": "button_text_1", "button_color": null, "transition_template_id": "template_id_1"}, {"action_id": 2, "action_type": null, "button_text": "button_text_2", "button_color": null, "transition_template_id": "template_id_2"}]}, {"stage_id": 2, "stage_display_name": "name2", "stage_color": "color2", "task_stage_id": 2, "assignee": null, "actions": [{"action_id": 3, "action_type": "NO_VALIDATIONS", "button_text": "button_text_3", "button_color": null, "transition_template_id": "template_id_3"}, {"action_id": 4, "action_type": null, "button_text": "button_text_4", "button_color": null, "transition_template_id": "template_id_4"}]}, {"stage_id": 3, "stage_display_name": "name3", "stage_color": "color3", "task_stage_id": 3, "assignee": null, "actions": []}]}'

snapshots['TestGetTaskPresenterImplementation.test_user_not_a_member_of_project_raise_exception exception_object'] = b'{"response": "user not a member of the project", "http_status_code": 404, "res_status": "USER_NOT_A_MEMBER_OF_PROJECT"}'
