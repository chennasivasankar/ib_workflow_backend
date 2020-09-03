# -*- coding: utf-8 -*-
# snapshottest: v1 - https://goo.gl/zC4yUc
from __future__ import unicode_literals

from snapshottest import Snapshot


snapshots = Snapshot()

snapshots['TestCase18CreateTaskAPITestCase.test_case[www.google.com] status_code'] = '400'

snapshots['TestCase18CreateTaskAPITestCase.test_case[www.google.com] body'] = {
    'http_status_code': 400,
    'res_status': 'INVALID_URL',
    'response': 'Invalid value for url: www.google.com for field: FIELD_ID-0'
}

snapshots['TestCase18CreateTaskAPITestCase.test_case[http://google] status_code'] = '400'

snapshots['TestCase18CreateTaskAPITestCase.test_case[http://google] body'] = {
    'http_status_code': 400,
    'res_status': 'INVALID_URL',
    'response': 'Invalid value for url: http://google for field: FIELD_ID-0'
}
