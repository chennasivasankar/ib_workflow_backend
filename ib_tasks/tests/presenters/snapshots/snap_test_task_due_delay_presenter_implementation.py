# -*- coding: utf-8 -*-
# snapshottest: v1 - https://goo.gl/zC4yUc
from __future__ import unicode_literals

from snapshottest import Snapshot


snapshots = Snapshot()

snapshots['TestGetTaskDueDelay.test_response_invalid_task_id response'] = b'{"response": "invalid task id is: -1, please send valid task id", "http_status_code": 404, "res_status": "INVALID_TASK_ID"}'

snapshots['TestGetTaskDueDelay.test_response_for_user_is_not_assignee_for_task response'] = b'{"response": "user is not assigned to the task", "http_status_code": 403, "res_status": "USER_IS_NOT_ASSIGNED_TO_TASK"}'

snapshots['TestAddTaskDueDelay.test_response_for_invalid_due_datetime response'] = b'{"response": "given updated due datetime is invalid", "http_status_code": 400, "res_status": "INVALID_DUE_DATE_TIME"}'

snapshots['TestAddTaskDueDelay.test_response_for_invalid_reason_id response'] = b'{"response": "given reason id is not in options", "http_status_code": 400, "res_status": "INVALID_REASON_ID"}'
