# -*- coding: utf-8 -*-
# snapshottest: v1 - https://goo.gl/zC4yUc
from __future__ import unicode_literals

from snapshottest import Snapshot


snapshots = Snapshot()

snapshots['TestCase01GetUserProfileAPITestCase.test_user_account_does_not_exist status_code'] = '404'

snapshots['TestCase01GetUserProfileAPITestCase.test_user_account_does_not_exist body'] = {
    'http_status_code': 404,
    'res_status': 'USER_ACCOUNT_DOES_NOT_EXIST',
    'response': 'Please send valid user id'
}

snapshots['TestCase01GetUserProfileAPITestCase.test_given_valid_user_id_returns_user_profile_data status_code'] = '200'

snapshots['TestCase01GetUserProfileAPITestCase.test_given_valid_user_id_returns_user_profile_data body'] = {
    'company': {
        'company_id': 'b9d000c7-c14f-4909-8c5a-6a6c02abb200',
        'description': 'description 0',
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
        'logo_url': 'url 0',
        'name': 'company 0',
        'roles': None
    },
    'cover_page_url': 'url0',
    'email': 'name1@gmail.com',
    'is_admin': False,
    'name': 'name1',
    'profile_pic_url': 'url1',
    'teams': [
        {
            'description': 'team_description 0',
            'members': [
                {
                    'member_id': '217abeb3-6466-4440-96e7-bf02ee941bf8',
                    'name': 'name1',
                    'profile_pic_url': 'url1'
                },
                {
                    'member_id': '7e39bf1c-f9a5-4e76-8451-b962ddd52044',
                    'name': 'name3',
                    'profile_pic_url': 'url3'
                }
            ],
            'name': 'team 0',
            'team_id': '6ce31e92-f188-4019-b295-2e5ddc9c7a11'
        }
    ],
    'user_id': '217abeb3-6466-4440-96e7-bf02ee941bf8'
}
