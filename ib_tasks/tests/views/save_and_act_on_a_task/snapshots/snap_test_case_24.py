# -*- coding: utf-8 -*-
# snapshottest: v1 - https://goo.gl/zC4yUc
from __future__ import unicode_literals

from snapshottest import Snapshot


snapshots = Snapshot()

snapshots['TestCase24SaveAndActOnATaskAPITestCase.test_case[email.com] status_code'] = '400'

snapshots['TestCase24SaveAndActOnATaskAPITestCase.test_case[email.com] body'] = {
    'http_status_code': 400,
    'res_status': 'INVALID_EMAIL',
    'response': 'Invalid value for email: email.com for field: FIELD_ID-1'
}

snapshots['TestCase24SaveAndActOnATaskAPITestCase.test_case[email@gmail] status_code'] = '400'

snapshots['TestCase24SaveAndActOnATaskAPITestCase.test_case[email@gmail] body'] = {
    'http_status_code': 400,
    'res_status': 'INVALID_EMAIL',
    'response': 'Invalid value for email: email@gmail for field: FIELD_ID-1'
}

snapshots['TestCase24SaveAndActOnATaskAPITestCase.test_case[@.com] status_code'] = '400'

snapshots['TestCase24SaveAndActOnATaskAPITestCase.test_case[@.com] body'] = {
    'http_status_code': 400,
    'res_status': 'INVALID_EMAIL',
    'response': 'Invalid value for email: @.com for field: FIELD_ID-1'
}
