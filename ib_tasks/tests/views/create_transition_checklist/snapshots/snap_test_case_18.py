# -*- coding: utf-8 -*-
# snapshottest: v1 - https://goo.gl/zC4yUc
from __future__ import unicode_literals

from snapshottest import Snapshot


snapshots = Snapshot()

snapshots['TestCase18CreateTransitionChecklistAPITestCase.test_case[iBHubs] status_code'] = '400'

snapshots['TestCase18CreateTransitionChecklistAPITestCase.test_case[iBHubs] body'] = {
    'http_status_code': 400,
    'res_status': 'INVALID_NUMBER_VALUE',
    'response': 'Invalid number: iBHubs for field: field_1! Number should only consists digits'
}

snapshots['TestCase18CreateTransitionChecklistAPITestCase.test_case[700.0] status_code'] = '400'

snapshots['TestCase18CreateTransitionChecklistAPITestCase.test_case[700.0] body'] = {
    'http_status_code': 400,
    'res_status': 'INVALID_NUMBER_VALUE',
    'response': 'Invalid number: 700.0 for field: field_1! Number should only consists digits'
}
