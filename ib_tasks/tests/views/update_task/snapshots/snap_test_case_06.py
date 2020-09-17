# -*- coding: utf-8 -*-
# snapshottest: v1 - https://goo.gl/zC4yUc
from __future__ import unicode_literals

from snapshottest import Snapshot


snapshots = Snapshot()

snapshots['TestCase06UpdateTaskAPITestCase.test_case status_code'] = '400'

snapshots['TestCase06UpdateTaskAPITestCase.test_case body'] = {
    'http_status_code': 400,
    'res_status': 'DUE_DATE_TIME_HAS_EXPIRED',
    'response': 'given due date time 2020-09-09 12:00:00 has expired, please give a valid due date time'
}
