# -*- coding: utf-8 -*-
# snapshottest: v1 - https://goo.gl/zC4yUc
from __future__ import unicode_literals

from snapshottest import Snapshot


snapshots = Snapshot()

snapshots['TestCase01PerformTaskActionAPITestCase.test_case status_code'] = '500'

snapshots['TestCase01PerformTaskActionAPITestCase.test_case body'] = {
    'res_status': [
        '"INVALID_PRESENT_STAGE_ACTION" is not a valid choice.'
    ]
}
