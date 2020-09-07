# -*- coding: utf-8 -*-
# snapshottest: v1 - https://goo.gl/zC4yUc
from __future__ import unicode_literals

from snapshottest import Snapshot


snapshots = Snapshot()

snapshots['TestUpdateTaskStageAssigneesPresenterImplementation.test_given_invalid_task_display_id_raise_exception response'] = b'{"response": "BWG-10 is invalid task_id send valid task_id", "http_status_code": 404, "res_status": "INVALID_TASK_ID"}'

snapshots['TestUpdateTaskStageAssigneesPresenterImplementation.test_given_duplication_of_stage_ids_raise_exception response'] = b'{"response": "Duplicate stage ids that you have sent are: [1, 2],please send unique stage ids", "http_status_code": 400, "res_status": "DUPLICATE_STAGE_IDS"}'

snapshots['TestUpdateTaskStageAssigneesPresenterImplementation.test_given_invalid_stage_ids_raise_exception response'] = b'{"response": "Invalid stage ids that you have sent are: [1, 2],please send valid stage ids", "http_status_code": 404, "res_status": "INVALID_STAGE_IDS"}'

snapshots['TestUpdateTaskStageAssigneesPresenterImplementation.test_given_virtual_stage_ids_raise_exception response'] = b'{"response": "Invalid stage ids that you have sent are: [1, 2],please send valid stage ids", "http_status_code": 400, "res_status": "VIRTUAL_STAGE_IDS"}'

snapshots['TestUpdateTaskStageAssigneesPresenterImplementation.test_given_invalid_user_id_raise_exception response'] = b'{"response": "User with id 123e4567-e89b-12d3-a456-42661417400 doesn\'t exist", "http_status_code": 404, "res_status": "INVALID_USER_ID"}'

snapshots['TestUpdateTaskStageAssigneesPresenterImplementation.test_given_stage_ids_having_invalid_permission_for_user response'] = b'{"response": "Stage ids with invalid permission of assignees that you have sent are: [1, 2],please assign valid assignees for stages", "http_status_code": 400, "res_status": "STAGE_IDS_WITH_INVALID_PERMISSION_OF_ASSIGNEE"}'
