# -*- coding: utf-8 -*-
# snapshottest: v1 - https://goo.gl/zC4yUc
from __future__ import unicode_literals

from snapshottest import Snapshot


snapshots = Snapshot()

snapshots['TestGetTaskRelatedRps.test_response_invalid_task_id response'] = b'{"response": "iBWF-10 is invalid task_id send valid task_id", "http_status_code": 404, "res_status": "INVALID_TASK_ID"}'

snapshots['TestGetTaskRelatedRps.test_response_for_user_is_not_assignee_for_task response'] = b'{"response": "user is not assigned to the task", "http_status_code": 403, "res_status": "USER_IS_NOT_ASSIGNED_TO_TASK"}'

snapshots['TestGetTaskRelatedRps.test_response_for_invalid_stage_id response'] = b'{"response": "please give a valid stage id", "http_status_code": 404, "res_status": "INVALID_STAGE_ID"}'

snapshots['TestGetTaskRelatedRps.test_response_for_get_task_rps_details response'] = b'[{"user_id": "123e4567-e89b-12d3-a456-426614174000", "name": "name_0", "profile_pic_url": "pic_url"}, {"user_id": "123e4567-e89b-12d3-a456-426614174001", "name": "name_1", "profile_pic_url": "pic_url"}, {"user_id": "123e4567-e89b-12d3-a456-426614174002", "name": "name_2", "profile_pic_url": "pic_url"}, {"user_id": "123e4567-e89b-12d3-a456-426614174003", "name": "name_3", "profile_pic_url": "pic_url"}]'

snapshots['TestGetTaskRelatedRps.test_response_for_due_date_does_not_exist_to_task response'] = b'{"response": "please add due date to task", "http_status_code": 404, "res_status": "DUE_DATE_IS_NOT_ADDED_TO_TASK"}'
