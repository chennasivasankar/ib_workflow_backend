# -*- coding: utf-8 -*-
# snapshottest: v1 - https://goo.gl/zC4yUc
from __future__ import unicode_literals

from snapshottest import Snapshot, GenericRepr


snapshots = Snapshot()

snapshots['TestGetStageGoFDTOsForGivenStagesAndGoFs.test_when_stage_gofs_exists_returns_stage_gof_dtos stage_gofs'] = [
    GenericRepr("DBStageIdWithGoFIdDTO(stage_id=1, gof_id='gof_1')"),
    GenericRepr("DBStageIdWithGoFIdDTO(stage_id=1, gof_id='gof_3')"),
    GenericRepr("DBStageIdWithGoFIdDTO(stage_id=2, gof_id='gof_2')")
]

snapshots['TestGetStageGoFDTOsForGivenStagesAndGoFs.test_when_stage_gofs_not_exists_returns_empty_list stage_gofs'] = [
]
