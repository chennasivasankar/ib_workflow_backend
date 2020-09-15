# -*- coding: utf-8 -*-
# snapshottest: v1 - https://goo.gl/zC4yUc
from __future__ import unicode_literals

from snapshottest import Snapshot


snapshots = Snapshot()

snapshots['TestCase35UpdateTaskAPITestCase.test_case status_code'] = '400'

snapshots['TestCase35UpdateTaskAPITestCase.test_case body'] = {
    'http_status_code': 400,
    'res_status': 'INVALID_TIME_FORMAT',
    'response': 'given invalid format for time: 20:70:00 for field: FIELD-1! Try with this format: %H:%M:%S'
}
