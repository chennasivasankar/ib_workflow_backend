# -*- coding: utf-8 -*-
# snapshottest: v1 - https://goo.gl/zC4yUc
from __future__ import unicode_literals

from snapshottest import GenericRepr, Snapshot


snapshots = Snapshot()

snapshots['TestGetFieldsAndActionsInteractor.test_get_actions_and_fields_given_valid_task_template_id_and_stage_id response'] = [
    GenericRepr("GetTaskStageCompleteDetailsDTO(task_id=1, stage_id='stage_id_1', field_dtos=[FieldDetailsDTO(field_type='Drop down', field_id='FIELD-ID-1', key='key', value='value'), FieldDetailsDTO(field_type='Drop down', field_id='FIELD-ID-2', key='key', value='value')], action_dtos=[ActionDetailsDTO(action_id=1, name='name_1', stage_id='stage_id_1', button_text='button_text_1', button_color=None), ActionDetailsDTO(action_id=2, name='name_2', stage_id='stage_id_1', button_text='button_text_2', button_color=None)])"),
    GenericRepr("GetTaskStageCompleteDetailsDTO(task_id=1, stage_id='stage_id_2', field_dtos=[FieldDetailsDTO(field_type='Drop down', field_id='FIELD-ID-3', key='key', value='value'), FieldDetailsDTO(field_type='Drop down', field_id='FIELD-ID-4', key='key', value='value')], action_dtos=[ActionDetailsDTO(action_id=3, name='name_3', stage_id='stage_id_2', button_text='button_text_3', button_color=None), ActionDetailsDTO(action_id=4, name='name_4', stage_id='stage_id_2', button_text='button_text_4', button_color=None)])")
]
