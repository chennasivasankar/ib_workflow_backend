# -*- coding: utf-8 -*-
# snapshottest: v1 - https://goo.gl/zC4yUc
from __future__ import unicode_literals

from snapshottest import Snapshot, GenericRepr


snapshots = Snapshot()

snapshots['TestGetColumnStageIds.test_get_column_stages_in_display_order response'] = [
    GenericRepr("ColumnStageIdsDTO(column_id='COLUMN_ID_2', stage_ids=['stage_id_1', 'stage_id_2', 'stage_id_3'])"),
    GenericRepr("ColumnStageIdsDTO(column_id='COLUMN_ID_3', stage_ids=['stage_id_1', 'stage_id_2', 'stage_id_3'])"),
    GenericRepr("ColumnStageIdsDTO(column_id='COLUMN_ID_4', stage_ids=['stage_id_1', 'stage_id_2', 'stage_id_3'])"),
    GenericRepr("ColumnStageIdsDTO(column_id='COLUMN_ID_1', stage_ids=['stage_id_1', 'stage_id_2', 'stage_id_3'])")
]
