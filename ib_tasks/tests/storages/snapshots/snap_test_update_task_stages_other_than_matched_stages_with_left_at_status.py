# -*- coding: utf-8 -*-
# snapshottest: v1 - https://goo.gl/zC4yUc
from __future__ import unicode_literals

from snapshottest import GenericRepr, Snapshot


snapshots = Snapshot()

snapshots['TestUpdateTaskStagesWithLeftAtStatus.test_update_task_stages_other_than_matched_stages_with_left_at_status task_stage_objs'] = [
    {
        'assignee_id': '123e4567-e89b-12d3-a456-426614174000',
        'left_at': GenericRepr("FakeDatetime(2020, 8, 10, 12, 30)"),
        'stage_id': 1,
        'task_id': 1
    },
    {
        'assignee_id': '123e4567-e89b-12d3-a456-426614174001',
        'left_at': GenericRepr("FakeDatetime(2020, 8, 10, 12, 30)"),
        'stage_id': 2,
        'task_id': 1
    },
    {
        'assignee_id': '123e4567-e89b-12d3-a456-426614174002',
        'left_at': GenericRepr("FakeDatetime(2012, 10, 11, 0, 0)"),
        'stage_id': 3,
        'task_id': 1
    },
    {
        'assignee_id': '123e4567-e89b-12d3-a456-426614174003',
        'left_at': GenericRepr("FakeDatetime(2012, 10, 11, 0, 0)"),
        'stage_id': 4,
        'task_id': 1
    }
]
