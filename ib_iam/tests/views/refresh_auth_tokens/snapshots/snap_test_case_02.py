# -*- coding: utf-8 -*-
# snapshottest: v1 - https://goo.gl/zC4yUc
from __future__ import unicode_literals

from snapshottest import Snapshot


snapshots = Snapshot()

snapshots['TestCase02RefreshTokensAPITestCase.test_with_valid_details_return_response status_code'] = '200'

snapshots['TestCase02RefreshTokensAPITestCase.test_with_valid_details_return_response body'] = {
    'access_token': 'asdfaldskfjdfdlsdkf',
    'expires_in_seconds': 5647665599,
    'refresh_token': 'sadfenkljkdfeller'
}
