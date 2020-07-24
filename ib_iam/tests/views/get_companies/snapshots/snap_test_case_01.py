# -*- coding: utf-8 -*-
# snapshottest: v1 - https://goo.gl/zC4yUc
from __future__ import unicode_literals

from snapshottest import Snapshot


snapshots = Snapshot()

snapshots['TestCase01GetCompaniesAPITestCase.test_case status_code'] = '200'

snapshots['TestCase01GetCompaniesAPITestCase.test_case body'] = {
    'companies': [
        {
            'company_id': 'f2c02d98-f311-4ab2-8673-3daa00757002',
            'description': 'description 1',
            'logo_url': 'url 1',
            'name': 'company 1',
            'no_of_employees': 2
        },
        {
            'company_id': 'aa66c40f-6d93-484a-b418-984716514c7b',
            'description': 'description 2',
            'logo_url': 'url 2',
            'name': 'company 2',
            'no_of_employees': 3
        }
    ]
}
