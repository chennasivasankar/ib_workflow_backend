# -*- coding: utf-8 -*-
# snapshottest: v1 - https://goo.gl/zC4yUc
from __future__ import unicode_literals

from snapshottest import Snapshot


snapshots = Snapshot()

snapshots['TestCase01AddTeamAPITestCase.test_case status_code'] = '201'

snapshots['TestCase01AddTeamAPITestCase.test_case body'] = {
    'team_id': '22a4f72a-eb54-47b5-8b50-c33c32e434f1'
}
