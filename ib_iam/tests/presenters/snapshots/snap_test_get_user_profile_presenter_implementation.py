# -*- coding: utf-8 -*-
# snapshottest: v1 - https://goo.gl/zC4yUc
from __future__ import unicode_literals

from snapshottest import Snapshot


snapshots = Snapshot()

snapshots['TestGetUserProfilePresenterImplementation.test_prepare_response_for_user_profile_dto get_user_profile_response'] = {
    'company': {
        'company_id': 'f2c02d98-f311-4ab2-8673-3daa00757002',
        'description': 'company_description1',
        'employees': [
            {
                'employee_id': 'eca1a0c1-b9ef-4e59-b415-60a28ef17b10',
                'name': 'name1',
                'profile_pic_url': 'url1'
            },
            {
                'employee_id': '548a803c-7b48-47ba-a700-24f2ea0d1280',
                'name': 'name3',
                'profile_pic_url': 'url3'
            }
        ],
        'logo_url': 'logo_url1',
        'name': 'company1'
    },
    'email': 'name1@gmail.com',
    'is_admin': False,
    'name': 'name1',
    'profile_pic_url': 'url1',
    'teams': [
        {
            'description': 'team_description 1',
            'members': [
                {
                    'member_id': 'eca1a0c1-b9ef-4e59-b415-60a28ef17b10',
                    'name': 'name1',
                    'profile_pic_url': 'url1'
                },
                {
                    'member_id': '4b8fb6eb-fa7d-47c1-8726-cd917901104e',
                    'name': 'name2',
                    'profile_pic_url': 'url2'
                }
            ],
            'name': 'team 1',
            'team_id': '2bdb417e-4632-419a-8ddd-085ea272c6eb'
        }
    ],
    'user_id': 'eca1a0c1-b9ef-4e59-b415-60a28ef17b10'
}
