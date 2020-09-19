# -*- coding: utf-8 -*-
# snapshottest: v1 - https://goo.gl/zC4yUc
from __future__ import unicode_literals

from snapshottest import GenericRepr, Snapshot


snapshots = Snapshot()

snapshots['TestGetStageIdWithTemplateIdDTOs.test_when_stages_for_task_templates_exists_returns_dtos stage_id_with_template_id_dtos'] = [
    GenericRepr("StageIdWithTemplateIdDTO(template_id='template_1', stage_id=1)"),
    GenericRepr("StageIdWithTemplateIdDTO(template_id='template_2', stage_id=2)"),
    GenericRepr("StageIdWithTemplateIdDTO(template_id='template_1', stage_id=3)"),
    GenericRepr("StageIdWithTemplateIdDTO(template_id='template_2', stage_id=4)")
]

snapshots['TestGetStageIdWithTemplateIdDTOs.test_when_no_stages_for_task_templates_exists_returns_empty_list stage_id_with_template_id_dtos'] = [
]
