# -*- coding: utf-8 -*-
# snapshottest: v1 - https://goo.gl/zC4yUc
from __future__ import unicode_literals

from snapshottest import Snapshot


snapshots = Snapshot()

snapshots['TestCase22CreateTaskAPITestCase.test_case[iB] status_code'] = '400'

snapshots['TestCase22CreateTaskAPITestCase.test_case[iB] body'] = {
    'http_status_code': 400,
    'res_status': 'INVALID_FLOAT_VALUE',
    'response': 'Invalid float value: iB for field: FIELD_ID-0!'
}

snapshots['TestCase22CreateTaskAPITestCase.test_case[500_iB] status_code'] = '400'

snapshots['TestCase22CreateTaskAPITestCase.test_case[500_iB] body'] = {
    'http_status_code': 400,
    'res_status': 'INVALID_FLOAT_VALUE',
    'response': 'Invalid float value: 500_iB for field: FIELD_ID-0!'
}
