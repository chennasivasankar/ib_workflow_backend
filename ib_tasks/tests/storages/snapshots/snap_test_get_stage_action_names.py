# -*- coding: utf-8 -*-
# snapshottest: v1 - https://goo.gl/zC4yUc
from __future__ import unicode_literals

from snapshottest import Snapshot, GenericRepr


snapshots = Snapshot()

snapshots['TestGetStageActions.test_get_stage_actions result'] = [
    GenericRepr("StageActionNamesDTO(stage_id='stage_id_0', action_names=['action_name_0'])"),
    GenericRepr("StageActionNamesDTO(stage_id='stage_id_1', action_names=['action_name_1'])"),
    GenericRepr("StageActionNamesDTO(stage_id='stage_id_2', action_names=['action_name_2'])")
]
