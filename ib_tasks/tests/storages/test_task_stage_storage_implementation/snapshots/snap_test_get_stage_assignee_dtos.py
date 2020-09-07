# -*- coding: utf-8 -*-
# snapshottest: v1 - https://goo.gl/zC4yUc
from __future__ import unicode_literals

from snapshottest import Snapshot, GenericRepr


snapshots = Snapshot()

snapshots['TestGetStageAssigneeDTOS.test_given_task_id_stage_ids_returns_task_stage_assignee_dtos task_stage_assignee_dtos'] = [
    GenericRepr("TaskStageAssigneeDTO(task_stage_id=1, stage_id=1, assignee_id='123e4567-e89b-12d3-a456-426614174000', team_id='team_1')"),
    GenericRepr("TaskStageAssigneeDTO(task_stage_id=2, stage_id=2, assignee_id='123e4567-e89b-12d3-a456-426614174001', team_id='team_2')"),
    GenericRepr("TaskStageAssigneeDTO(task_stage_id=3, stage_id=3, assignee_id='123e4567-e89b-12d3-a456-426614174002', team_id='team_3')"),
    GenericRepr("TaskStageAssigneeDTO(task_stage_id=4, stage_id=4, assignee_id='123e4567-e89b-12d3-a456-426614174003', team_id='team_4')")
]
