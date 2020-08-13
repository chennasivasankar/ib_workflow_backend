# -*- coding: utf-8 -*-
# snapshottest: v1 - https://goo.gl/zC4yUc
from __future__ import unicode_literals

from snapshottest import Snapshot


snapshots = Snapshot()

snapshots['TestCase01CreateTaskAPITestCase.test_case status_code'] = '400'

snapshots['TestCase01CreateTaskAPITestCase.test_case body'] = {
    'http_status_code': 400,
    'res_status': 'START_DATE_IS_AHEAD_OF_DUE_DATE',
    'response': 'given start date 2099-12-31 is ahead of given due date 2019-12-31 '
}
