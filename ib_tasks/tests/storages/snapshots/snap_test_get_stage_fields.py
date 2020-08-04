# -*- coding: utf-8 -*-
# snapshottest: v1 - https://goo.gl/zC4yUc
from __future__ import unicode_literals

from snapshottest import Snapshot, GenericRepr


snapshots = Snapshot()

snapshots['TestGetFieldIds.test_get_field_ids response'] = [
    GenericRepr("TaskTemplateStageFieldsDTO(task_template_id='task_template_id_0', task_id=0, stage_id='stage_id_0', field_ids=['field_id_1', 'field_id_2'])"),
    GenericRepr("TaskTemplateStageFieldsDTO(task_template_id='task_template_id_1', task_id=1, stage_id='stage_id_1', field_ids=['field_id_1', 'field_id_2'])"),
    GenericRepr("TaskTemplateStageFieldsDTO(task_template_id='task_template_id_2', task_id=2, stage_id='stage_id_2', field_ids=['field_id_1', 'field_id_2'])")
]
