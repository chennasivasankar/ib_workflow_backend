# -*- coding: utf-8 -*-
# snapshottest: v1 - https://goo.gl/zC4yUc
from __future__ import unicode_literals

from snapshottest import Snapshot, GenericRepr


snapshots = Snapshot()

snapshots['TestGetStageDetailsDTOS.test_given_stage_ids_returns_stage_details_dtos stage_details_dto'] = [
    GenericRepr("CurrentStageDetailsDTO(stage_id='stage_id_7', stage_display_name='name_7')"),
    GenericRepr("CurrentStageDetailsDTO(stage_id='stage_id_8', stage_display_name='name_8')"),
    GenericRepr("CurrentStageDetailsDTO(stage_id='stage_id_9', stage_display_name='name_9')"),
    GenericRepr("CurrentStageDetailsDTO(stage_id='stage_id_10', stage_display_name='name_10')")
]
