# -*- coding: utf-8 -*-
# snapshottest: v1 - https://goo.gl/zC4yUc
from __future__ import unicode_literals

from snapshottest import GenericRepr, Snapshot


snapshots = Snapshot()

snapshots['TestGetTaskStagesAndActions.test_given_task_id_returns_task_related_stages_and_their_actions response'] = [
    GenericRepr("StageAndActionsDetailsDTO(stage_id='stage_id_0', name='name_0', actions_dtos=[ActionDetailsDTO(action_id=1, name='name_1', stage_id='stage_id_0', button_text='button_text_1', button_color=None), ActionDetailsDTO(action_id=2, name='name_2', stage_id='stage_id_0', button_text='button_text_2', button_color=None)])"),
    GenericRepr("StageAndActionsDetailsDTO(stage_id='stage_id_1', name='name_1', actions_dtos=[ActionDetailsDTO(action_id=3, name='name_3', stage_id='stage_id_1', button_text='button_text_3', button_color=None)])"),
    GenericRepr("StageAndActionsDetailsDTO(stage_id='stage_id_2', name='name_2', actions_dtos=[ActionDetailsDTO(action_id=4, name='name_4', stage_id='stage_id_2', button_text='button_text_4', button_color=None)])")
]

snapshots['TestGetTaskStagesAndActions.test_given_task_id_but_task_has_no_actions_returns_actions_as_empty_list response'] = [
    GenericRepr("StageAndActionsDetailsDTO(stage_id='stage_id_0', name='name_0', actions_dtos=[])"),
    GenericRepr("StageAndActionsDetailsDTO(stage_id='stage_id_1', name='name_1', actions_dtos=[])"),
    GenericRepr("StageAndActionsDetailsDTO(stage_id='stage_id_2', name='name_2', actions_dtos=[])")
]

snapshots['TestGetTaskStagesAndActions.test_given_task_id_with_one_stage_returns_stage_and_their_actions response'] = [
    GenericRepr("StageAndActionsDetailsDTO(stage_id='stage_id_0', name='name_0', actions_dtos=[ActionDetailsDTO(action_id=1, name='name_1', stage_id='stage_id_0', button_text='button_text_1', button_color=None), ActionDetailsDTO(action_id=2, name='name_2', stage_id='stage_id_0', button_text='button_text_2', button_color=None)])")
]

snapshots['TestGetTaskStagesAndActions.test_given_task_id_with_one_stage_without_no_actions_returns_actions_as_empty_list response'] = [
    GenericRepr("StageAndActionsDetailsDTO(stage_id='stage_id_0', name='name_0', actions_dtos=[])")
]
