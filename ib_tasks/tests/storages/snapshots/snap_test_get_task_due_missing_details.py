# -*- coding: utf-8 -*-
# snapshottest: v1 - https://goo.gl/zC4yUc
from __future__ import unicode_literals

from snapshottest import GenericRepr, Snapshot


snapshots = Snapshot()

snapshots['TestGetTaskDueMissingDetails.test_get_due_details_of_task_given_task_id due_details'] = [
    GenericRepr("TaskDueMissingDTO(task_id=1, due_date_time=datetime.datetime(2020, 8, 11, 4, 22, 46, 875022, tzinfo=<UTC>), due_missed_count=1, reason='wrong estimation of time', user_id='user_id_0')"),
    GenericRepr("TaskDueMissingDTO(task_id=1, due_date_time=datetime.datetime(2020, 8, 11, 4, 22, 46, 875318, tzinfo=<UTC>), due_missed_count=1, reason='wrong estimation of time', user_id='user_id_1')"),
    GenericRepr("TaskDueMissingDTO(task_id=1, due_date_time=datetime.datetime(2020, 8, 11, 4, 22, 46, 875584, tzinfo=<UTC>), due_missed_count=1, reason='wrong estimation of time', user_id='user_id_2')"),
    GenericRepr("TaskDueMissingDTO(task_id=1, due_date_time=datetime.datetime(2020, 8, 11, 4, 22, 46, 875918, tzinfo=<UTC>), due_missed_count=1, reason='wrong estimation of time', user_id='user_id_3')")
]

snapshots['TestGetTaskDueMissingDetails.test_get_due_details_of_task_when_task_has_no_delays due_details'] = [
]
