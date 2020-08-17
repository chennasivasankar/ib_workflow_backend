# -*- coding: utf-8 -*-
# snapshottest: v1 - https://goo.gl/zC4yUc
from __future__ import unicode_literals

from snapshottest import GenericRepr, Snapshot


snapshots = Snapshot()

snapshots['TestGetTaskDueMissingDetails.test_get_due_details_of_task_given_task_id due_details'] = [
    GenericRepr("TaskDueMissingDTO(task_id='iBWF-0', due_date_time=FakeDatetime(2020, 8, 14, 14, 58, 34, 344544), due_missed_count=1, reason='wrong estimation of time', user_id='123e4567-e89b-12d3-a456-426614174000')"),
    GenericRepr("TaskDueMissingDTO(task_id='iBWF-0', due_date_time=FakeDatetime(2020, 8, 14, 14, 58, 34, 344803), due_missed_count=1, reason='wrong estimation of time', user_id='123e4567-e89b-12d3-a456-426614174001')"),
    GenericRepr("TaskDueMissingDTO(task_id='iBWF-0', due_date_time=FakeDatetime(2020, 8, 14, 14, 58, 34, 345029), due_missed_count=1, reason='wrong estimation of time', user_id='123e4567-e89b-12d3-a456-426614174002')"),
    GenericRepr("TaskDueMissingDTO(task_id='iBWF-0', due_date_time=FakeDatetime(2020, 8, 14, 14, 58, 34, 345247), due_missed_count=1, reason='wrong estimation of time', user_id='123e4567-e89b-12d3-a456-426614174003')")
]

snapshots['TestGetTaskDueMissingDetails.test_get_due_details_of_task_when_task_has_no_delays due_details'] = [
]
