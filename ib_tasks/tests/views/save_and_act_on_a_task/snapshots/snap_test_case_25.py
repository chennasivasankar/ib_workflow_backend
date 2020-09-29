# -*- coding: utf-8 -*-
# snapshottest: v1 - https://goo.gl/zC4yUc
from __future__ import unicode_literals

from snapshottest import Snapshot


snapshots = Snapshot()

snapshots['TestCase25SaveAndActOnATaskAPITestCase.test_case[strong_password] status_code'] = '400'

snapshots['TestCase25SaveAndActOnATaskAPITestCase.test_case[strong_password] body'] = {
    'http_status_code': 400,
    'res_status': 'NOT_A_STRONG_PASSWORD',
    'response': 'Given a weak password: strong_password for field: DISPLAY_NAME-0! Try with at least 6 characters including special characters'
}

snapshots['TestCase25SaveAndActOnATaskAPITestCase.test_case[password123] status_code'] = '400'

snapshots['TestCase25SaveAndActOnATaskAPITestCase.test_case[password123] body'] = {
    'http_status_code': 400,
    'res_status': 'NOT_A_STRONG_PASSWORD',
    'response': 'Given a weak password: password123 for field: DISPLAY_NAME-0! Try with at least 6 characters including special characters'
}

snapshots['TestCase25SaveAndActOnATaskAPITestCase.test_case[#2pass=] status_code'] = '400'

snapshots['TestCase25SaveAndActOnATaskAPITestCase.test_case[#2pass=] body'] = {
    'http_status_code': 400,
    'res_status': 'NOT_A_STRONG_PASSWORD',
    'response': 'Given a weak password: #2pass= for field: DISPLAY_NAME-0! Try with at least 6 characters including special characters'
}
