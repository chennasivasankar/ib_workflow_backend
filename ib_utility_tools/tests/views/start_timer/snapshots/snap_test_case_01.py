# -*- coding: utf-8 -*-
# snapshottest: v1 - https://goo.gl/zC4yUc
from __future__ import unicode_literals

from snapshottest import Snapshot


snapshots = Snapshot()

snapshots['TestCase01StartTimerAPITestCase.test_case status_code'] = '200'

snapshots['TestCase01StartTimerAPITestCase.test_case body'] = {
    'duration_in_seconds': 0,
    'is_running': True
}

snapshots['TestCase01StartTimerAPITestCase.test_case start_datetime'] = '08/07/2020, 18:00:00'
