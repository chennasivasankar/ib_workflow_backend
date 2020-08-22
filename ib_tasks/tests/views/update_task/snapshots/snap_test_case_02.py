# -*- coding: utf-8 -*-
# snapshottest: v1 - https://goo.gl/zC4yUc
from __future__ import unicode_literals

from snapshottest import Snapshot


snapshots = Snapshot()

snapshots['TestCase01UpdateTaskAPITestCase.test_case status_code'] = '400'

snapshots['TestCase01UpdateTaskAPITestCase.test_case body'] = {
    'http_status_code': 400,
    'res_status': 'INVALID_DUE_TIME_FORMAT',
    'response': '12-00-00 has invalid due time format, time format should be HH:MM:SS'
}

snapshots['TestCase02UpdateTaskAPITestCase.test_case status_code'] = '400'

snapshots['TestCase02UpdateTaskAPITestCase.test_case body'] = {
    'http_status_code': 400,
    'res_status': 'INVALID_DUE_TIME_FORMAT',
    'response': '12-00-00 has invalid due time format, time format should be HH:MM:SS'
}
