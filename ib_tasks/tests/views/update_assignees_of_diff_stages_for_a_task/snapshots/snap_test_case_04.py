# -*- coding: utf-8 -*-
# snapshottest: v1 - https://goo.gl/zC4yUc
from __future__ import unicode_literals

from snapshottest import Snapshot


snapshots = Snapshot()

snapshots['TestCase04UpdateAssigneesOfDiffStagesForATaskAPITestCase.test_case status_code'] = '404'

snapshots['TestCase04UpdateAssigneesOfDiffStagesForATaskAPITestCase.test_case body'] = {
    'http_status_code': 404,
    'res_status': 'INVALID_STAGE_IDS',
    'response': 'Invalid stage ids that you have sent are: [2, 3],please send valid stage ids'
}
