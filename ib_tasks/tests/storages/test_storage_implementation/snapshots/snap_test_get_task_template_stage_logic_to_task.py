# -*- coding: utf-8 -*-
# snapshottest: v1 - https://goo.gl/zC4yUc
from __future__ import unicode_literals

from snapshottest import Snapshot, GenericRepr


snapshots = Snapshot()

snapshots['TestGetTaskTemplateStageLogicToTask.test_given_task_id_returns_stage_display_value_dtos stage_display_value_dtos'] = [
    GenericRepr("StageDisplayValueDTO(stage_id='stage_0', display_logic='', value=0)"),
    GenericRepr("StageDisplayValueDTO(stage_id='stage_3', display_logic='', value=3)"),
    GenericRepr("StageDisplayValueDTO(stage_id='stage_6', display_logic='', value=6)"),
    GenericRepr("StageDisplayValueDTO(stage_id='stage_9', display_logic='', value=9)")
]
