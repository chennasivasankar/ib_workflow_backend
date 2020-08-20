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

snapshots['TestCase01GetUserProfileAPITestCase.test_valid_user_id status_code'] = '200'

snapshots['TestCase01GetUserProfileAPITestCase.test_valid_user_id body'] = {
    'company': None,
    'cover_page_url': 'url0',
    'email': 'name1@gmail.com',
    'is_admin': False,
    'name': 'name1',
    'profile_pic_url': 'url1',
    'roles': [
    ],
    'teams': [
    ],
    'user_id': '217abeb3-6466-4440-96e7-bf02ee941bf8'
}