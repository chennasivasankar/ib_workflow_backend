# -*- coding: utf-8 -*-
# snapshottest: v1 - https://goo.gl/zC4yUc
from __future__ import unicode_literals

from snapshottest import Snapshot


snapshots = Snapshot()

snapshots['TestCase02AddTeamAPITestCase.test_case status_code'] = '401'

snapshots['TestCase02AddTeamAPITestCase.test_case body'] = {
    'http_status_code': 401,
    'res_status': 'USER_HAS_NO_ACCESS',
    'response': 'user has no access to see list of teams as he is not admin'
}
