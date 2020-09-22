# -*- coding: utf-8 -*-
# snapshottest: v1 - https://goo.gl/zC4yUc
from __future__ import unicode_literals

from snapshottest import Snapshot


snapshots = Snapshot()

snapshots['TestCase12SaveAndActOnATaskAPITestCase.test_case status_code'] = '400'

snapshots['TestCase12SaveAndActOnATaskAPITestCase.test_case body'] = {
    'http_status_code': 400,
    'res_status': 'TASK_DELAY_REASON_NOT_UPDATED',
    'response': 'you are trying to update task due date to 2020-09-20 12:00:00 without updating the delay reason for task IBWF-1 in stage display_name_0'
}
