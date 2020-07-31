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
            'employees': [
                {
                    'employee_id': '2bdb417e-4632-419a-8ddd-085ea272c6eb',
                    'name': 'user1',
                    'profile_pic_url': 'url1'
                },
                {
                    'employee_id': '548a803c-7b48-47ba-a700-24f2ea0d1280',
                    'name': 'user2',
                    'profile_pic_url': 'url2'
                },
                {
                    'employee_id': '4b8fb6eb-fa7d-47c1-8726-cd917901104e',
                    'name': 'user3',
                    'profile_pic_url': 'url3'
                }
            ],
            'logo_url': 'url 1',
            'name': 'company 1'
        },
        {
            'company_id': 'aa66c40f-6d93-484a-b418-984716514c7b',
            'description': 'description 2',
            'employees': [
                {
                    'employee_id': '2bdb417e-4632-419a-8ddd-085ea272c6eb',
                    'name': 'user1',
                    'profile_pic_url': 'url1'
                },
                {
                    'employee_id': '7ee2c7b4-34c8-4d65-a83a-f87da75db24e',
                    'name': 'user4',
                    'profile_pic_url': 'url4'
                }
            ],
            'logo_url': 'url 2',
            'name': 'company 2'
        }
    ]
}
