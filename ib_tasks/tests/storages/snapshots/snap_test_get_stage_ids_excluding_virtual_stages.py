# -*- coding: utf-8 -*-
# snapshottest: v1 - https://goo.gl/zC4yUc
from __future__ import unicode_literals

from snapshottest import Snapshot


snapshots = Snapshot()

snapshots['TestGetStageIdsWithoutVirtualStages.test_given_stage_ids_returns_stage_ids_with_out_virtual_stages stage_ids_without_virtual_stages'] = [
    'stage_0',
    'stage_2',
    'stage_3',
    'stage_5',
    'stage_6',
    'stage_8',
    'stage_9'
]
