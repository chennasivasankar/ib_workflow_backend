# -*- coding: utf-8 -*-
# snapshottest: v1 - https://goo.gl/zC4yUc
from __future__ import unicode_literals

from snapshottest import Snapshot


snapshots = Snapshot()

snapshots['TestCase20CreateTransitionChecklistAPITestCase.test_case[iBHubs] status_code'] = '400'

snapshots['TestCase20CreateTransitionChecklistAPITestCase.test_case[iBHubs] body'] = {
    'http_status_code': 400,
    'res_status': 'NOT_A_STRONG_PASSWORD',
    'response': 'Given a weak password: iBHubs for field: field_1! Try with at least 6 characters including special characters'
}

snapshots['TestCase20CreateTransitionChecklistAPITestCase.test_case[@priB] status_code'] = '400'

snapshots['TestCase20CreateTransitionChecklistAPITestCase.test_case[@priB] body'] = {
    'http_status_code': 400,
    'res_status': 'NOT_A_STRONG_PASSWORD',
    'response': 'Given a weak password: @priB for field: field_1! Try with at least 6 characters including special characters'
}
