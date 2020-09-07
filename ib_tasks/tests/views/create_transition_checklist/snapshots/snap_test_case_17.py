# -*- coding: utf-8 -*-
# snapshottest: v1 - https://goo.gl/zC4yUc
from __future__ import unicode_literals

from snapshottest import Snapshot


snapshots = Snapshot()

snapshots['TestCase17CreateTransitionChecklistAPITestCase.test_case[rajesh@ibhubs@.com] status_code'] = '400'

snapshots['TestCase17CreateTransitionChecklistAPITestCase.test_case[rajesh@ibhubs@.com] body'] = {
    'http_status_code': 400,
    'res_status': 'INVALID_EMAIL',
    'response': 'Invalid value for email: rajesh@ibhubs@.com for field: field_1'
}

snapshots['TestCase17CreateTransitionChecklistAPITestCase.test_case[.kumar@gmail@com] status_code'] = '400'

snapshots['TestCase17CreateTransitionChecklistAPITestCase.test_case[.kumar@gmail@com] body'] = {
    'http_status_code': 400,
    'res_status': 'INVALID_EMAIL',
    'response': 'Invalid value for email: .kumar@gmail@com for field: field_1'
}
