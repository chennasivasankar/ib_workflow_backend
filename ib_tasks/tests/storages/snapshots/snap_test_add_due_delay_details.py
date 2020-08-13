# -*- coding: utf-8 -*-
# snapshottest: v1 - https://goo.gl/zC4yUc
from __future__ import unicode_literals

from snapshottest import GenericRepr, Snapshot


snapshots = Snapshot()

snapshots['TestAddDueDelayDetails.test_add_due_delay_details_given_details reason'] = GenericRepr("<QuerySet [{'id': 1, 'task_id': 1, 'due_datetime': FakeDatetime(2020, 8, 13, 12, 16, 31, 420200), 'count': 1, 'reason_id': 1, 'reason': 'wrong estimation of time', 'user_id': '123e4567-e89b-12d3-a456-426614174000'}, {'id': 4, 'task_id': 1, 'due_datetime': FakeDatetime(2020, 8, 10, 12, 30), 'count': 2, 'reason_id': 1, 'reason': 'reason', 'user_id': '123e4567-e89b-12d3-a456-426614174000'}]>")

snapshots['TestAddDueDelayDetails.test_add_due_delay_details_given_details task_due_datetime'] = GenericRepr("<CommonCustomQuerySet [{'id': 1, 'tasklog__user_id': '123e4567-e89b-12d3-a456-426614174000', 'due_date': datetime.datetime(2020, 8, 10, 12, 30)}]>")
