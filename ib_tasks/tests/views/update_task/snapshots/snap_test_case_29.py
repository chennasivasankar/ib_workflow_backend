# -*- coding: utf-8 -*-
# snapshottest: v1 - https://goo.gl/zC4yUc
from __future__ import unicode_literals

from snapshottest import Snapshot


snapshots = Snapshot()

snapshots['TestCase29UpdateTaskAPITestCase.test_case status_code'] = '400'

snapshots['TestCase29UpdateTaskAPITestCase.test_case body'] = {
    'http_status_code': 400,
    'res_status': 'INVALID_DATE_FORMAT',
    'response': 'given invalid format for date: 9-9-2020 for field: FIELD-1! Try with this format: %Y-%m-%d'
}
