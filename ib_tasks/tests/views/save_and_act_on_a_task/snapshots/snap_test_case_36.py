# -*- coding: utf-8 -*-
# snapshottest: v1 - https://goo.gl/zC4yUc
from __future__ import unicode_literals

from snapshottest import Snapshot


snapshots = Snapshot()

snapshots['TestCase36SaveAndActOnATaskAPITestCase.test_case status_code'] = '400'

snapshots['TestCase36SaveAndActOnATaskAPITestCase.test_case body'] = {
    'http_status_code': 400,
    'res_status': 'INVALID_TIME_FORMAT',
    'response': 'given invalid format for time: 24:00:00 for field: FIELD_ID-1! Try with this format: %H:%M:%S'
}
