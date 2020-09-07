# -*- coding: utf-8 -*-
# snapshottest: v1 - https://goo.gl/zC4yUc
from __future__ import unicode_literals

from snapshottest import Snapshot, GenericRepr


snapshots = Snapshot()

snapshots['TestUpdateTaskDueDateTime.test_update_task_due_datetime_given_details task_id_1'] = 1

snapshots['TestUpdateTaskDueDateTime.test_update_task_due_datetime_given_details task_log_user_id_1'] = '123e4567-e89b-12d3-a456-426614174000'

snapshots['TestUpdateTaskDueDateTime.test_update_task_due_datetime_given_details due_date_1'] = GenericRepr("FakeDatetime(2020, 8, 10, 12, 30)")
