# -*- coding: utf-8 -*-
# snapshottest: v1 - https://goo.gl/zC4yUc
from __future__ import unicode_literals

from snapshottest import Snapshot


snapshots = Snapshot()

snapshots['TestCase19CreateSubTaskAPITestCase.test_case status_code'] = '400'

snapshots['TestCase19CreateSubTaskAPITestCase.test_case body'] = {
    'http_status_code': 400,
    'res_status': 'INVALID_STAGE_PERMITTED_GOFS',
    'response': "['GOF_DISPLAY_NAME-0'] gof ids are not permitted for the stage 1"
}
