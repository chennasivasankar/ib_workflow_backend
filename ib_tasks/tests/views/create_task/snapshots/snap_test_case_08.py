# -*- coding: utf-8 -*-
# snapshottest: v1 - https://goo.gl/zC4yUc
from __future__ import unicode_literals

from snapshottest import Snapshot


snapshots = Snapshot()

snapshots['TestCase08CreateTaskAPITestCase.test_case status_code'] = '400'

snapshots['TestCase08CreateTaskAPITestCase.test_case body'] = {
    'http_status_code': 400,
    'res_status': 'INVALID_DUE_TIME_FORMAT',
    'response': '55:00:00 has invalid due time format, time format should be HH:MM:SS'
}
