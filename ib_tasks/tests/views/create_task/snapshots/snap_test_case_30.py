# -*- coding: utf-8 -*-
# snapshottest: v1 - https://goo.gl/zC4yUc
from __future__ import unicode_literals

from snapshottest import Snapshot


snapshots = Snapshot()

snapshots['TestCase30CreateTaskAPITestCase.test_case status_code'] = '400'

snapshots['TestCase30CreateTaskAPITestCase.test_case body'] = {
    'http_status_code': 400,
    'res_status': 'INVALID_TIME_FORMAT',
    'response': 'given invalid format for time: 31:00:00 for field: FIELD_ID-0! Try with this format: %H:%M:%S'
}
