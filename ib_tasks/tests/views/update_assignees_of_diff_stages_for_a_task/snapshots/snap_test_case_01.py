# -*- coding: utf-8 -*-
# snapshottest: v1 - https://goo.gl/zC4yUc
from __future__ import unicode_literals

from snapshottest import Snapshot, GenericRepr


snapshots = Snapshot()

snapshots['TestCase01UpdateAssigneesOfDiffStagesForATaskAPITestCase.test_case task_stage_objs'] = [
    {
        'assignee_id': 'assignee_id_1',
        'left_at': GenericRepr("datetime.datetime(2012, 10, 11, 0, 0)"),
        'stage_id': 1,
        'task_id': 1
    },
    {
        'assignee_id': '123e4567-e89b-12d3-a456-426614174001',
        'left_at': GenericRepr("datetime.datetime(2012, 10, 11, 0, 0)"),
        'stage_id': 2,
        'task_id': 1
    }
]

snapshots['TestCase01UpdateAssigneesOfDiffStagesForATaskAPITestCase.test_case status_code'] = '400'

snapshots['TestCase01UpdateAssigneesOfDiffStagesForATaskAPITestCase.test_case body'] = {
    'task_id': [
        'This field is required.'
    ]
}
