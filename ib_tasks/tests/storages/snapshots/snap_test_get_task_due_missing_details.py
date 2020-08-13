# -*- coding: utf-8 -*-
# snapshottest: v1 - https://goo.gl/zC4yUc
from __future__ import unicode_literals

from snapshottest import GenericRepr, Snapshot


snapshots = Snapshot()

snapshots['TestGetTaskDueMissingDetails.test_get_due_details_of_task_given_task_id due_details'] = [
    GenericRepr("TaskDueMissingDTO(task_id=1, due_date_time=FakeDatetime(2020, 8, 11, 5, 57, 36, 329726, tzinfo=<UTC>), due_missed_count=1, reason='wrong estimation of time', user_id='user_id_0')"),
    GenericRepr("TaskDueMissingDTO(task_id=1, due_date_time=FakeDatetime(2020, 8, 11, 5, 57, 36, 329978, tzinfo=<UTC>), due_missed_count=1, reason='wrong estimation of time', user_id='user_id_1')"),
    GenericRepr("TaskDueMissingDTO(task_id=1, due_date_time=FakeDatetime(2020, 8, 11, 5, 57, 36, 330209, tzinfo=<UTC>), due_missed_count=1, reason='wrong estimation of time', user_id='user_id_2')"),
    GenericRepr("TaskDueMissingDTO(task_id=1, due_date_time=FakeDatetime(2020, 8, 11, 5, 57, 36, 330463, tzinfo=<UTC>), due_missed_count=1, reason='wrong estimation of time', user_id='user_id_3')")
]

snapshots['TestGetTaskDueMissingDetails.test_get_due_details_of_task_when_task_has_no_delays due_details'] = [
]
