# -*- coding: utf-8 -*-
# snapshottest: v1 - https://goo.gl/zC4yUc
from __future__ import unicode_literals

from snapshottest import Snapshot


snapshots = Snapshot()

snapshots['TestCase27SaveAndActOnATaskAPITestCase.test_case[float.3] status_code'] = '400'

snapshots['TestCase27SaveAndActOnATaskAPITestCase.test_case[float.3] body'] = {
    'http_status_code': 400,
    'res_status': 'INVALID_FLOAT_VALUE',
    'response': 'Invalid float value: float.3 for field: FIELD_ID-1!'
}

snapshots['TestCase27SaveAndActOnATaskAPITestCase.test_case[one.two] status_code'] = '400'

snapshots['TestCase27SaveAndActOnATaskAPITestCase.test_case[one.two] body'] = {
    'http_status_code': 400,
    'res_status': 'INVALID_FLOAT_VALUE',
    'response': 'Invalid float value: one.two for field: FIELD_ID-1!'
}
