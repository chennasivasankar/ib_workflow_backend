# -*- coding: utf-8 -*-
# snapshottest: v1 - https://goo.gl/zC4yUc
from __future__ import unicode_literals

from snapshottest import GenericRepr, Snapshot


snapshots = Snapshot()

snapshots['TestGetFieldIds.test_get_field_ids response'] = [
    GenericRepr("TaskTemplateStageFieldsDTO(task_template_id='task_template_id_0', stage_id='stage_id_0', field_ids=['FIELD_ID_1', 'FIELD_ID_2'])"),
    GenericRepr("TaskTemplateStageFieldsDTO(task_template_id='task_template_id_1', stage_id='stage_id_1', field_ids=['FIELD_ID_1', 'FIELD_ID_2'])"),
    GenericRepr("TaskTemplateStageFieldsDTO(task_template_id='task_template_id_2', stage_id='stage_id_2', field_ids=['FIELD_ID_1', 'FIELD_ID_2'])")
]
