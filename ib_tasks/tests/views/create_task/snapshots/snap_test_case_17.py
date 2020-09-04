# -*- coding: utf-8 -*-
# snapshottest: v1 - https://goo.gl/zC4yUc
from __future__ import unicode_literals

from snapshottest import Snapshot


snapshots = Snapshot()

snapshots['TestCase17CreateTaskAPITestCase.test_case[879389jkh2] status_code'] = '400'

snapshots['TestCase17CreateTaskAPITestCase.test_case[879389jkh2] body'] = {
    'http_status_code': 400,
    'res_status': 'INVALID_PHONE_NUMBER_VALUE',
    'response': 'Invalid value for phone number: 879389jkh2 for field: FIELD_ID-0'
}

snapshots['TestCase17CreateTaskAPITestCase.test_case[34567892] status_code'] = '400'

snapshots['TestCase17CreateTaskAPITestCase.test_case[34567892] body'] = {
    'http_status_code': 400,
    'res_status': 'INVALID_PHONE_NUMBER_VALUE',
    'response': 'Invalid value for phone number: 34567892 for field: FIELD_ID-0'
}
