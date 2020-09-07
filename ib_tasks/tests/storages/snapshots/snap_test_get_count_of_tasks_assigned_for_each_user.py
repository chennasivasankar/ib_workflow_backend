# -*- coding: utf-8 -*-
# snapshottest: v1 - https://goo.gl/zC4yUc
from __future__ import unicode_literals

from snapshottest import GenericRepr, Snapshot


snapshots = Snapshot()

snapshots['TestGetCountOfTasksAssignedForEachUser.test_given_db_stage_ids_and_task_ids_returns_assignee_current_tasks_count_dtos assignee_with_current_tasks_count_dtos'] = [
    GenericRepr("AssigneeCurrentTasksCountDTO(assignee_id='123e4567-e89b-12d3-a456-426614174002', tasks_count=2)"),
    GenericRepr("AssigneeCurrentTasksCountDTO(assignee_id='123e4567-e89b-12d3-a456-426614174003', tasks_count=2)"),
    GenericRepr("AssigneeCurrentTasksCountDTO(assignee_id='123e4567-e89b-12d3-a456-426614174000', tasks_count=3)"),
    GenericRepr("AssigneeCurrentTasksCountDTO(assignee_id='123e4567-e89b-12d3-a456-426614174001', tasks_count=3)")
]
