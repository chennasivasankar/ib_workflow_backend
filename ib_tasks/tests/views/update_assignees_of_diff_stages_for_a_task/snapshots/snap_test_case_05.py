# -*- coding: utf-8 -*-
# snapshottest: v1 - https://goo.gl/zC4yUc
from __future__ import unicode_literals

from snapshottest import Snapshot


snapshots = Snapshot()

snapshots['TestCase05UpdateAssigneesOfDiffStagesForATaskAPITestCase.test_case status_code'] = '400'

snapshots['TestCase05UpdateAssigneesOfDiffStagesForATaskAPITestCase.test_case body'] = {
    'http_status_code': 400,
    'res_status': 'VIRTUAL_STAGE_IDS',
    'response': 'Invalid stage ids that you have sent are: [2],please send valid stage ids'
}
