# -*- coding: utf-8 -*-
# snapshottest: v1 - https://goo.gl/zC4yUc
from __future__ import unicode_literals

from snapshottest import Snapshot


snapshots = Snapshot()

snapshots['TestCase01UpdateTeamDetailsAPITestCase.test_case status_code'] = '400'

snapshots['TestCase01UpdateTeamDetailsAPITestCase.test_case body'] = {
    'http_status_code': 400,
    'res_status': 'TEAM_NAME_ALREADY_EXISTS',
    'response': "Given 'team2' is already exists, so updating name is not possible."
}
