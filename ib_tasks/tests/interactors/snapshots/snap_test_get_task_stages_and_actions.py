# -*- coding: utf-8 -*-
# snapshottest: v1 - https://goo.gl/zC4yUc
from __future__ import unicode_literals

from snapshottest import Snapshot, GenericRepr


snapshots = Snapshot()

snapshots['TestGetTaskStagesAndActions.test_when_user_has_permissions_get_stage_actions response'] = [
    GenericRepr("StageAndActionsDetailsDTO(stage_id='stage_id_1', name='name_1', actions_dtos=[ActionDetailsDTO(action_id=1, name='name_1', stage_id='stage_id_1', button_text='button_text_1', button_color=None), ActionDetailsDTO(action_id=2, name='name_2', stage_id='stage_id_1', button_text='button_text_2', button_color=None), ActionDetailsDTO(action_id=3, name='name_3', stage_id='stage_id_1', button_text='button_text_3', button_color=None)])"),
    GenericRepr("StageAndActionsDetailsDTO(stage_id='stage_id_2', name='name_2', actions_dtos=[ActionDetailsDTO(action_id=4, name='name_4', stage_id='stage_id_2', button_text='button_text_4', button_color=None), ActionDetailsDTO(action_id=5, name='name_5', stage_id='stage_id_2', button_text='button_text_5', button_color=None)])"),
    GenericRepr("StageAndActionsDetailsDTO(stage_id='stage_id_3', name='name_3', actions_dtos=[ActionDetailsDTO(action_id=6, name='name_6', stage_id='stage_id_3', button_text='button_text_6', button_color=None), ActionDetailsDTO(action_id=7, name='name_7', stage_id='stage_id_3', button_text='button_text_7', button_color=None)])")
]

snapshots['TestGetTaskStagesAndActions.test_when_user_has_no_permissions_returns_empty_actions response'] = [
    GenericRepr("StageAndActionsDetailsDTO(stage_id='stage_id_1', name='name_1', actions_dtos=[])"),
    GenericRepr("StageAndActionsDetailsDTO(stage_id='stage_id_2', name='name_2', actions_dtos=[])"),
    GenericRepr("StageAndActionsDetailsDTO(stage_id='stage_id_3', name='name_3', actions_dtos=[])")
]
