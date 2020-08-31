# -*- coding: utf-8 -*-
# snapshottest: v1 - https://goo.gl/zC4yUc
from __future__ import unicode_literals

from snapshottest import GenericRepr, Snapshot


snapshots = Snapshot()

snapshots['TestAddDueDelayDetails.test_add_due_delay_details_given_details task_due_datetime'] = GenericRepr("<CommonCustomQuerySet [{'id': 1, 'tasklog__user_id': '123e4567-e89b-12d3-a456-426614174000', 'due_date': FakeDatetime(2020, 8, 10, 12, 30)}]>")

snapshots['TestAddDueDelayDetails.test_update_task_due_datetime_given_details task_due_datetime'] = GenericRepr("<CommonCustomQuerySet [{'id': 1, 'tasklog__user_id': '123e4567-e89b-12d3-a456-426614174000', 'due_date': FakeDatetime(2020, 8, 10, 12, 30)}]>")
