# -*- coding: utf-8 -*-
# snapshottest: v1 - https://goo.gl/zC4yUc
from __future__ import unicode_literals

from snapshottest import Snapshot


snapshots = Snapshot()

snapshots['TestCase02GetAllTasksOverviewAPITestCase.test_case status_code'] = '400'

snapshots['TestCase02GetAllTasksOverviewAPITestCase.test_case body'] = {
    'http_status_code': 400,
    'res_status': 'OFFSET_SHOULD_BE_GREATER_THAN_ZERO',
    'response': 'Offset value should be greater than zero'
}
