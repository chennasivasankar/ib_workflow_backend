# -*- coding: utf-8 -*-
# snapshottest: v1 - https://goo.gl/zC4yUc
from __future__ import unicode_literals

from snapshottest import Snapshot


snapshots = Snapshot()

snapshots['TestCase01UpdateTaskAPITestCase.test_case status_code'] = '400'

snapshots['TestCase01UpdateTaskAPITestCase.test_case body'] = {
    'http_status_code': 400,
    'res_status': 'DUE_DATE_HAS_EXPIRED',
    'response': 'given due date 2020-08-02 has expired'
}

snapshots['TestCase03UpdateTaskAPITestCase.test_case status_code'] = '400'

snapshots['TestCase03UpdateTaskAPITestCase.test_case body'] = {
    'http_status_code': 400,
    'res_status': 'DUE_DATE_HAS_EXPIRED',
    'response': 'given due date 2020-08-02 has expired'
}
