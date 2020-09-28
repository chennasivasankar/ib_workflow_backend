# -*- coding: utf-8 -*-
# snapshottest: v1 - https://goo.gl/zC4yUc
from __future__ import unicode_literals

from snapshottest import Snapshot


snapshots = Snapshot()

snapshots['TestCase26CreateSubTaskAPITestCase.test_case[iB] status_code'] = '400'

snapshots['TestCase26CreateSubTaskAPITestCase.test_case[iB] body'] = {
    'http_status_code': 400,
    'res_status': 'INVALID_NUMBER_VALUE',
    'response': 'Invalid number: iB for field: DISPLAY_NAME-0! Number should only consists digits'
}

snapshots['TestCase26CreateSubTaskAPITestCase.test_case[700.0] status_code'] = '400'

snapshots['TestCase26CreateSubTaskAPITestCase.test_case[700.0] body'] = {
    'http_status_code': 400,
    'res_status': 'INVALID_NUMBER_VALUE',
    'response': 'Invalid number: 700.0 for field: DISPLAY_NAME-0! Number should only consists digits'
}
