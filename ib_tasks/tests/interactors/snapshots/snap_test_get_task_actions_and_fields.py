# -*- coding: utf-8 -*-
# snapshottest: v1 - https://goo.gl/zC4yUc
from __future__ import unicode_literals

from snapshottest import Snapshot, GenericRepr




snapshots = Snapshot()

snapshots['TestGetFieldsAndActionsInteractor.test_get_actions_and_fields_when_task_has_no_actions_or_fields_returns_empty_list response'] = [
    GenericRepr("GetTaskStageCompleteDetailsDTO(task_id=1, stage_id='stage_id_1', field_dtos=[], action_dtos=[])"),
    GenericRepr("GetTaskStageCompleteDetailsDTO(task_id=1, stage_id='stage_id_2', field_dtos=[], action_dtos=[])")
]

snapshots['TestGetFieldsAndActionsInteractor.test_get_actions_and_fields_given_valid_task_template_id_and_stage_id response'] = [
    GenericRepr("GetTaskStageCompleteDetailsDTO(task_id=1, stage_id='stage_id_1', field_dtos=[FieldDetailsDTO(field_type='Drop down', field_id='FIELD-ID-1', key='key', value='value'), FieldDetailsDTO(field_type='Drop down', field_id='FIELD-ID-2', key='key', value='value')], action_dtos=[StageActionDetailsDTO(action_id=1, name='name_1', stage_id='stage_id_1', button_text='button_text_1', button_color=None, action_type='action_type_1', transition_template_id='template_id_1'), StageActionDetailsDTO(action_id=2, name='name_2', stage_id='stage_id_1', button_text='button_text_2', button_color=None, action_type='action_type_2', transition_template_id='template_id_2')])"),
    GenericRepr("GetTaskStageCompleteDetailsDTO(task_id=2, stage_id='stage_id_2', field_dtos=[FieldDetailsDTO(field_type='Drop down', field_id='FIELD-ID-3', key='key', value='value'), FieldDetailsDTO(field_type='Drop down', field_id='FIELD-ID-4', key='key', value='value')], action_dtos=[StageActionDetailsDTO(action_id=3, name='name_3', stage_id='stage_id_2', button_text='button_text_3', button_color=None, action_type='action_type_3', transition_template_id='template_id_3'), StageActionDetailsDTO(action_id=4, name='name_4', stage_id='stage_id_2', button_text='button_text_4', button_color=None, action_type='action_type_4', transition_template_id='template_id_4')])")
]

snapshots['TestGetFieldsAndActionsInteractor.test_get_actions_and_fields_when_two_tasks_are_in_same_stage response'] = [
    GenericRepr("GetTaskStageCompleteDetailsDTO(task_id=1, stage_id='stage_id_1', field_dtos=[FieldDetailsDTO(field_type='Drop down', field_id='FIELD-ID-1', key='key', value='value'), FieldDetailsDTO(field_type='Drop down', field_id='FIELD-ID-2', key='key', value='value'), FieldDetailsDTO(field_type='Drop down', field_id='FIELD-ID-1', key='key', value='value'), FieldDetailsDTO(field_type='Drop down', field_id='FIELD-ID-2', key='key', value='value')], action_dtos=[StageActionDetailsDTO(action_id=1, name='name_1', stage_id='stage_id_1', button_text='button_text_1', button_color=None, action_type='action_type_1', transition_template_id='template_id_1'), StageActionDetailsDTO(action_id=2, name='name_2', stage_id='stage_id_1', button_text='button_text_2', button_color=None, action_type='action_type_2', transition_template_id='template_id_2')])"),
    GenericRepr("GetTaskStageCompleteDetailsDTO(task_id=2, stage_id='stage_id_1', field_dtos=[], action_dtos=[StageActionDetailsDTO(action_id=1, name='name_1', stage_id='stage_id_1', button_text='button_text_1', button_color=None, action_type='action_type_1', transition_template_id='template_id_1'), StageActionDetailsDTO(action_id=2, name='name_2', stage_id='stage_id_1', button_text='button_text_2', button_color=None, action_type='action_type_2', transition_template_id='template_id_2')])")
]

