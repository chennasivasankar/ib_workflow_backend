# -*- coding: utf-8 -*-
# snapshottest: v1 - https://goo.gl/zC4yUc
from __future__ import unicode_literals

from snapshottest import Snapshot


snapshots = Snapshot()

snapshots['TestCase04AddReasonForMissingDueDateTimeAPITestCase.test_case status_code'] = '400'

snapshots['TestCase04AddReasonForMissingDueDateTimeAPITestCase.test_case body'] = {
    'http_status_code': 400,
    'res_status': 'INVALID_DUE_DATE_TIME',
    'response': 'given updated due datetime is invalid'
}
