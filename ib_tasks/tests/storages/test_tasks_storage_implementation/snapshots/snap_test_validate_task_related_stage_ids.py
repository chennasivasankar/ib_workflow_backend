# -*- coding: utf-8 -*-
# snapshottest: v1 - https://goo.gl/zC4yUc
from __future__ import unicode_literals

from snapshottest import GenericRepr, Snapshot


snapshots = Snapshot()

snapshots['TestValidateTaskStageIds.test_validate_stage_task_details response'] = [
    GenericRepr("GetTaskDetailsDTO(task_id=1, stage_id='stage_id_1')"),
    GenericRepr("GetTaskDetailsDTO(task_id=2, stage_id='stage_id_2')"),
    GenericRepr("GetTaskDetailsDTO(task_id=3, stage_id='stage_id_3')")
]
