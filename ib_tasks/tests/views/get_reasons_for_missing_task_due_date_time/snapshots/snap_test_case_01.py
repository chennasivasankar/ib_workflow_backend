# -*- coding: utf-8 -*-
# snapshottest: v1 - https://goo.gl/zC4yUc
from __future__ import unicode_literals

from snapshottest import Snapshot


snapshots = Snapshot()

snapshots['TestCase01GetReasonsForMissingTaskDueDateTimeAPITestCase.test_case status_code'] = '200'

snapshots['TestCase01GetReasonsForMissingTaskDueDateTimeAPITestCase.test_case body'] = [
    {
        'due_date_time': '2099-12-31 00:00:00',
        'due_missed_count': 1,
        'task_id': 1,
        'user': {
            'name': 'string',
            'profile_pic': 'string',
            'user_id': 'string'
        }
    }
]
