# -*- coding: utf-8 -*-
# snapshottest: v1 - https://goo.gl/zC4yUc
from __future__ import unicode_literals

from snapshottest import Snapshot


snapshots = Snapshot()

snapshots['TestCase01GetUserProfileAPITestCase.test_valid_user_id status_code'] = '200'

snapshots['TestCase01GetUserProfileAPITestCase.test_valid_user_id body'] = {
    'company': {
        'company_id': 'f2c02d98-f311-4ab2-8673-3daa00757002',
        'description': 'description 1',
        'employees': [
            {
                'employee_id': '217abeb3-6466-4440-96e7-bf02ee941bf8',
                'name': 'name1',
                'profile_pic_url': 'url1'
            },
            {
                'employee_id': '4b8fb6eb-fa7d-47c1-8726-cd917901104e',
                'name': 'name2',
                'profile_pic_url': 'url2'
            }
        ],
        'logo_url': 'url 1',
        'name': 'company 1'
    },
    'email': 'test@gmail.com',
    'is_admin': False,
    'name': 'test',
    'profile_pic_url': 'test.com',
    'teams': [
        {
            'description': 'team_description 1',
            'members': [
                {
                    'member_id': '217abeb3-6466-4440-96e7-bf02ee941bf8',
                    'name': 'name1',
                    'profile_pic_url': 'url1'
                },
                {
                    'member_id': '548a803c-7b48-47ba-a700-24f2ea0d1280',
                    'name': 'name3',
                    'profile_pic_url': 'url3'
                }
            ],
            'name': 'team 1',
            'team_id': '2bdb417e-4632-419a-8ddd-085ea272c6eb'
        }
    ],
    'user_id': '217abeb3-6466-4440-96e7-bf02ee941bf8'
}

snapshots['TestCase01GetUserProfileAPITestCase.test_user_account_does_not_exist status_code'] = '404'

snapshots['TestCase01GetUserProfileAPITestCase.test_user_account_does_not_exist body'] = {
    'http_status_code': 404,
    'res_status': 'USER_ACCOUNT_DOES_NOT_EXIST',
    'response': 'Please send valid user id'
}
