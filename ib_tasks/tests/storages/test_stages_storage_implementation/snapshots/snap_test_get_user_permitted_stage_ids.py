# -*- coding: utf-8 -*-
# snapshottest: v1 - https://goo.gl/zC4yUc
from __future__ import unicode_literals

from snapshottest import Snapshot


snapshots = Snapshot()

snapshots['TestGetUserPermittedStageIds.test_when_user_permitted_stages_exists_returns_stage_ids user_permitted_stage_ids'] = [
    1,
    2
]

snapshots['TestGetUserPermittedStageIds.test_when_user_permitted_stages_not_exists_returns_empty_stage_ids user_permitted_stage_ids'] = [
]

snapshots['TestGetUserPermittedStageIds.test_when_user_permitted_stages_exists_with_all_role_ids_returns_stage_ids user_permitted_stage_ids'] = [
    1,
    2
]
