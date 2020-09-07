# -*- coding: utf-8 -*-
# snapshottest: v1 - https://goo.gl/zC4yUc
from __future__ import unicode_literals

from snapshottest import Snapshot


snapshots = Snapshot()

snapshots['TestUpdateTaskStageAssigneesPresenterImplementation.test_with_invalid_task_display_id http_status_code'] = 404

snapshots['TestUpdateTaskStageAssigneesPresenterImplementation.test_with_invalid_task_display_id res_status'] = 'INVALID_TASK_ID'

snapshots['TestUpdateTaskStageAssigneesPresenterImplementation.test_with_invalid_task_display_id json_response'] = 'task_display_id is invalid task_id send valid task_id'

snapshots['TestUpdateTaskStageAssigneesPresenterImplementation.test_with_duplicate_stage_ids http_status_code'] = 400

snapshots['TestUpdateTaskStageAssigneesPresenterImplementation.test_with_duplicate_stage_ids res_status'] = 'DUPLICATE_STAGE_IDS'

snapshots['TestUpdateTaskStageAssigneesPresenterImplementation.test_with_duplicate_stage_ids json_response'] = 'Duplicate stage ids that you have sent are: [2, 2],please send unique stage ids'

snapshots['TestUpdateTaskStageAssigneesPresenterImplementation.test_given_invalid_stage_ids_raise_exception http_status_code'] = 404

snapshots['TestUpdateTaskStageAssigneesPresenterImplementation.test_given_invalid_stage_ids_raise_exception res_status'] = 'INVALID_STAGE_IDS'

snapshots['TestUpdateTaskStageAssigneesPresenterImplementation.test_given_invalid_stage_ids_raise_exception json_response'] = 'Invalid stage ids that you have sent are: [1, 2],please send valid stage ids'

snapshots['TestUpdateTaskStageAssigneesPresenterImplementation.test_given_virtual_stageids_raise_exception http_status_code'] = 400

snapshots['TestUpdateTaskStageAssigneesPresenterImplementation.test_given_virtual_stageids_raise_exception res_status'] = 'VIRTUAL_STAGE_IDS'

snapshots['TestUpdateTaskStageAssigneesPresenterImplementation.test_given_virtual_stageids_raise_exception json_response'] = 'Invalid stage ids that you have sent are: [1, 2],please send valid stage ids'

snapshots['TestUpdateTaskStageAssigneesPresenterImplementation.test_raise_stage_ids_with_invalid_permission_for_assignee_exception http_status_code'] = 400

snapshots['TestUpdateTaskStageAssigneesPresenterImplementation.test_raise_stage_ids_with_invalid_permission_for_assignee_exception res_status'] = 'STAGE_IDS_WITH_INVALID_PERMISSION_OF_ASSIGNEE'

snapshots['TestUpdateTaskStageAssigneesPresenterImplementation.test_raise_stage_ids_with_invalid_permission_for_assignee_exception json_response'] = 'Stage ids with invalid permission of assignees that you have sent are: [1, 2],please assign valid assignees for stages'

snapshots['TestUpdateTaskStageAssigneesPresenterImplementation.test_raise_invalid_user_id_exception http_status_code'] = 404

snapshots['TestUpdateTaskStageAssigneesPresenterImplementation.test_raise_invalid_user_id_exception res_status'] = 'USER_NOT_IN_PROJECT'

snapshots['TestUpdateTaskStageAssigneesPresenterImplementation.test_raise_invalid_user_id_exception json_response'] = 'User Not a part of the Project'
