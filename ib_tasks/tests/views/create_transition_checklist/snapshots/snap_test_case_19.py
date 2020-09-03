# -*- coding: utf-8 -*-
# snapshottest: v1 - https://goo.gl/zC4yUc
from __future__ import unicode_literals

from snapshottest import Snapshot


snapshots = Snapshot()

snapshots['TestCase19CreateTransitionChecklistAPITestCase.test_case[iBHubs] status_code'] = '400'

snapshots['TestCase19CreateTransitionChecklistAPITestCase.test_case[iBHubs] body'] = {
    'http_status_code': 400,
    'res_status': 'INVALID_FLOAT_VALUE',
    'response': 'Invalid float value: iBHubs for field: field_1!'
}

snapshots['TestCase19CreateTransitionChecklistAPITestCase.test_case[700.0iB] status_code'] = '400'

snapshots['TestCase19CreateTransitionChecklistAPITestCase.test_case[700.0iB] body'] = {
    'http_status_code': 400,
    'res_status': 'INVALID_FLOAT_VALUE',
    'response': 'Invalid float value: 700.0iB for field: field_1!'
}
