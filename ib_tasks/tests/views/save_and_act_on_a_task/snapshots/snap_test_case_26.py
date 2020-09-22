# -*- coding: utf-8 -*-
# snapshottest: v1 - https://goo.gl/zC4yUc
from __future__ import unicode_literals

from snapshottest import Snapshot


snapshots = Snapshot()

snapshots['TestCase25SaveAndActOnATaskAPITestCase.test_case[number] status_code'] = '400'

snapshots['TestCase25SaveAndActOnATaskAPITestCase.test_case[number] body'] = {
    'http_status_code': 400,
    'res_status': 'INVALID_NUMBER_VALUE',
    'response': 'Invalid number: number for field: FIELD_ID-1! Number should only consists digits'
}

snapshots['TestCase25SaveAndActOnATaskAPITestCase.test_case[one2] status_code'] = '400'

snapshots['TestCase25SaveAndActOnATaskAPITestCase.test_case[one2] body'] = {
    'http_status_code': 400,
    'res_status': 'INVALID_NUMBER_VALUE',
    'response': 'Invalid number: one2 for field: FIELD_ID-1! Number should only consists digits'
}

snapshots['TestCase25SaveAndActOnATaskAPITestCase.test_case[@2] status_code'] = '400'

snapshots['TestCase25SaveAndActOnATaskAPITestCase.test_case[@2] body'] = {
    'http_status_code': 400,
    'res_status': 'INVALID_NUMBER_VALUE',
    'response': 'Invalid number: @2 for field: FIELD_ID-1! Number should only consists digits'
}
