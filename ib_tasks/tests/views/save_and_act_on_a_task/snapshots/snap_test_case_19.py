# -*- coding: utf-8 -*-
# snapshottest: v1 - https://goo.gl/zC4yUc
from __future__ import unicode_literals

from snapshottest import Snapshot


snapshots = Snapshot()

snapshots['TestCase19SaveAndActOnATaskAPITestCase.test_case status_code'] = '400'

snapshots['TestCase19SaveAndActOnATaskAPITestCase.test_case body'] = {
    'http_status_code': 400,
    'res_status': 'INVALID_STAGE_PERMITTED_GOFS',
    'response': "['gof_1'] gof ids are not permitted for the stage 1"
}
