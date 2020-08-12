# -*- coding: utf-8 -*-
# snapshottest: v1 - https://goo.gl/zC4yUc
from __future__ import unicode_literals

from snapshottest import Snapshot, GenericRepr

snapshots = Snapshot()

snapshots['TestGetFieldIds.test_get_field_ids_when_one_task_is_in_two_stages response'] = [
    GenericRepr("TaskTemplateStageFieldsDTO(task_template_id='task_template_id_0', task_id=1, stage_id='stage_id_0', stage_color='green', field_ids=['field_id_1', 'field_id_2'])"),
    GenericRepr("TaskTemplateStageFieldsDTO(task_template_id='task_template_id_0', task_id=1, stage_id='stage_id_1', stage_color='blue', field_ids=['field_id_5', 'field_id_6'])"),
    GenericRepr("TaskTemplateStageFieldsDTO(task_template_id='task_template_id_2', task_id=2, stage_id='stage_id_2', stage_color='orange', field_ids=['field_id_7', 'field_id_8'])"),
    GenericRepr("TaskTemplateStageFieldsDTO(task_template_id='task_template_id_3', task_id=2, stage_id='stage_id_3', stage_color='green', field_ids=['field_id_9', 'field_id_10'])")
]

snapshots['TestGetFieldIds.test_get_field_ids_when_two_tasks_are_in_one_stage response'] = [
    GenericRepr("TaskTemplateStageFieldsDTO(task_template_id='task_template_id_0', task_id=0, stage_id='stage_id_0', stage_color='orange', field_ids=['field_id_1', 'field_id_2'])"),
    GenericRepr("TaskTemplateStageFieldsDTO(task_template_id='task_template_id_0', task_id=1, stage_id='stage_id_0', stage_color='orange', field_ids=['field_id_1', 'field_id_2'])")
]

snapshots['TestGetFieldIds.test_get_field_ids_when_view_type_is_list response'] = [
    GenericRepr("TaskTemplateStageFieldsDTO(task_template_id='task_template_id_0', task_id=0, stage_id='stage_id_0', stage_color='blue', field_ids=['field_id_1', 'field_id_2'])"),
    GenericRepr("TaskTemplateStageFieldsDTO(task_template_id='task_template_id_1', task_id=1, stage_id='stage_id_1', stage_color='orange', field_ids=['field_id_5', 'field_id_6'])"),
    GenericRepr("TaskTemplateStageFieldsDTO(task_template_id='task_template_id_2', task_id=2, stage_id='stage_id_2', stage_color='green', field_ids=['field_id_7', 'field_id_8'])")
]

snapshots['TestGetFieldIds.test_get_field_ids_when_view_type_is_kanban response'] = [
    GenericRepr("TaskTemplateStageFieldsDTO(task_template_id='task_template_id_0', task_id=0, stage_id='stage_id_0', stage_color='orange', field_ids=['field_id_1', 'field_id_2'])"),
    GenericRepr("TaskTemplateStageFieldsDTO(task_template_id='task_template_id_1', task_id=1, stage_id='stage_id_1', stage_color='green', field_ids=['field_id_3', 'field_id_4'])"),
    GenericRepr("TaskTemplateStageFieldsDTO(task_template_id='task_template_id_2', task_id=2, stage_id='stage_id_2', stage_color='blue', field_ids=['field_id_5', 'field_id_6'])")
]
