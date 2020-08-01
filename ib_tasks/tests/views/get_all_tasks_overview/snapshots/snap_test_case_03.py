# -*- coding: utf-8 -*-
# snapshottest: v1 - https://goo.gl/zC4yUc
from __future__ import unicode_literals

from snapshottest import Snapshot


snapshots = Snapshot()

snapshots['TestCase03GetAllTasksOverviewAPITestCase.test_case status_code'] = '400'

snapshots['TestCase03GetAllTasksOverviewAPITestCase.test_case body'] = {
    'http_status_code': 400,
    'res_status': 'EMPTY_STAGE_IDS_ARE_INVALID',
    'response': 'Stage Ids list should not be empty'
}
