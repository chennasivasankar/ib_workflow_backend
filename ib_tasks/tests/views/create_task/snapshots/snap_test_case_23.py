# -*- coding: utf-8 -*-
# snapshottest: v1 - https://goo.gl/zC4yUc
from __future__ import unicode_literals

from snapshottest import Snapshot


snapshots = Snapshot()

snapshots['TestCase23CreateTaskAPITestCase.test_case status_code'] = '400'

snapshots['TestCase23CreateTaskAPITestCase.test_case body'] = {
    'http_status_code': 400,
    'res_status': 'INVALID_VALUE_FOR_DROPDOWN',
    'response': "Invalid dropdown value: Other for field: FIELD_ID-0! Try with these dropdown values: ['Mr', 'Mrs']"
}
