# -*- coding: utf-8 -*-
# snapshottest: v1 - https://goo.gl/zC4yUc
from __future__ import unicode_literals

from snapshottest import GenericRepr, Snapshot


snapshots = Snapshot()

snapshots['TestGetActionDetails.test_get_action_details response'] = [
    GenericRepr("StageActionDetailsDTO(action_id=1, name='action_name_0', stage_id='stage_id_0', button_text='hey', button_color='#fafafa', action_type='action_type', transition_template_id='template_1')"),
    GenericRepr("StageActionDetailsDTO(action_id=2, name='action_name_1', stage_id='stage_id_0', button_text='hey', button_color='#fafafa', action_type='action_type', transition_template_id='template_2')"),
    GenericRepr("StageActionDetailsDTO(action_id=3, name='action_name_2', stage_id='stage_id_0', button_text='hey', button_color='#fafafa', action_type='action_type', transition_template_id='template_3')"),
    GenericRepr("StageActionDetailsDTO(action_id=4, name='action_name_3', stage_id='stage_id_1', button_text='hey', button_color='#fafafa', action_type='action_type', transition_template_id='template_4')")
]

snapshots['TestGetActionDetails.test_get_permitted_action_ids_given_stage_ids response'] = [
    1,
    2,
    3,
    4,
    5,
    6,
    7,
    8,
    9
]
