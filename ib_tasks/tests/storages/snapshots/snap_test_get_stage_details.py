# -*- coding: utf-8 -*-
# snapshottest: v1 - https://goo.gl/zC4yUc
from __future__ import unicode_literals

from snapshottest import Snapshot, GenericRepr


snapshots = Snapshot()

snapshots['TestGetStageDetails.test_get_stage_details response'] = [
    GenericRepr("TaskTemplateStageDTO(task_id=1, task_template_id='task_template_id_1', stage_id='stage_id_1')"),
    GenericRepr("TaskTemplateStageDTO(task_id=2, task_template_id='task_template_id_1', stage_id='stage_id_2')"),
    GenericRepr("TaskTemplateStageDTO(task_id=3, task_template_id='task_template_id_1', stage_id='stage_id_3')")
]