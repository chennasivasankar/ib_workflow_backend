# -*- coding: utf-8 -*-
# snapshottest: v1 - https://goo.gl/zC4yUc
from __future__ import unicode_literals

from snapshottest import Snapshot


snapshots = Snapshot()

snapshots['TestCase04AddTeamAPITestCase.test_case status_code'] = '400'

snapshots['TestCase04AddTeamAPITestCase.test_case body'] = {
    'http_status_code': 400,
    'res_status': 'DUPLICATE_USERS',
    'response': 'Given users consists of duplicates, please check it'
}