snapshots['TestGetFieldsAndActionsInteractor.test_get_actions_and_fields_when_task_is_in_two_stages response'] = [
    GenericRepr("GetTaskStageCompleteDetailsDTO(task_id=1, stage_id='stage_id_1', field_dtos=[FieldDetailsDTO(field_type='Drop down', field_id='FIELD-ID-1', key='key', value='value'), FieldDetailsDTO(field_type='Drop down', field_id='FIELD-ID-2', key='key', value='value')], action_dtos=[StageActionDetailsDTO(action_id=1, name='name_1', stage_id='stage_id_1', button_text='button_text_1', button_color=None, action_type='action_type_1', transition_template_id='template_id_1'), StageActionDetailsDTO(action_id=2, name='name_2', stage_id='stage_id_1', button_text='button_text_2', button_color=None, action_type='action_type_2', transition_template_id='template_id_2')])"),
    GenericRepr("GetTaskStageCompleteDetailsDTO(task_id=1, stage_id='stage_id_2', field_dtos=[FieldDetailsDTO(field_type='Drop down', field_id='FIELD-ID-1', key='key', value='value'), FieldDetailsDTO(field_type='Drop down', field_id='FIELD-ID-2', key='key', value='value')], action_dtos=[StageActionDetailsDTO(action_id=3, name='name_3', stage_id='stage_id_2', button_text='button_text_3', button_color=None, action_type='action_type_3', transition_template_id='template_id_3'), StageActionDetailsDTO(action_id=4, name='name_4', stage_id='stage_id_2', button_text='button_text_4', button_color=None, action_type='action_type_4', transition_template_id='template_id_4')])")
]

snapshots['TestGetFieldsAndActionsInteractor.test_get_user_permitted_fields_and_actions response'] = [
    GenericRepr("GetTaskStageCompleteDetailsDTO(task_id=1, stage_id='stage_id_1', field_dtos=[FieldDetailsDTO(field_type='Drop down', field_id='FIELD-ID-1', key='key', value='value'), FieldDetailsDTO(field_type='Drop down', field_id='FIELD-ID-2', key='key', value='value')], action_dtos=[StageActionDetailsDTO(action_id=1, name='name_1', stage_id='stage_id_1', button_text='button_text_1', button_color=None, action_type='action_type_1', transition_template_id='template_id_1'), StageActionDetailsDTO(action_id=2, name='name_2', stage_id='stage_id_1', button_text='button_text_2', button_color=None, action_type='action_type_2', transition_template_id='template_id_2')])"),
    GenericRepr("GetTaskStageCompleteDetailsDTO(task_id=2, stage_id='stage_id_2', field_dtos=[FieldDetailsDTO(field_type='Drop down', field_id='FIELD-ID-3', key='key', value='value'), FieldDetailsDTO(field_type='Drop down', field_id='FIELD-ID-4', key='key', value='value')], action_dtos=[StageActionDetailsDTO(action_id=3, name='name_3', stage_id='stage_id_2', button_text='button_text_3', button_color=None, action_type='action_type_3', transition_template_id='template_id_3'), StageActionDetailsDTO(action_id=4, name='name_4', stage_id='stage_id_2', button_text='button_text_4', button_color=None, action_type='action_type_4', transition_template_id='template_id_4')])")
]

snapshots['TestGetFieldsAndActionsInteractor.test_get_actions_and_fields_given_valid_task_template_id_and_stage_id_and_field_type_is_kanban response'] = [
    GenericRepr("GetTaskStageCompleteDetailsDTO(task_id=1, stage_id='stage_id_1', field_dtos=[FieldDetailsDTO(field_type='Drop down', field_id='FIELD-ID-2', key='key', value='value')], action_dtos=[StageActionDetailsDTO(action_id=1, name='name_1', stage_id='stage_id_1', button_text='button_text_1', button_color=None, action_type='action_type_1', transition_template_id='template_id_1'), StageActionDetailsDTO(action_id=2, name='name_2', stage_id='stage_id_1', button_text='button_text_2', button_color=None, action_type='action_type_2', transition_template_id='template_id_2')])"),
    GenericRepr("GetTaskStageCompleteDetailsDTO(task_id=2, stage_id='stage_id_2', field_dtos=[FieldDetailsDTO(field_type='Drop down', field_id='FIELD-ID-4', key='key', value='value')], action_dtos=[StageActionDetailsDTO(action_id=3, name='name_3', stage_id='stage_id_2', button_text='button_text_3', button_color=None, action_type='action_type_3', transition_template_id='template_id_3'), StageActionDetailsDTO(action_id=4, name='name_4', stage_id='stage_id_2', button_text='button_text_4', button_color=None, action_type='action_type_4', transition_template_id='template_id_4')])")
]
