# -*- coding: utf-8 -*-
# snapshottest: v1 - https://goo.gl/zC4yUc
from __future__ import unicode_literals

from snapshottest import Snapshot, GenericRepr


snapshots = Snapshot()

snapshots['TestGetStageDetailsDTOsGivenStageIds.test_given_stage_ids_returns_stage_details_dtos stage_details_dtos'] = [
    GenericRepr("StageDetailsDTO(db_stage_id=1, stage_id='stage_0', color='#fff2f0', name='display_name_0')"),
    GenericRepr("StageDetailsDTO(db_stage_id=2, stage_id='stage_1', color='#fff2f1', name='display_name_1')"),
    GenericRepr("StageDetailsDTO(db_stage_id=3, stage_id='stage_2', color='#fff2f2', name='display_name_2')"),
    GenericRepr("StageDetailsDTO(db_stage_id=4, stage_id='stage_3', color='#fff2f3', name='display_name_3')"),
    GenericRepr("StageDetailsDTO(db_stage_id=5, stage_id='stage_4', color='#fff2f4', name='display_name_4')")
]
