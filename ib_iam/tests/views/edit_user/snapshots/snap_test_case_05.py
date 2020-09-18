# -*- coding: utf-8 -*-
# snapshottest: v1 - https://goo.gl/zC4yUc
from __future__ import unicode_literals

from snapshottest import Snapshot


snapshots = Snapshot()

snapshots['TestCase05EditUserAPITestCase.test_give_invalid_team_ids_returns_invalid_team_ids_response status_code'] = '404'

snapshots['TestCase05EditUserAPITestCase.test_give_invalid_team_ids_returns_invalid_team_ids_response body'] = {
    'http_status_code': 404,
    'res_status': 'INVALID_TEAM_IDS',
    'response': 'given team ids are invalid'
}
