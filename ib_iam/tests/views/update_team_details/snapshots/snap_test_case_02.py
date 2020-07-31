# -*- coding: utf-8 -*-
# snapshottest: v1 - https://goo.gl/zC4yUc
from __future__ import unicode_literals

from snapshottest import Snapshot


snapshots = Snapshot()

snapshots['TestCase02UpdateTeamDetailsAPITestCase.test_case status_code'] = '401'

snapshots['TestCase02UpdateTeamDetailsAPITestCase.test_case body'] = {
    'http_status_code': 401,
    'res_status': 'USER_HAS_NO_ACCESS',
    'response': 'User has no access to update team details as he is not an admin'
}
