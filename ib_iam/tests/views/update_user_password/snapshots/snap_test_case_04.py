# -*- coding: utf-8 -*-
# snapshottest: v1 - https://goo.gl/zC4yUc
from __future__ import unicode_literals

from snapshottest import Snapshot


snapshots = Snapshot()

snapshots['TestCase04UpdateUserPasswordAPITestCase.test_case status_code'] = '400'

snapshots['TestCase04UpdateUserPasswordAPITestCase.test_case body'] = {
    'http_status_code': 400,
    'res_status': 'CURRENT_PASSWORD_MISMATCH',
    'response': 'Given current password is not matching with the current password'
}
