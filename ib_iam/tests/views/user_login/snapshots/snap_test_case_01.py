# -*- coding: utf-8 -*-
# snapshottest: v1 - https://goo.gl/zC4yUc
from __future__ import unicode_literals

from snapshottest import Snapshot


snapshots = Snapshot()

snapshots['TestCase01UserLoginAPITestCase.test_case status_code'] = '200'

snapshots['TestCase01UserLoginAPITestCase.test_case body'] = {
    'access_token': 'asdfaldskfjdfdlsdkf',
    'expires_in_seconds': 1000,
    'refresh_token': 'sadfenkljkdfeller'
}
