# -*- coding: utf-8 -*-
# snapshottest: v1 - https://goo.gl/zC4yUc
from __future__ import unicode_literals

from snapshottest import Snapshot, GenericRepr


snapshots = Snapshot()

snapshots['TestGetTaskDueMissingDetails.test_get_due_details_of_task_given_task_id due_details'] = [
    GenericRepr("TaskDueMissingDTO(task_id='IBWF-1', due_date_time=FakeDatetime(2020, 9, 9, 13, 56, 40, 645996), due_missed_count=1, reason='wrong estimation of time', user_id='123e4567-e89b-12d3-a456-426614174000')"),
    GenericRepr("TaskDueMissingDTO(task_id='IBWF-1', due_date_time=FakeDatetime(2020, 9, 9, 13, 56, 40, 645996), due_missed_count=1, reason='wrong estimation of time', user_id='123e4567-e89b-12d3-a456-426614174001')")
]

snapshots['TestGetTaskDueMissingDetails.test_get_due_details_of_task_when_task_has_no_delays due_details'] = [
]
