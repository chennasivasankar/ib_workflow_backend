# -*- coding: utf-8 -*-
# snapshottest: v1 - https://goo.gl/zC4yUc
from __future__ import unicode_literals

from snapshottest import Snapshot


snapshots = Snapshot()

snapshots['TestCase07SaveAndActOnATaskAPITestCase.test_case status_code'] = '400'

snapshots['TestCase07SaveAndActOnATaskAPITestCase.test_case body'] = {
    'http_status_code': 400,
    'res_status': 'START_DATE_TIME_IS_REQUIRED',
    'response': 'start datetime is required if action type is not no validations'
}
