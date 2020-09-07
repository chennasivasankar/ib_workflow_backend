# -*- coding: utf-8 -*-
# snapshottest: v1 - https://goo.gl/zC4yUc
from __future__ import unicode_literals

from snapshottest import Snapshot


snapshots = Snapshot()

snapshots['TestCase38UpdateTaskAPITestCase.test_case status_code'] = '400'

snapshots['TestCase38UpdateTaskAPITestCase.test_case body'] = {
    'http_status_code': 400,
    'res_status': 'TASK_DELAY_REASON_NOT_UPDATED',
    'response': 'Task delay reason not updated for task IBWF-1 in stage display_name_0 with missed due date 2020-09-09 11:00:00'
}
