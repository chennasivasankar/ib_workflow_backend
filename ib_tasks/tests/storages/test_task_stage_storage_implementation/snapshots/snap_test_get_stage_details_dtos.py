# -*- coding: utf-8 -*-
# snapshottest: v1 - https://goo.gl/zC4yUc
from __future__ import unicode_literals

from snapshottest import Snapshot, GenericRepr


snapshots = Snapshot()

snapshots['TestGetStageDetailsDTOS.test_given_stage_ids_returns_stage_details_dtos stage_details_dto'] = [
    GenericRepr("CurrentStageDetailsDTO(stage_id='stage_id_0', stage_display_name='name_0')"),
    GenericRepr("CurrentStageDetailsDTO(stage_id='stage_id_1', stage_display_name='name_1')"),
    GenericRepr("CurrentStageDetailsDTO(stage_id='stage_id_2', stage_display_name='name_2')"),
    GenericRepr("CurrentStageDetailsDTO(stage_id='stage_id_3', stage_display_name='name_3')")
]
