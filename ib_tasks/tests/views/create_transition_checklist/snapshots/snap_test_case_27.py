# -*- coding: utf-8 -*-
# snapshottest: v1 - https://goo.gl/zC4yUc
from __future__ import unicode_literals

from snapshottest import Snapshot


snapshots = Snapshot()

snapshots['TestCase27CreateTransitionChecklistAPITestCase.test_case[31-2099-12] status_code'] = '400'

snapshots['TestCase27CreateTransitionChecklistAPITestCase.test_case[31-2099-12] body'] = {
    'http_status_code': 400,
    'res_status': 'INVALID_DATE_FORMAT',
    'response': 'given invalid format for date: 31-2099-12 for field: field_1! Try with this format: %Y-%m-%d'
}

snapshots['TestCase27CreateTransitionChecklistAPITestCase.test_case[2099-31-12] status_code'] = '400'

snapshots['TestCase27CreateTransitionChecklistAPITestCase.test_case[2099-31-12] body'] = {
    'http_status_code': 400,
    'res_status': 'INVALID_DATE_FORMAT',
    'response': 'given invalid format for date: 2099-31-12 for field: field_1! Try with this format: %Y-%m-%d'
}

snapshots['TestCase27CreateTransitionChecklistAPITestCase.test_case[31-12-2099] status_code'] = '400'

snapshots['TestCase27CreateTransitionChecklistAPITestCase.test_case[31-12-2099] body'] = {
    'http_status_code': 400,
    'res_status': 'INVALID_DATE_FORMAT',
    'response': 'given invalid format for date: 31-12-2099 for field: field_1! Try with this format: %Y-%m-%d'
}

snapshots['TestCase27CreateTransitionChecklistAPITestCase.test_case[12-31-2099] status_code'] = '400'

snapshots['TestCase27CreateTransitionChecklistAPITestCase.test_case[12-31-2099] body'] = {
    'http_status_code': 400,
    'res_status': 'INVALID_DATE_FORMAT',
    'response': 'given invalid format for date: 12-31-2099 for field: field_1! Try with this format: %Y-%m-%d'
}
