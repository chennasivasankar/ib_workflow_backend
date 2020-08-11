# -*- coding: utf-8 -*-
# snapshottest: v1 - https://goo.gl/zC4yUc
from __future__ import unicode_literals

from snapshottest import GenericRepr, Snapshot


snapshots = Snapshot()

snapshots['TestGetActionDetails.test_get_action_details response'] = [
    GenericRepr("StageActionDetailsDTO(action_id=1, name='action_name_0', stage_id='stage_id_0', button_text='hey', button_color='#fafafa', action_type='action_type', transition_template_id='template_1')"),
    GenericRepr("StageActionDetailsDTO(action_id=2, name='action_name_1', stage_id='stage_id_0', button_text='hey', button_color='#fafafa', action_type='action_type', transition_template_id='template_2')"),
    GenericRepr("StageActionDetailsDTO(action_id=3, name='action_name_2', stage_id='stage_id_0', button_text='hey', button_color='#fafafa', action_type='action_type', transition_template_id='template_3')"),
    GenericRepr("StageActionDetailsDTO(action_id=4, name='action_name_3', stage_id='stage_id_1', button_text='hey', button_color='#fafafa', action_type='action_type', transition_template_id='template_4')"),
    GenericRepr("StageActionDetailsDTO(action_id=5, name='action_name_4', stage_id='stage_id_1', button_text='hey', button_color='#fafafa', action_type='action_type', transition_template_id='template_5')"),
    GenericRepr("StageActionDetailsDTO(action_id=6, name='action_name_5', stage_id='stage_id_1', button_text='hey', button_color='#fafafa', action_type='action_type', transition_template_id='template_6')"),
    GenericRepr("StageActionDetailsDTO(action_id=7, name='action_name_6', stage_id='stage_id_2', button_text='hey', button_color='#fafafa', action_type='action_type', transition_template_id='template_7')"),
    GenericRepr("StageActionDetailsDTO(action_id=8, name='action_name_7', stage_id='stage_id_2', button_text='hey', button_color='#fafafa', action_type='action_type', transition_template_id='template_8')"),
    GenericRepr("StageActionDetailsDTO(action_id=9, name='action_name_8', stage_id='stage_id_2', button_text='hey', button_color='#fafafa', action_type='action_type', transition_template_id='template_9')")
]

snapshots['TestGetActionDetails.test_given_stage_ids_has_no_permitted_actions response'] = [
]

snapshots['TestGetActionDetails.test_get_action_details_when_action_has_all_roles_permission response'] = [
    GenericRepr("StageActionDetailsDTO(action_id=1, name='action_name_0', stage_id='stage_id_0', button_text='hey', button_color='#fafafa', action_type='action_type', transition_template_id='template_1')"),
    GenericRepr("StageActionDetailsDTO(action_id=2, name='action_name_1', stage_id='stage_id_0', button_text='hey', button_color='#fafafa', action_type='action_type', transition_template_id='template_2')"),
    GenericRepr("StageActionDetailsDTO(action_id=3, name='action_name_2', stage_id='stage_id_0', button_text='hey', button_color='#fafafa', action_type='action_type', transition_template_id='template_3')"),
    GenericRepr("StageActionDetailsDTO(action_id=4, name='action_name_3', stage_id='stage_id_1', button_text='hey', button_color='#fafafa', action_type='action_type', transition_template_id='template_4')"),
    GenericRepr("StageActionDetailsDTO(action_id=5, name='action_name_4', stage_id='stage_id_1', button_text='hey', button_color='#fafafa', action_type='action_type', transition_template_id='template_5')"),
    GenericRepr("StageActionDetailsDTO(action_id=6, name='action_name_5', stage_id='stage_id_1', button_text='hey', button_color='#fafafa', action_type='action_type', transition_template_id='template_6')"),
    GenericRepr("StageActionDetailsDTO(action_id=7, name='action_name_6', stage_id='stage_id_2', button_text='hey', button_color='#fafafa', action_type='action_type', transition_template_id='template_7')"),
    GenericRepr("StageActionDetailsDTO(action_id=8, name='action_name_7', stage_id='stage_id_2', button_text='hey', button_color='#fafafa', action_type='action_type', transition_template_id='template_8')"),
    GenericRepr("StageActionDetailsDTO(action_id=9, name='action_name_8', stage_id='stage_id_2', button_text='hey', button_color='#fafafa', action_type='action_type', transition_template_id='template_9')")
]
