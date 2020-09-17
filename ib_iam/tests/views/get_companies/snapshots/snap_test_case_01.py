# -*- coding: utf-8 -*-
# snapshottest: v1 - https://goo.gl/zC4yUc
from __future__ import unicode_literals

from snapshottest import Snapshot


snapshots = Snapshot()

snapshots['TestCase01GetCompaniesAPITestCase.test_case status_code'] = '200'

snapshots['TestCase01GetCompaniesAPITestCase.test_case body'] = {
    'companies': [
        {
            'company_id': 'f2c02d98-f311-4ab2-8673-3daa00757003',
            'description': 'description 2',
            'employees': [
                {
                    'employee_id': '2bdb417e-4632-419a-8ddd-085ea272c6eb',
                    'name': 'name1',
                    'profile_pic_url': 'http://sample.com'
                },
                {
                    'employee_id': '7ee2c7b4-34c8-4d65-a83a-f87da75db24e',
                    'name': 'name4',
                    'profile_pic_url': 'http://sample.com'
                }
            ],
            'logo_url': 'http://sample.com',
            'name': 'Arogya'
        },
        {
            'company_id': 'f2c02d98-f311-4ab2-8673-3daa00757002',
            'description': 'description 1',
            'employees': [
                {
                    'employee_id': '2bdb417e-4632-419a-8ddd-085ea272c6eb',
                    'name': 'name1',
                    'profile_pic_url': 'http://sample.com'
                },
                {
                    'employee_id': '548a803c-7b48-47ba-a700-24f2ea0d1280',
                    'name': 'name2',
                    'profile_pic_url': 'http://sample.com'
                },
                {
                    'employee_id': '4b8fb6eb-fa7d-47c1-8726-cd917901104e',
                    'name': 'name3',
                    'profile_pic_url': 'http://sample.com'
                }
            ],
            'logo_url': 'http://sample.com',
            'name': 'Proyuga'
        }
    ]
}
