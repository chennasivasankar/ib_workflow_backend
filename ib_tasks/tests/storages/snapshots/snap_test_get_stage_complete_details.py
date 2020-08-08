# -*- coding: utf-8 -*-
# snapshottest: v1 - https://goo.gl/zC4yUc
from __future__ import unicode_literals

from snapshottest import Snapshot, GenericRepr


snapshots = Snapshot()

snapshots['TestGetStagesDetails.test_get_stage_ids_details stage_details_dtos'] = [
    GenericRepr("StageDetailsDTO(db_stage_id=1, stage_id='stage_id_0', name='name_0', color='blue')"),
    GenericRepr("StageDetailsDTO(db_stage_id=2, stage_id='stage_id_1', name='name_1', color='blue')"),
    GenericRepr("StageDetailsDTO(db_stage_id=3, stage_id='stage_id_2', name='name_2', color='blue')"),
    GenericRepr("StageDetailsDTO(db_stage_id=4, stage_id='stage_id_3', name='name_3', color='blue')"),
    GenericRepr("StageDetailsDTO(db_stage_id=5, stage_id='stage_id_4', name='name_4', color='blue')"),
    GenericRepr("StageDetailsDTO(db_stage_id=6, stage_id='stage_id_5', name='name_5', color='blue')"),
    GenericRepr("StageDetailsDTO(db_stage_id=7, stage_id='stage_id_6', name='name_6', color='blue')"),
    GenericRepr("StageDetailsDTO(db_stage_id=8, stage_id='stage_id_7', name='name_7', color='blue')"),
    GenericRepr("StageDetailsDTO(db_stage_id=9, stage_id='stage_id_8', name='name_8', color='blue')"),
    GenericRepr("StageDetailsDTO(db_stage_id=10, stage_id='stage_id_9', name='name_9', color='blue')")
]
