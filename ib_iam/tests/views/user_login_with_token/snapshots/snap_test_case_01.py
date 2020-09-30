# -*- coding: utf-8 -*-
# snapshottest: v1 - https://goo.gl/zC4yUc
from __future__ import unicode_literals

from snapshottest import Snapshot


snapshots = Snapshot()

snapshots['TestCase01UserLoginWithTokenAPITestCase.test_case status_code'] = '200'

snapshots['TestCase01UserLoginWithTokenAPITestCase.test_case body'] = {
    'access_token': 'access_token_0',
    'expires_in_seconds': 10000000000,
    'is_admin': False,
    'refresh_token': 'refresh_token_token_0'
}
