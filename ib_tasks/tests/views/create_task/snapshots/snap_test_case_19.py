# -*- coding: utf-8 -*-
# snapshottest: v1 - https://goo.gl/zC4yUc
from __future__ import unicode_literals

from snapshottest import Snapshot


snapshots = Snapshot()

snapshots['TestCase19CreateTaskAPITestCase.test_case[www.google.@com] status_code'] = '400'

snapshots['TestCase19CreateTaskAPITestCase.test_case[www.google.@com] body'] = {
    'http_status_code': 400,
    'res_status': 'INVALID_EMAIL',
    'response': 'Invalid value for email: www.google.@com for field: FIELD_ID-0'
}

snapshots['TestCase19CreateTaskAPITestCase.test_case[http://google] status_code'] = '400'

snapshots['TestCase19CreateTaskAPITestCase.test_case[http://google] body'] = {
    'http_status_code': 400,
    'res_status': 'INVALID_EMAIL',
    'response': 'Invalid value for email: http://google for field: FIELD_ID-0'
}
