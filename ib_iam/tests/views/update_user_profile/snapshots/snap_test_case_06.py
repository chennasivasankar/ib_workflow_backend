# -*- coding: utf-8 -*-
# snapshottest: v1 - https://goo.gl/zC4yUc
from __future__ import unicode_literals

from snapshottest import Snapshot


snapshots = Snapshot()

snapshots['TestCase06UpdateUserProfileAPITestCase.test_case status_code'] = '400'

snapshots['TestCase06UpdateUserProfileAPITestCase.test_case body'] = {
    'http_status_code': 400,
    'res_status': 'EMAIL_ALREADY_IN_USE',
    'response': 'Email is already in use'
}
