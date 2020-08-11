# -*- coding: utf-8 -*-
# snapshottest: v1 - https://goo.gl/zC4yUc
from __future__ import unicode_literals

from snapshottest import GenericRepr, Snapshot


snapshots = Snapshot()

snapshots['TestAddDueDelayDetails.test_add_due_delay_details_given_details reason'] = GenericRepr("<QuerySet [{'id': 1, 'task_id': 1, 'due_datetime': FakeDatetime(2020, 8, 10, 12, 30, tzinfo=<UTC>), 'count': 1, 'reason_id': 1, 'reason': 'reason', 'user_id': '123e4567-e89b-12d3-a456-426614174000'}]>")
