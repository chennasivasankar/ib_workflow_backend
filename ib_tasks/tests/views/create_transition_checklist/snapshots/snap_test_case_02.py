# -*- coding: utf-8 -*-
# snapshottest: v1 - https://goo.gl/zC4yUc
from __future__ import unicode_literals

from snapshottest import Snapshot


snapshots = Snapshot()

snapshots['TestCase02CreateTransitionChecklistAPITestCase.test_case status_code'] = '400'

snapshots['TestCase02CreateTransitionChecklistAPITestCase.test_case body'] = {
    'http_status_code': 400,
    'res_status': 'INVALID_TASK_ID',
    'response': 'IBWF-200 is invalid task_id send valid task_id'
}
