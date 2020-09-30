# -*- coding: utf-8 -*-
# snapshottest: v1 - https://goo.gl/zC4yUc
from __future__ import unicode_literals

from snapshottest import GenericRepr, Snapshot


snapshots = Snapshot()

snapshots['TestGetStageDisplayNameValueDtosForStageIds.test_given_stage_ids_returns_stage_display_name_value_dtos stage_display_name_value_dtos'] = [
    GenericRepr("StageDisplayNameValueDTO(stage_id='stage_0', name='display_name_0', value=0)"),
    GenericRepr("StageDisplayNameValueDTO(stage_id='stage_1', name='display_name_1', value=1)"),
    GenericRepr("StageDisplayNameValueDTO(stage_id='stage_2', name='display_name_2', value=2)"),
    GenericRepr("StageDisplayNameValueDTO(stage_id='stage_3', name='display_name_3', value=3)"),
    GenericRepr("StageDisplayNameValueDTO(stage_id='stage_4', name='display_name_4', value=4)")
]
