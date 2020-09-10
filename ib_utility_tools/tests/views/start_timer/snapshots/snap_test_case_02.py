# -*- coding: utf-8 -*-
# snapshottest: v1 - https://goo.gl/zC4yUc
from __future__ import unicode_literals

from snapshottest import Snapshot


snapshots = Snapshot()

snapshots['TestCase02StartTimerAPITestCase.test_case status_code'] = '400'

snapshots['TestCase02StartTimerAPITestCase.test_case body'] = {
    'http_status_code': 400,
    'res_status': 'TIMER_IS_ALREADY_RUNNING',
    'response': 'Timer is already running'
}
