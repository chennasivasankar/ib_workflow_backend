# -*- coding: utf-8 -*-
# snapshottest: v1 - https://goo.gl/zC4yUc
from __future__ import unicode_literals

from snapshottest import Snapshot


snapshots = Snapshot()

snapshots['TestGetTaskDueDelay.test_response_invalid_task_id response'] = b'{"response": "invalid task id is: -1, please send valid task id", "http_status_code": 404, "res_status": "INVALID_TASK_ID"}'

snapshots['TestGetTaskDueDelay.test_response_for_user_is_not_assignee_for_task response'] = b'{"response": "user is not assigned to the task", "http_status_code": 403, "res_status": "USER_IS_NOT_ASSIGNED_TO_TASK"}'

snapshots['TestGetTaskDueDelay.test_get_response_for_get_task_due_details response'] = b'[{"task_id": "task_id_1", "reason": "reason_id_0", "due_date_time": "2020-08-10T21:02:37.1597073557Z", "due_missed_count": 0, "user": {"user_id": "user_id_0", "name": "name_0", "profile_pic": "pic_url"}}, {"task_id": "task_id_2", "reason": "reason_id_1", "due_date_time": "2020-08-10T21:02:37.1597073557Z", "due_missed_count": 1, "user": {"user_id": "user_id_1", "name": "name_1", "profile_pic": "pic_url"}}, {"task_id": "task_id_3", "reason": "reason_id_2", "due_date_time": "2020-08-10T21:02:37.1597073557Z", "due_missed_count": 2, "user": {"user_id": "user_id_2", "name": "name_2", "profile_pic": "pic_url"}}, {"task_id": "task_id_4", "reason": "reason_id_3", "due_date_time": "2020-08-10T21:02:37.1597073557Z", "due_missed_count": 3, "user": {"user_id": "user_id_3", "name": "name_3", "profile_pic": "pic_url"}}, {"task_id": "task_id_5", "reason": "reason_id_4", "due_date_time": "2020-08-10T21:02:37.1597073557Z", "due_missed_count": 4, "user": {"user_id": "user_id_4", "name": "name_4", "profile_pic": "pic_url"}}]'
