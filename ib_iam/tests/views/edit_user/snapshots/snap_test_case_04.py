# -*- coding: utf-8 -*-
# snapshottest: v1 - https://goo.gl/zC4yUc
from __future__ import unicode_literals

from snapshottest import Snapshot

snapshots = Snapshot()

snapshots['TestCase04EditUserAPITestCase.test_given_invalid_company_returns_invalid_company_response status_code'] = '404'

snapshots['TestCase04EditUserAPITestCase.test_given_invalid_company_returns_invalid_company_response body'] = {
    'http_status_code': 404,
    'res_status': 'INVALID_COMPANY_ID',
    'response': 'given company id is invalid'
}
