# -*- coding: utf-8 -*-
# snapshottest: v1 - https://goo.gl/zC4yUc
from __future__ import unicode_literals

from snapshottest import GenericRepr, Snapshot


snapshots = Snapshot()

snapshots['TestCase01StartTimerAPITestCase.test_case status_code'] = '200'

snapshots['TestCase01StartTimerAPITestCase.test_case body'] = {
    'duration_in_seconds': 0,
    'is_running': True
}

snapshots['TestCase01StartTimerAPITestCase.test_case start_datetime'] = GenericRepr("FakeDatetime(2020, 8, 7, 18, 0)")
