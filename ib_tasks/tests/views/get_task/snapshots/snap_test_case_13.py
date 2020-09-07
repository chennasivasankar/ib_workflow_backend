# -*- coding: utf-8 -*-
# snapshottest: v1 - https://goo.gl/zC4yUc
from __future__ import unicode_literals

from snapshottest import Snapshot


snapshots = Snapshot()

snapshots['TestCase13GetTaskAPITestCase.test_case status_code'] = '404'

snapshots['TestCase13GetTaskAPITestCase.test_case body'] = {
    'http_status_code': 404,
    'res_status': 'USER_NOT_A_MEMBER_OF_PROJECT',
    'response': 'user not a member of the project'
}
