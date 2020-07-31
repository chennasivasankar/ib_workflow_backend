# -*- coding: utf-8 -*-
# snapshottest: v1 - https://goo.gl/zC4yUc
from __future__ import unicode_literals

from snapshottest import GenericRepr, Snapshot


snapshots = Snapshot()

snapshots['TestGetTaskStagesAndActions.test_given_valid_details_get_details response'] = [
    GenericRepr("StageAndActionsDetailsDTO(stage_id='stage_id_0', name='name_0', actions_dtos=[])"),
    GenericRepr("StageAndActionsDetailsDTO(stage_id='stage_id_1', name='name_1', actions_dtos=[ActionDetailsDTO(action_id=1, name='name_1', stage_id='stage_id_1', button_text='button_text_1', button_color=None)])"),
    GenericRepr("StageAndActionsDetailsDTO(stage_id='stage_id_2', name='name_2', actions_dtos=[ActionDetailsDTO(action_id=2, name='name_2', stage_id='stage_id_2', button_text='button_text_2', button_color=None)])")
]
