# -*- coding: utf-8 -*-
# snapshottest: v1 - https://goo.gl/zC4yUc
from __future__ import unicode_literals

from snapshottest import Snapshot


snapshots = Snapshot()

snapshots['TestCase16CreateTaskAPITestCase.test_case status_code'] = '400'

snapshots['TestCase16CreateTaskAPITestCase.test_case body'] = {
    'http_status_code': 400,
    'res_status': 'EMPTY_VALUE_FOR_REQUIRED_FIELD',
    'response': 'Given Empty value for the required field of field_id: FIELD_ID-0! Required field should not be empty'
}
