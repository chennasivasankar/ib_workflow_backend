# -*- coding: utf-8 -*-
# snapshottest: v1 - https://goo.gl/zC4yUc
from __future__ import unicode_literals

from snapshottest import Snapshot


snapshots = Snapshot()

snapshots['TestCase10GetTaskAPITestCase.test_case status_code'] = '404'

snapshots['TestCase10GetTaskAPITestCase.test_case body'] = {
    'http_status_code': 404,
    'res_status': 'INVALID_PROJECT_ID',
    'response': 'project0 is invalid project id, please send valid project id'
}
