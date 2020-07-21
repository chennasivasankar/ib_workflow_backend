# -*- coding: utf-8 -*-
# snapshottest: v1 - https://goo.gl/zC4yUc
from __future__ import unicode_literals

from snapshottest import Snapshot


snapshots = Snapshot()

snapshots['TestCase01GetListOfCompaniesAPITestCase.test_case status_code'] = '200'

snapshots['TestCase01GetListOfCompaniesAPITestCase.test_case body'] = {
    'list_of_companies': [
        {
            'company_id': 'string',
            'description': 'string',
            'logo': 'string',
            'name': 'string',
            'no_of_employees': 1
        }
    ],
    'total_companies': 1
}
