# -*- coding: utf-8 -*-
# snapshottest: v1 - https://goo.gl/zC4yUc
from __future__ import unicode_literals

from snapshottest import Snapshot


snapshots = Snapshot()

snapshots['TestCase36CreateSubTaskAPITestCase.test_case status_code'] = '400'

snapshots['TestCase36CreateSubTaskAPITestCase.test_case body'] = {
    'http_status_code': 400,
    'res_status': 'INVALID_DATE_FORMAT',
    'response': 'given invalid format for date: 2020-15-09 for field: DISPLAY_NAME-0! Try with this format: %Y-%m-%d'
}
