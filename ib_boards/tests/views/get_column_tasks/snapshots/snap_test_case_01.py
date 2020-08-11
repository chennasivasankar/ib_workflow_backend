# -*- coding: utf-8 -*-
# snapshottest: v1 - https://goo.gl/zC4yUc
from __future__ import unicode_literals

from snapshottest import Snapshot


snapshots = Snapshot()

snapshots['TestCase01GetColumnTasksAPITestCase.test_case status_code'] = '404'

snapshots['TestCase01GetColumnTasksAPITestCase.test_case body'] = {
    'http_status_code': 404,
    'res_status': 'INVALID_COLUMN_ID',
    'response': 'column id is invalid'
}
