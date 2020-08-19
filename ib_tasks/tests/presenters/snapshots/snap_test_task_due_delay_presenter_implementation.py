# -*- coding: utf-8 -*-
# snapshottest: v1 - https://goo.gl/zC4yUc
from __future__ import unicode_literals

from snapshottest import Snapshot


snapshots = Snapshot()

snapshots['TestGetTaskDueDelay.test_response_invalid_task_id response'] = b'{"response": "iBWF-10 is invalid task_id send valid task_id", "http_status_code": 404, "res_status": "INVALID_TASK_ID"}'

snapshots['TestGetTaskDueDelay.test_response_for_user_is_not_assignee_for_task response'] = b'{"response": "user is not assigned to the task", "http_status_code": 403, "res_status": "USER_IS_NOT_ASSIGNED_TO_TASK"}'

snapshots['TestGetTaskDueDelay.test_get_response_for_get_task_due_details response'] = b'[{"task_id": "task_id_1", "reason": "reason_id_0", "due_date_time": "2020-08-14 00:00:00", "due_missed_count": 0, "user": {"user_id": "123e4567-e89b-12d3-a456-426614174000", "name": "name_0", "profile_pic": "https://www.google.com/search?q=ibhubs&client=ubuntu&hs=DI7&channel=fs&source=lnms&tbm=isch&sa=X&ved=2ahUKEwjZqYjthYfrAhUF4zgGHevjDZUQ_AUoA3oECAsQBQ&biw=1848&bih=913#imgrc=Kg3TRY0jmx3udM"}}, {"task_id": "task_id_2", "reason": "reason_id_1", "due_date_time": "2020-08-14 00:00:00", "due_missed_count": 1, "user": {"user_id": "123e4567-e89b-12d3-a456-426614174001", "name": "name_1", "profile_pic": "https://www.google.com/search?q=ibhubs&client=ubuntu&hs=DI7&channel=fs&source=lnms&tbm=isch&sa=X&ved=2ahUKEwjZqYjthYfrAhUF4zgGHevjDZUQ_AUoA3oECAsQBQ&biw=1848&bih=913#imgrc=Kg3TRY0jmx3udM"}}, {"task_id": "task_id_3", "reason": "reason_id_2", "due_date_time": "2020-08-14 00:00:00", "due_missed_count": 2, "user": {"user_id": "123e4567-e89b-12d3-a456-426614174002", "name": "name_2", "profile_pic": "https://www.google.com/search?q=ibhubs&client=ubuntu&hs=DI7&channel=fs&source=lnms&tbm=isch&sa=X&ved=2ahUKEwjZqYjthYfrAhUF4zgGHevjDZUQ_AUoA3oECAsQBQ&biw=1848&bih=913#imgrc=Kg3TRY0jmx3udM"}}, {"task_id": "task_id_4", "reason": "reason_id_3", "due_date_time": "2020-08-14 00:00:00", "due_missed_count": 3, "user": {"user_id": "123e4567-e89b-12d3-a456-426614174003", "name": "name_3", "profile_pic": "https://www.google.com/search?q=ibhubs&client=ubuntu&hs=DI7&channel=fs&source=lnms&tbm=isch&sa=X&ved=2ahUKEwjZqYjthYfrAhUF4zgGHevjDZUQ_AUoA3oECAsQBQ&biw=1848&bih=913#imgrc=Kg3TRY0jmx3udM"}}, {"task_id": "task_id_5", "reason": "reason_id_4", "due_date_time": "2020-08-14 00:00:00", "due_missed_count": 4, "user": {"user_id": "123e4567-e89b-12d3-a456-426614174004", "name": "name_4", "profile_pic": "https://www.google.com/search?q=ibhubs&client=ubuntu&hs=DI7&channel=fs&source=lnms&tbm=isch&sa=X&ved=2ahUKEwjZqYjthYfrAhUF4zgGHevjDZUQ_AUoA3oECAsQBQ&biw=1848&bih=913#imgrc=Kg3TRY0jmx3udM"}}]'

snapshots['TestAddTaskDueDelay.test_response_for_invalid_due_datetime response'] = b'{"response": "given updated due datetime is invalid", "http_status_code": 400, "res_status": "INVALID_DUE_DATE_TIME"}'

snapshots['TestAddTaskDueDelay.test_response_for_invalid_reason_id response'] = b'{"response": "given reason id is not in options", "http_status_code": 400, "res_status": "INVALID_REASON_ID"}'
