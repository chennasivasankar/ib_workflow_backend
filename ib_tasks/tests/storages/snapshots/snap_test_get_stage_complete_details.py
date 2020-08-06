# -*- coding: utf-8 -*-
# snapshottest: v1 - https://goo.gl/zC4yUc
from __future__ import unicode_literals

from snapshottest import GenericRepr, Snapshot

snapshots = Snapshot()

snapshots['TestGetStagesDetails.test_get_stage_ids_details stage_details_dtos'] = [
    GenericRepr("StageDetailsDTO(stage_id='stage_id_0', name='name_0')"),
    GenericRepr("StageDetailsDTO(stage_id='stage_id_1', name='name_1')"),
    GenericRepr("StageDetailsDTO(stage_id='stage_id_2', name='name_2')"),
    GenericRepr("StageDetailsDTO(stage_id='stage_id_3', name='name_3')"),
    GenericRepr("StageDetailsDTO(stage_id='stage_id_4', name='name_4')"),
    GenericRepr("StageDetailsDTO(stage_id='stage_id_5', name='name_5')"),
    GenericRepr("StageDetailsDTO(stage_id='stage_id_6', name='name_6')"),
    GenericRepr("StageDetailsDTO(stage_id='stage_id_7', name='name_7')"),
    GenericRepr("StageDetailsDTO(stage_id='stage_id_8', name='name_8')"),
    GenericRepr("StageDetailsDTO(stage_id='stage_id_9', name='name_9')")
]
