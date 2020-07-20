# -*- coding: utf-8 -*-
# snapshottest: v1 - https://goo.gl/zC4yUc
from __future__ import unicode_literals

from snapshottest import Snapshot


snapshots = Snapshot()

snapshots['TestCase04GetListOfTeamsAPITestCase.test_case status_code'] = '400'

snapshots['TestCase04GetListOfTeamsAPITestCase.test_case body'] = {
    'http_status_code': 400,
    'res_status': 'INVALID_OFFSET',
    'response': 'Given offset is invalid to retrieve list of teams'
}
