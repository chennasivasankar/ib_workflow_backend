# -*- coding: utf-8 -*-
# snapshottest: v1 - https://goo.gl/zC4yUc
from __future__ import unicode_literals

from snapshottest import Snapshot, GenericRepr


snapshots = Snapshot()

snapshots['TestTaskStageStorageImplementation.test_given_task_id_stage_ids_returns_task_stage_assignee_dtos task_stage_assignee_dtos'] = [
    GenericRepr("TaskStageAssigneeDTO(task_stage_id=1, stage_id=1, assignee_id='123e4567-e89b-12d3-a456-426614174000')"),
    GenericRepr("TaskStageAssigneeDTO(task_stage_id=2, stage_id=2, assignee_id='123e4567-e89b-12d3-a456-426614174001')"),
    GenericRepr("TaskStageAssigneeDTO(task_stage_id=3, stage_id=3, assignee_id='123e4567-e89b-12d3-a456-426614174002')"),
    GenericRepr("TaskStageAssigneeDTO(task_stage_id=4, stage_id=4, assignee_id='123e4567-e89b-12d3-a456-426614174003')")
]

snapshots['TestTaskStageStorageImplementation.test_given_stage_ids_returns_stage_details_dtos stage_details_dto'] = [
    GenericRepr("CurrentStageDetailsDTO(stage_id='stage_id_26', stage_display_name='name_26')"),
    GenericRepr("CurrentStageDetailsDTO(stage_id='stage_id_27', stage_display_name='name_27')"),
    GenericRepr("CurrentStageDetailsDTO(stage_id='stage_id_28', stage_display_name='name_28')"),
    GenericRepr("CurrentStageDetailsDTO(stage_id='stage_id_29', stage_display_name='name_29')")
]