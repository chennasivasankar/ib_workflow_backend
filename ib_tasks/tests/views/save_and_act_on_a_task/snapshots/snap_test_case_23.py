# -*- coding: utf-8 -*-
# snapshottest: v1 - https://goo.gl/zC4yUc
from __future__ import unicode_literals

from snapshottest import Snapshot


snapshots = Snapshot()

snapshots['TestCase23SaveAndActOnATaskAPITestCase.test_case status_code'] = '400'

snapshots['TestCase23SaveAndActOnATaskAPITestCase.test_case body'] = {
    'http_status_code': 400,
    'res_status': 'INVALID_PHONE_NUMBER_VALUE',
    'response': 'Invalid value for phone number: phone number for field: FIELD_ID-1'
}
