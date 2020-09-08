# -*- coding: utf-8 -*-
# snapshottest: v1 - https://goo.gl/zC4yUc
from __future__ import unicode_literals

from snapshottest import Snapshot


snapshots = Snapshot()

snapshots['TestCase22CreateTransitionChecklistAPITestCase.test_case status_code'] = '400'

snapshots['TestCase22CreateTransitionChecklistAPITestCase.test_case body'] = {
    'http_status_code': 400,
    'res_status': 'INVALID_VALUE_FOR_DROPDOWN',
    'response': "Invalid dropdown value: Group for field: field_1! Try with these dropdown values: [{'name': 'Individual', 'gof_ids': ['FIN_VENDOR_BASIC_DETAILS']}, {'name': 'Company', 'gof_ids': ['FIN_VENDOR_COMPANY_DETAILS']}]"
}
