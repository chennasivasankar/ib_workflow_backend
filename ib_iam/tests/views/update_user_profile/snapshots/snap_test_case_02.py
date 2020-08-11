# -*- coding: utf-8 -*-
# snapshottest: v1 - https://goo.gl/zC4yUc
from __future__ import unicode_literals

from snapshottest import Snapshot


snapshots = Snapshot()

snapshots['TestCase02UpdateUserProfileAPITestCase.test_case status_code'] = '400'

snapshots['TestCase02UpdateUserProfileAPITestCase.test_case body'] = {
    'http_status_code': 400,
    'res_status': 'NAME_MINIMUM_LENGTH_SHOULD_BE',
    'response': 'Name minimum length should be 5 or more'
}
