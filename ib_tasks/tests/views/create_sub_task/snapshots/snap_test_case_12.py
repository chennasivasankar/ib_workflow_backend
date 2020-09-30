# -*- coding: utf-8 -*-
# snapshottest: v1 - https://goo.gl/zC4yUc
from __future__ import unicode_literals

from snapshottest import Snapshot


snapshots = Snapshot()

snapshots['TestCase12CreateSubTaskAPITestCase.test_case status_code'] = '400'

snapshots['TestCase12CreateSubTaskAPITestCase.test_case body'] = {
    'http_status_code': 400,
    'res_status': 'DUE_DATE_TIME_HAS_EXPIRED',
    'response': 'given due date time 2020-08-19 12:00:00 has expired, please give a valid due date time'
}
