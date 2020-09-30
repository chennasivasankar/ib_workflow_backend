# -*- coding: utf-8 -*-
# snapshottest: v1 - https://goo.gl/zC4yUc
from __future__ import unicode_literals

from snapshottest import GenericRepr, Snapshot


snapshots = Snapshot()

snapshots['TestGetExistingGoFIdsWithStageIdOfStages.test_when_stage_gofs_exists_for_given_stages_returns_db_stage_id_with_gof_id_dtos db_stage_id_with_gof_id_dtos'] = [
    GenericRepr("DBStageIdWithGoFIdDTO(stage_id=1, gof_id='gof_1')"),
    GenericRepr("DBStageIdWithGoFIdDTO(stage_id=1, gof_id='gof_3')"),
    GenericRepr("DBStageIdWithGoFIdDTO(stage_id=2, gof_id='gof_2')"),
    GenericRepr("DBStageIdWithGoFIdDTO(stage_id=2, gof_id='gof_4')")
]

snapshots['TestGetExistingGoFIdsWithStageIdOfStages.test_when_stage_gofs_not_exists_for_given_stages_returns_empty_list db_stage_id_with_gof_id_dtos'] = [
]
