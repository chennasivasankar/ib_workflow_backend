# -*- coding: utf-8 -*-
# snapshottest: v1 - https://goo.gl/zC4yUc
from __future__ import unicode_literals

from snapshottest import Snapshot


snapshots = Snapshot()

snapshots['TestCase02GetTimerAPITestCase.test_case status_code'] = '200'

snapshots['TestCase02GetTimerAPITestCase.test_case body'] = {
    'duration_in_seconds': 3700,
    'is_running': True
}
