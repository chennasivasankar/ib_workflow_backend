# -*- coding: utf-8 -*-
# snapshottest: v1 - https://goo.gl/zC4yUc
from __future__ import unicode_literals

from snapshottest import Snapshot


snapshots = Snapshot()

snapshots['TestCase03UpdateUserPasswordAPITestCase.test_case status_code'] = '400'

snapshots['TestCase03UpdateUserPasswordAPITestCase.test_case body'] = {
    'http_status_code': 400,
    'res_status': 'INVALID_CURRENT_PASSWORD',
    'response': 'Given current password is not valid'
}
