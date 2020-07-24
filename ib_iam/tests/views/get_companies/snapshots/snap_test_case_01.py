# -*- coding: utf-8 -*-
# snapshottest: v1 - https://goo.gl/zC4yUc
from __future__ import unicode_literals

from snapshottest import Snapshot


snapshots = Snapshot()

snapshots['TestCase01GetCompaniesAPITestCase.test_case status_code'] = '200'

snapshots['TestCase01GetCompaniesAPITestCase.test_case body'] = {
    'companies': [
        {
            'company_id': 'f3b6fc9f-7da7-43a3-b67e-4dba6989610a',
            'description': 'description 0',
            'logo_url': 'url 0',
            'name': 'company 0',
            'no_of_employees': 2
        },
        {
            'company_id': 'dfa3649a-734d-49fa-863a-8f75fe2d5548',
            'description': 'description 1',
            'logo_url': 'url 1',
            'name': 'company 1',
            'no_of_employees': 3
        },
        {
            'company_id': 'dbca1ba6-ffe1-4e06-987c-a59674c1aba4',
            'description': 'description 2',
            'logo_url': 'url 2',
            'name': 'company 2',
            'no_of_employees': 1
        }
    ]
}
