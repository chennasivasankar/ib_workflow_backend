# -*- coding: utf-8 -*-
# snapshottest: v1 - https://goo.gl/zC4yUc
from __future__ import unicode_literals

from snapshottest import GenericRepr, Snapshot


snapshots = Snapshot()

snapshots['TestGetDBStageIdsWithStageIds.test_when_stage_ids_exists_returns_dtos db_stage_ids_with_stage_ids_dtos'] = [
    GenericRepr("DBStageIdWithStageIdDTO(db_stage_id=1, stage_id='stage_0')"),
    GenericRepr("DBStageIdWithStageIdDTO(db_stage_id=2, stage_id='stage_1')")
]

snapshots['TestGetDBStageIdsWithStageIds.test_when_stage_ids_not_exists_returns_empty_dtos db_stage_ids_with_stage_ids_dtos'] = [
]
