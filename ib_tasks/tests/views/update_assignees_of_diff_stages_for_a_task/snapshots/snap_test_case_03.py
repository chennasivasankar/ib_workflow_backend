# -*- coding: utf-8 -*-
# snapshottest: v1 - https://goo.gl/zC4yUc
from __future__ import unicode_literals

from snapshottest import Snapshot


snapshots = Snapshot()

snapshots['TestCase03UpdateAssigneesOfDiffStagesForATaskAPITestCase.test_case status_code'] = '400'

snapshots['TestCase03UpdateAssigneesOfDiffStagesForATaskAPITestCase.test_case body'] = {
    'http_status_code': 400,
    'res_status': 'DUPLICATE_STAGE_IDS',
    'response': 'Duplicate stage ids that you have sent are: [1],please send unique stage ids'
}
