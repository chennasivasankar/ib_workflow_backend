# -*- coding: utf-8 -*-
# snapshottest: v1 - https://goo.gl/zC4yUc
from __future__ import unicode_literals

from snapshottest import GenericRepr, Snapshot


snapshots = Snapshot()

snapshots['TestGetTaskStagesAndActions.test_given_task_id_but_task_has_no_actions_returns_actions_as_empty_list response'] = [
    GenericRepr("StageAndActionsDetailsDTO(db_stage_id=1, stage_id='stage_id_0', name='name_0', actions_dtos=[])"),
    GenericRepr("StageAndActionsDetailsDTO(db_stage_id=2, stage_id='stage_id_1', name='name_1', actions_dtos=[])"),
    GenericRepr("StageAndActionsDetailsDTO(db_stage_id=3, stage_id='stage_id_2', name='name_2', actions_dtos=[])")
]

snapshots['TestGetTaskStagesAndActions.test_given_task_id_with_one_stage_returns_stage_and_their_actions response'] = [
    GenericRepr("StageAndActionsDetailsDTO(db_stage_id=1, stage_id='stage_id_0', name='name_0', actions_dtos=[StageActionDetailsDTO(action_id=2, name='name_2', stage_id='stage_id_0', button_text='button_text_2', button_color=None, action_type='action_type_2', transition_template_id='template_id_2'), StageActionDetailsDTO(action_id=3, name='name_3', stage_id='stage_id_0', button_text='button_text_3', button_color=None, action_type='action_type_3', transition_template_id='template_id_3')])")
]

snapshots['TestGetTaskStagesAndActions.test_given_task_id_with_one_stage_without_no_actions_returns_actions_as_empty_list response'] = [
    GenericRepr("StageAndActionsDetailsDTO(db_stage_id=1, stage_id='stage_id_0', name='name_0', actions_dtos=[])")
]

snapshots['TestGetTaskStagesAndActions.test_when_user_has_permissions_get_stage_actions response'] = [
    GenericRepr("StageAndActionsDetailsDTO(db_stage_id=1, stage_id='stage_id_0', name='name_0', actions_dtos=[StageActionDetailsDTO(action_id=1, name='name_1', stage_id='stage_id_0', button_text='button_text_1', button_color=None, action_type='action_type_1', transition_template_id='template_id_1'), StageActionDetailsDTO(action_id=2, name='name_2', stage_id='stage_id_0', button_text='button_text_2', button_color=None, action_type='action_type_2', transition_template_id='template_id_2'), StageActionDetailsDTO(action_id=3, name='name_3', stage_id='stage_id_0', button_text='button_text_3', button_color=None, action_type='action_type_3', transition_template_id='template_id_3')])"),
    GenericRepr("StageAndActionsDetailsDTO(db_stage_id=2, stage_id='stage_id_1', name='name_1', actions_dtos=[StageActionDetailsDTO(action_id=4, name='name_4', stage_id='stage_id_1', button_text='button_text_4', button_color=None, action_type='action_type_4', transition_template_id='template_id_4'), StageActionDetailsDTO(action_id=5, name='name_5', stage_id='stage_id_1', button_text='button_text_5', button_color=None, action_type='action_type_5', transition_template_id='template_id_5')])"),
    GenericRepr("StageAndActionsDetailsDTO(db_stage_id=3, stage_id='stage_id_2', name='name_2', actions_dtos=[StageActionDetailsDTO(action_id=6, name='name_6', stage_id='stage_id_2', button_text='button_text_6', button_color=None, action_type='action_type_6', transition_template_id='template_id_6'), StageActionDetailsDTO(action_id=7, name='name_7', stage_id='stage_id_2', button_text='button_text_7', button_color=None, action_type='action_type_7', transition_template_id='template_id_7')])")
]

snapshots['TestGetTaskStagesAndActions.test_when_user_has_no_permissions_returns_empty_actions response'] = [
    GenericRepr("StageAndActionsDetailsDTO(db_stage_id=1, stage_id='stage_id_0', name='name_0', actions_dtos=[])"),
    GenericRepr("StageAndActionsDetailsDTO(db_stage_id=2, stage_id='stage_id_1', name='name_1', actions_dtos=[])"),
    GenericRepr("StageAndActionsDetailsDTO(db_stage_id=3, stage_id='stage_id_2', name='name_2', actions_dtos=[])")
]
