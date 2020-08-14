# -*- coding: utf-8 -*-
# snapshottest: v1 - https://goo.gl/zC4yUc
from __future__ import unicode_literals

from snapshottest import Snapshot, GenericRepr


snapshots = Snapshot()

snapshots['TestGetTaskIdsInteractor.test_with_valid_stage_ids_return_task_ids_with_stage_ids_dict response'] = [
    GenericRepr("TaskIdsDTO(unique_key='1', task_stage_ids=[TaskStageIdsDTO(task_id='TASK_ID_1', stage_id='STAGE_ID_1'), TaskStageIdsDTO(task_id='TASK_ID_2', stage_id='STAGE_ID_1'), TaskStageIdsDTO(task_id='TASK_ID_3', stage_id='STAGE_ID_1'), TaskStageIdsDTO(task_id='TASK_ID_4', stage_id='STAGE_ID_1'), TaskStageIdsDTO(task_id='TASK_ID_5', stage_id='STAGE_ID_2'), TaskStageIdsDTO(task_id='TASK_ID_6', stage_id='STAGE_ID_2'), TaskStageIdsDTO(task_id='TASK_ID_7', stage_id='STAGE_ID_2'), TaskStageIdsDTO(task_id='TASK_ID_8', stage_id='STAGE_ID_2')], total_tasks=100)"),
    GenericRepr("TaskIdsDTO(unique_key='1', task_stage_ids=[TaskStageIdsDTO(task_id='TASK_ID_9', stage_id='STAGE_ID_3'), TaskStageIdsDTO(task_id='TASK_ID_10', stage_id='STAGE_ID_3'), TaskStageIdsDTO(task_id='TASK_ID_11', stage_id='STAGE_ID_3'), TaskStageIdsDTO(task_id='TASK_ID_12', stage_id='STAGE_ID_3'), TaskStageIdsDTO(task_id='TASK_ID_13', stage_id='STAGE_ID_4'), TaskStageIdsDTO(task_id='TASK_ID_14', stage_id='STAGE_ID_4'), TaskStageIdsDTO(task_id='TASK_ID_15', stage_id='STAGE_ID_4'), TaskStageIdsDTO(task_id='TASK_ID_16', stage_id='STAGE_ID_4')], total_tasks=100)")
]
