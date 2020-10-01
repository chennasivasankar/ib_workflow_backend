# -*- coding: utf-8 -*-
# snapshottest: v1 - https://goo.gl/zC4yUc
from __future__ import unicode_literals

from snapshottest import Snapshot


snapshots = Snapshot()

snapshots['TestCase01UserLoginWithTokenAPITestCase.test_auth_user_already_exist_returns_response status_code'] = '200'

snapshots['TestCase01UserLoginWithTokenAPITestCase.test_auth_user_already_exist_returns_response body'] = {
    'access_token': 'access_token_0',
    'expires_in_seconds': 10000000000,
    'is_admin': False,
    'refresh_token': 'refresh_token_token_0'
}

snapshots['TestCase01UserLoginWithTokenAPITestCase.test_auth_user_already_exist_returns_response UserAuthDetails'] = {
    'auth_token_user_id': '89d96f4b-c19d-4e69-8eae-e818f3123b09',
    'id': 1,
    'token': 'token1',
    'user_id': 'user_id_1'
}
