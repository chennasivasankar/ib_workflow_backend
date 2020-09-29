# -*- coding: utf-8 -*-
# snapshottest: v1 - https://goo.gl/zC4yUc
from __future__ import unicode_literals

from snapshottest import Snapshot


snapshots = Snapshot()

snapshots['TestCase11CreateSubTaskAPITestCase.test_case status_code'] = '400'

snapshots['TestCase11CreateSubTaskAPITestCase.test_case body'] = {
    'http_status_code': 400,
    'res_status': 'DUE_DATE_TIME_WITHOUT_START_DATE_TIME',
    'response': 'due date time 2020-09-09 12:00:00 is given with out start datetime'
}
