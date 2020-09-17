# -*- coding: utf-8 -*-
# snapshottest: v1 - https://goo.gl/zC4yUc
from __future__ import unicode_literals

from snapshottest import Snapshot


snapshots = Snapshot()

snapshots['TestCase05UpdateTaskAPITestCase.test_case status_code'] = '400'

snapshots['TestCase05UpdateTaskAPITestCase.test_case body'] = {
    'http_status_code': 400,
    'res_status': 'START_DATE_IS_AHEAD_OF_DUE_DATE',
    'response': 'given start date 2020-09-20 00:00:00 is ahead of given due date 2020-08-20 00:00:00 '
}
