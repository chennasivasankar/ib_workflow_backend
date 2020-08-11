# -*- coding: utf-8 -*-
# snapshottest: v1 - https://goo.gl/zC4yUc
from __future__ import unicode_literals

from snapshottest import Snapshot


snapshots = Snapshot()

snapshots['TestCase01GetReasonsForMissingTaskDueDateTimeAPITestCase.test_case status_code'] = '404'

snapshots['TestCase01GetReasonsForMissingTaskDueDateTimeAPITestCase.test_case body'] = {
    'http_status_code': 404,
    'res_status': 'INVALID_TASK_ID',
    'response': 'invalid task id is: 1, please send valid task id'
}
