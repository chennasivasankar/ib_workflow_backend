# -*- coding: utf-8 -*-
# snapshottest: v1 - https://goo.gl/zC4yUc
from __future__ import unicode_literals

from snapshottest import Snapshot


snapshots = Snapshot()

snapshots['TestCase03AddTeamAPITestCase.test_case status_code'] = '400'

snapshots['TestCase03AddTeamAPITestCase.test_case body'] = {
    'http_status_code': 400,
    'res_status': 'TEAM_NAME_ALREADY_EXISTS',
    'response': "Given 'team1' is already exists, so choose another"
}
